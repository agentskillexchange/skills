#!/usr/bin/env python3
"""ASE Repo Quality Normalization Script"""
import os
import re
import yaml
from collections import Counter

SKILLS_DIR = 'skills'
STATS = {
    'total': 0,
    'frontmatter_fixes': 0,
    'install_fixes': 0,
    'verification_fixes': 0,
    'rating_review_fixes': 0,
    'source_url_fixes': 0,
    'creator_fixes': 0,
}

VERIFICATION_MAP = {
    '✅ Verified': 'security_reviewed',
    'Verified': 'verified_metadata',
    'verified': 'verified_metadata',
    'Community': 'listed',
    'community': 'listed',
    'Verified & Security Reviewed': 'security_reviewed',
    'Verified · Security Reviewed': 'security_reviewed',
    'Security Reviewed': 'security_reviewed',
    'security_reviewed': 'security_reviewed',
    'verified_metadata': 'verified_metadata',
    'listed': 'listed',
    'Verified ✅': 'security_reviewed',
    'Yes': 'verified_metadata',
    'Unverified': 'listed',
    'Security Reviewed ✓': 'security_reviewed',
    'Verified Metadata': 'verified_metadata',
    'Verified (Metadata)': 'verified_metadata',
    '': 'listed',
}

def parse_frontmatter(content):
    """Extract frontmatter between --- markers."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not m:
        return None, content
    return m.group(1), content[m.end():]

def normalize_verification(val):
    """Normalize verification field."""
    if val is None:
        return 'listed'
    val_str = str(val).strip().strip('"').strip("'")
    if val_str in VERIFICATION_MAP:
        return VERIFICATION_MAP[val_str]
    # Fallback: if it contains 'security' -> security_reviewed
    if 'security' in val_str.lower() or 'reviewed' in val_str.lower():
        return 'security_reviewed'
    if 'verified' in val_str.lower() or 'metadata' in val_str.lower():
        return 'verified_metadata'
    if val_str in ('security_reviewed', 'verified_metadata', 'listed'):
        return val_str
    return 'listed'

def build_install_section(slug):
    """Build the standard installation section."""
    return f"""## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill {slug}
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill {slug} -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill {slug} -a cursor
```

### OpenClaw
```bash
clawhub install {slug}
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill {slug} -a codex
```"""

def fix_install_section(body, slug):
    """Replace the installation section with the standard format."""
    # Find the Installation section
    pattern = r'(## Installation\s*\n)(.*?)(?=\n## (?!Installation)|$)'
    m = re.search(pattern, body, re.DOTALL)
    if not m:
        return body, False
    
    old_section = m.group(0)
    new_section = build_install_section(slug)
    
    # Check if it already matches the standard format
    # Quick check: does it have the right npx commands?
    has_standard = (
        f'npx skills add agentskillexchange/skills --skill {slug}\n' in old_section and
        f'-a claude-code' in old_section and
        f'-a cursor' in old_section and
        f'clawhub install {slug}' in old_section and
        f'-a codex' in old_section and
        'npx @anthropic' not in old_section and
        'claude skills' not in old_section and
        'codex skills add' not in old_section and
        'cursorrules' not in old_section.lower() and
        'Cursor Settings' not in old_section
    )
    
    if has_standard:
        return body, False
    
    new_body = body[:m.start()] + new_section + body[m.end():]
    return new_body, True

def rebuild_frontmatter(data):
    """Rebuild frontmatter as a clean YAML string with proper formatting."""
    lines = []
    field_order = ['name', 'description', 'category', 'framework', 'verification',
                   'rating', 'reviews', 'creator', 'creator_handle', 'creator_verified', 'source']
    
    for key in field_order:
        if key not in data:
            continue
        val = data[key]
        if key == 'verification':
            lines.append(f'verification: {val}')
        elif key == 'rating':
            lines.append(f'rating: {val}')
        elif key == 'reviews':
            lines.append(f'reviews: {val}')
        elif key == 'creator_verified':
            lines.append(f'creator_verified: {str(val).lower()}')
        else:
            # String fields: quote them
            val_str = str(val)
            if not (val_str.startswith('"') and val_str.endswith('"')):
                val_str = f'"{val_str}"'
            lines.append(f'{key}: {val_str}')
    
    # Add any extra fields not in the standard order
    for key in data:
        if key not in field_order:
            val = data[key]
            lines.append(f'{key}: {val}')
    
    return '\n'.join(lines)

def process_skill(skill_dir):
    """Process a single SKILL.md file."""
    slug = os.path.basename(skill_dir)
    filepath = os.path.join(skill_dir, 'SKILL.md')
    if not os.path.isfile(filepath):
        return None
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    STATS['total'] += 1
    
    fm_str, body = parse_frontmatter(content)
    if fm_str is None:
        return slug  # No frontmatter, skip
    
    changed_fm = False
    changed_install = False
    changed_verification = False
    changed_rating = False
    changed_source = False
    changed_creator = False
    
    # Parse frontmatter line by line for more control
    fm_data = {}
    for line in fm_str.strip().split('\n'):
        m = re.match(r'^(\w[\w_]*):\s*(.*)', line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            fm_data[key] = val
    
    # --- Fix verification ---
    raw_verif = fm_data.get('verification', '')
    # Strip quotes
    clean_verif = raw_verif.strip('"').strip("'").strip()
    normalized = normalize_verification(clean_verif)
    expected_verif = normalized  # bare, no quotes
    if raw_verif != expected_verif:
        fm_data['verification'] = expected_verif
        changed_verification = True
        changed_fm = True
    
    # --- Fix rating ---
    raw_rating = fm_data.get('rating', '0')
    clean_rating = raw_rating.strip('"').strip("'").strip()
    try:
        rating_val = float(clean_rating)
    except ValueError:
        rating_val = 0.0
    if rating_val > 5.0:
        rating_val = 5.0
    if rating_val < 0:
        rating_val = 0.0
    rating_formatted = f'{rating_val:.1f}' if rating_val > 0 else '0'
    # Fix 0 reviews but non-zero rating
    raw_reviews = fm_data.get('reviews', '0')
    clean_reviews = raw_reviews.strip('"').strip("'").strip()
    try:
        reviews_val = int(clean_reviews)
    except ValueError:
        reviews_val = 0
    if reviews_val == 0 and rating_val > 0:
        rating_val = 0.0
        rating_formatted = '0'
    
    expected_rating = rating_formatted
    expected_reviews = str(reviews_val)
    
    if raw_rating != expected_rating:
        fm_data['rating'] = expected_rating
        changed_rating = True
        changed_fm = True
    if raw_reviews != expected_reviews:
        fm_data['reviews'] = expected_reviews
        changed_rating = True
        changed_fm = True
    
    # --- Fix creator_verified ---
    raw_cv = fm_data.get('creator_verified', 'false')
    clean_cv = raw_cv.strip('"').strip("'").strip().lower()
    if clean_cv in ('true', 'yes', '✅', '1'):
        cv_val = 'true'
    else:
        cv_val = 'false'
    if raw_cv != cv_val:
        fm_data['creator_verified'] = cv_val
        changed_creator = True
        changed_fm = True
    
    # --- Fix source URL ---
    raw_source = fm_data.get('source', '')
    clean_source = raw_source.strip('"').strip("'").strip()
    if '/skill/' in clean_source and '/skills/' not in clean_source:
        new_source = clean_source.replace('/skill/', '/skills/')
        fm_data['source'] = f'"{new_source}"'
        changed_source = True
        changed_fm = True
    elif clean_source and not clean_source.startswith('"'):
        # Ensure source is quoted
        fm_data['source'] = f'"{clean_source}"'
        if raw_source != fm_data['source']:
            changed_fm = True
    
    # --- Fix creator quoting ---
    for field in ('name', 'description', 'category', 'framework', 'creator', 'creator_handle', 'source'):
        if field not in fm_data:
            continue
        val = fm_data[field]
        # Ensure string fields are quoted
        stripped = val.strip('"').strip("'")
        expected = f'"{stripped}"'
        if val != expected:
            fm_data[field] = expected
            if field in ('creator', 'creator_handle'):
                changed_creator = True
            changed_fm = True
    
    # --- Fix creator_handle @ prefix ---
    if 'creator_handle' in fm_data:
        handle = fm_data['creator_handle'].strip('"').strip("'")
        if handle and not handle.startswith('@'):
            handle = '@' + handle
            fm_data['creator_handle'] = f'"{handle}"'
            changed_creator = True
            changed_fm = True
    
    # --- Rebuild frontmatter ---
    if changed_fm:
        new_fm = rebuild_frontmatter(fm_data)
        content = f'---\n{new_fm}\n---\n{body}'
    
    # --- Fix install section ---
    # Re-parse body in case frontmatter rebuild changed offsets
    _, body = parse_frontmatter(content)
    new_body, install_fixed = fix_install_section(body, slug)
    if install_fixed:
        changed_install = True
        # Reconstruct with new body
        fm_part = content[:content.index('\n---\n', 4) + 5]
        content = fm_part + new_body
    
    # --- Write if changed ---
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        
        if changed_fm:
            STATS['frontmatter_fixes'] += 1
        if changed_install:
            STATS['install_fixes'] += 1
        if changed_verification:
            STATS['verification_fixes'] += 1
        if changed_rating:
            STATS['rating_review_fixes'] += 1
        if changed_source:
            STATS['source_url_fixes'] += 1
        if changed_creator:
            STATS['creator_fixes'] += 1
    
    return slug

def update_readme_badge(total):
    """Update README.md skill count badge."""
    readme_path = 'README.md'
    if not os.path.isfile(readme_path):
        return False
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Round to nearest 100+
    rounded = (total // 100) * 100
    badge_num = f'{rounded:,}+'
    badge_num_nospace = f'{rounded}+'  # for URL encoding
    
    # Replace skill count badges
    # Pattern: skills-NUMBER+-
    original = content
    content = re.sub(
        r'(skills-)[0-9,]+\+(-)',
        f'\\g<1>{badge_num_nospace}\\2',
        content
    )
    content = re.sub(
        r'(verified-)[0-9,]+\+(-)',
        f'\\g<1>{badge_num_nospace}\\2',
        content
    )
    # Also fix the URL-encoded version
    content = re.sub(
        r'(skills-)[0-9]%2C[0-9]+\+(-)',
        lambda m: f'{m.group(1)}{badge_num_nospace.replace(",", "%2C")}{m.group(2)}',
        content
    )
    
    if content != original:
        with open(readme_path, 'w') as f:
            f.write(content)
        return True
    return False

def find_duplicates():
    """Find skills with duplicate names."""
    names = Counter()
    for d in os.listdir(SKILLS_DIR):
        p = os.path.join(SKILLS_DIR, d, 'SKILL.md')
        if not os.path.isfile(p):
            continue
        with open(p) as f:
            for line in f:
                if line.startswith('name:'):
                    name = line.split(':', 1)[1].strip().strip('"').strip("'")
                    names[name] += 1
                    break
    return [(name, count) for name, count in names.most_common(10) if count > 1]

# --- Main ---
if __name__ == '__main__':
    skills = sorted(os.listdir(SKILLS_DIR))
    for skill_name in skills:
        skill_path = os.path.join(SKILLS_DIR, skill_name)
        if os.path.isdir(skill_path):
            process_skill(skill_path)
    
    badge_updated = update_readme_badge(STATS['total'])
    duplicates = find_duplicates()
    
    print(f"=== ASE Repo Quality Report ===")
    print(f"Total skills audited: {STATS['total']}")
    print(f"Frontmatter fixes: {STATS['frontmatter_fixes']} files")
    print(f"Install format fixes: {STATS['install_fixes']} files")
    print(f"Verification normalization: {STATS['verification_fixes']} files")
    print(f"Rating/review fixes: {STATS['rating_review_fixes']} files")
    print(f"Source URL fixes: {STATS['source_url_fixes']} files")
    print(f"Creator field fixes: {STATS['creator_fixes']} files")
    print(f"README badge updated: {'yes' if badge_updated else 'no'}")
    print(f"\nTop duplicate names:")
    for name, count in duplicates:
        print(f"  - {name}: {count} occurrences")
