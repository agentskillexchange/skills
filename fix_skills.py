#!/usr/bin/env python3
"""ASE Repo Quality: normalize SKILL.md frontmatter, install commands, body links, and data consistency."""

import os
import re
from collections import Counter

SKILLS_DIR = "skills"

VALID_VERIFICATIONS = {"security_reviewed", "verified_metadata", "listed"}

# Framework normalization map
FRAMEWORK_MAP = {
    "MCP-compatible": "MCP",
    "Unknown": "Custom Agents",
    "unknown": "Custom Agents",
}

# Category normalization
CATEGORY_MAP = {
    "Uncategorized": "Developer Tools",
}

# Verification normalization
VERIFICATION_MAP = {
    "Community": "listed",
    "Verified": "verified_metadata",
    "Verified · Security Reviewed": "security_reviewed",
}

stats = {
    "total": 0,
    "files_changed": 0,
    "framework_fixes": 0,
    "category_fixes": 0,
    "verification_fixes": 0,
    "rating_review_fixes": 0,
    "source_url_fixes": 0,
    "body_link_fixes": 0,
    "frontmatter_misc_fixes": 0,
}


def process_skill(slug, filepath):
    with open(filepath, "r") as f:
        content = f.read()

    original = content
    fixed_areas = set()

    # Split into frontmatter and body
    parts = content.split("---", 2)
    if len(parts) < 3:
        return False

    fm_text = parts[1]
    body = parts[2]

    # --- VERIFICATION normalization ---
    vm = re.search(r'^verification:\s*(.+)$', fm_text, re.M)
    if vm:
        raw = vm.group(1).strip()
        if raw not in VALID_VERIFICATIONS:
            # Strip quotes if present
            stripped = raw.strip('"').strip("'").strip()
            if stripped in VERIFICATION_MAP:
                mapped = VERIFICATION_MAP[stripped]
            elif stripped == "":
                mapped = "listed"
            else:
                mapped = "listed"
            fm_text = re.sub(r'^verification:\s*.+$', f'verification: {mapped}', fm_text, count=1, flags=re.M)
            fixed_areas.add("verification")

    # --- FRAMEWORK normalization ---
    fwm = re.search(r'^framework:\s*"(.*?)"', fm_text, re.M)
    if fwm:
        fw = fwm.group(1)
        if fw in FRAMEWORK_MAP:
            new_fw = FRAMEWORK_MAP[fw]
            fm_text = re.sub(r'^framework:\s*".*?"', f'framework: "{new_fw}"', fm_text, count=1, flags=re.M)
            fixed_areas.add("framework")

    # --- CATEGORY normalization ---
    cm = re.search(r'^category:\s*"(.*?)"', fm_text, re.M)
    if cm:
        cat = cm.group(1)
        if cat in CATEGORY_MAP:
            new_cat = CATEGORY_MAP[cat]
            fm_text = re.sub(r'^category:\s*".*?"', f'category: "{new_cat}"', fm_text, count=1, flags=re.M)
            fixed_areas.add("category")

    # --- RATING/REVIEW consistency ---
    rm = re.search(r'^rating:\s*(.+)$', fm_text, re.M)
    revm = re.search(r'^reviews:\s*(.+)$', fm_text, re.M)
    if rm and revm:
        rating_raw = rm.group(1).strip().strip('"').strip("'")
        reviews_raw = revm.group(1).strip().strip('"').strip("'")
        try:
            rating = float(rating_raw)
            reviews = int(reviews_raw)
            need_fix = False
            new_rating = rating
            new_reviews = reviews

            # Quoted values
            if '"' in rm.group(1) or "'" in rm.group(1):
                need_fix = True
            if '"' in revm.group(1) or "'" in revm.group(1):
                need_fix = True

            # No reviews but has rating
            if reviews == 0 and rating > 0:
                new_rating = 0.0
                need_fix = True

            # Out of range
            if rating > 5.0:
                new_rating = 5.0
                need_fix = True
            if rating < 0:
                new_rating = 0.0
                need_fix = True

            if need_fix:
                if new_rating == 0:
                    fm_text = re.sub(r'^rating:\s*.+$', 'rating: 0', fm_text, count=1, flags=re.M)
                else:
                    fm_text = re.sub(r'^rating:\s*.+$', f'rating: {new_rating:.1f}', fm_text, count=1, flags=re.M)
                fm_text = re.sub(r'^reviews:\s*.+$', f'reviews: {new_reviews}', fm_text, count=1, flags=re.M)
                fixed_areas.add("rating_review")
        except ValueError:
            pass

    # --- SOURCE URL: ensure /skills/ not /skill/ in frontmatter ---
    sm = re.search(r'^source:\s*"(.*?)"', fm_text, re.M)
    if sm:
        url = sm.group(1)
        # Only fix if it has /skill/ but not /skills/
        if "/skill/" in url:
            # Check it's not already /skills/
            if not re.search(r'/skills/', url):
                new_url = url.replace("/skill/", "/skills/")
                fm_text = re.sub(r'^source:\s*".*?"', f'source: "{new_url}"', fm_text, count=1, flags=re.M)
                fixed_areas.add("source_url")

    # --- CREATOR_VERIFIED: ensure boolean not string ---
    cvm = re.search(r'^creator_verified:\s*(.+)$', fm_text, re.M)
    if cvm:
        raw_cv = cvm.group(1).strip()
        if raw_cv == '"true"' or raw_cv == "'true'":
            fm_text = re.sub(r'^creator_verified:\s*.+$', 'creator_verified: true', fm_text, count=1, flags=re.M)
            fixed_areas.add("frontmatter_misc")
        elif raw_cv == '"false"' or raw_cv == "'false'":
            fm_text = re.sub(r'^creator_verified:\s*.+$', 'creator_verified: false', fm_text, count=1, flags=re.M)
            fixed_areas.add("frontmatter_misc")

    # Reassemble with fixed frontmatter
    content = f"---{fm_text}---{body}"

    # --- BODY LINKS: /skill/ → /skills/ (but not already /skills/) ---
    # Use regex to be precise
    content_new = re.sub(
        r'agentskillexchange\.com/skill/',
        'agentskillexchange.com/skills/',
        content
    )
    if content_new != content:
        content = content_new
        fixed_areas.add("body_link")

    # Write if changed
    if content != original:
        with open(filepath, "w") as f:
            f.write(content)
        
        for area in fixed_areas:
            if area in stats:
                stats[f"{area}_fixes"] += 1
            elif f"{area}_fixes" in stats:
                stats[f"{area}_fixes"] += 1
        
        # Map area names to stat keys properly
        if "verification" in fixed_areas:
            stats["verification_fixes"] += 1
        if "framework" in fixed_areas:
            stats["framework_fixes"] += 1
        if "category" in fixed_areas:
            stats["category_fixes"] += 1
        if "rating_review" in fixed_areas:
            stats["rating_review_fixes"] += 1
        if "source_url" in fixed_areas:
            stats["source_url_fixes"] += 1
        if "body_link" in fixed_areas:
            stats["body_link_fixes"] += 1
        if "frontmatter_misc" in fixed_areas:
            stats["frontmatter_misc_fixes"] += 1
        
        stats["files_changed"] += 1
        return True

    return False


def fix_readme_badge():
    readme_path = "README.md"
    if not os.path.isfile(readme_path):
        return False

    with open(readme_path) as f:
        content = f.read()

    skill_count = len([
        d for d in os.listdir(SKILLS_DIR)
        if os.path.isfile(os.path.join(SKILLS_DIR, d, "SKILL.md"))
    ])

    # Round to nearest 100
    rounded = (skill_count // 100) * 100
    # Badge format: skills-1%2C500+-
    badge_num = f"{rounded:,}".replace(",", "%2C")

    original = content
    content = re.sub(
        r'skills-[\d%2C,]+\+-',
        f'skills-{badge_num}+-',
        content
    )

    if content != original:
        with open(readme_path, "w") as f:
            f.write(content)
        return True
    return False


def find_duplicates():
    names = []
    for d in sorted(os.listdir(SKILLS_DIR)):
        p = os.path.join(SKILLS_DIR, d, "SKILL.md")
        if not os.path.isfile(p):
            continue
        with open(p) as f:
            content = f.read()
        m = re.search(r'^name:\s*"(.*?)"', content, re.M)
        if m:
            names.append((m.group(1), d))

    name_counts = Counter(n for n, _ in names)
    return [(n, c) for n, c in name_counts.most_common(10) if c > 1]


def main():
    for d in sorted(os.listdir(SKILLS_DIR)):
        p = os.path.join(SKILLS_DIR, d, "SKILL.md")
        if not os.path.isfile(p):
            continue
        stats["total"] += 1
        process_skill(d, p)

    badge_updated = fix_readme_badge()
    duplicates = find_duplicates()

    print("=== ASE Repo Quality Report ===")
    print(f"Total skills audited: {stats['total']}")
    print(f"Files changed: {stats['files_changed']}")
    print(f"Framework fixes (MCP-compatible→MCP, Unknown→Custom Agents): {stats['framework_fixes']}")
    print(f"Category fixes (Uncategorized→Developer Tools): {stats['category_fixes']}")
    print(f"Verification fixes: {stats['verification_fixes']}")
    print(f"Rating/review fixes: {stats['rating_review_fixes']}")
    print(f"Source URL fixes (frontmatter): {stats['source_url_fixes']}")
    print(f"Body link fixes (/skill/→/skills/): {stats['body_link_fixes']}")
    print(f"Other frontmatter fixes: {stats['frontmatter_misc_fixes']}")
    print(f"README badge updated: {'yes' if badge_updated else 'no (already correct)'}")
    print()
    print("Top 10 duplicate names:")
    for name, count in duplicates:
        print(f"  x{count:2d}  \"{name}\"")
    print()
    print("Note: Duplicates flagged for review but not deleted (may be valid variants).")


if __name__ == "__main__":
    main()
