#!/usr/bin/env python3
"""
ASE Repo Quality: normalize SKILL.md frontmatter, install sections, and README badges.
Runs inside /home/gachawla/.openclaw/workspace/ase-repo-review/
"""

import os
import re
import math
from pathlib import Path

REPO = Path(__file__).resolve().parent
SKILLS_DIR = REPO / "skills"

# Correct 5-method install block template
INSTALL_TEMPLATE = """## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill {slug} -a codex
```

### OpenClaw

```bash
clawhub install {slug}
```"""

stats = {
    "verified_metadata_to_listed": 0,
    "rating_zeroed": 0,
    "install_fixed": 0,
    "source_url_fixed": 0,
    "frontmatter_comment_normalized": 0,
    "total_skills": 0,
    "security_reviewed": 0,
    "listed": 0,
}

details = {
    "install_fixed": [],
    "verified_metadata_to_listed": [],
    "rating_zeroed": [],
    "source_url_fixed": [],
}


def fix_frontmatter(fm_text, slug):
    """Fix frontmatter issues, return (fixed_text, changes_made)."""
    changes = []
    lines = fm_text.split("\n")
    new_lines = []

    for line in lines:
        original = line

        # Fix verification: verified_metadata -> listed
        if re.match(r'^verification:\s*verified_metadata', line):
            line = re.sub(r'verification:\s*verified_metadata\b', 'verification: listed', line)
            # Normalize comment
            line = re.sub(r'#.*$', '# security_reviewed or listed', line)
            changes.append("verified_metadata->listed")
            stats["verified_metadata_to_listed"] += 1
            details["verified_metadata_to_listed"].append(slug)

        # Normalize verification comment format
        if re.match(r'^verification:\s*(security_reviewed|listed)', line):
            # Ensure consistent comment
            base = re.match(r'^(verification:\s*\S+)', line).group(1)
            line = f"{base}  # security_reviewed or listed"

        # Fix source URL: /skill/ -> /skills/
        if re.match(r'^source:', line) and '/skill/' in line and '/skills/' not in line:
            line = line.replace('/skill/', '/skills/')
            changes.append("source_url_fixed")
            stats["source_url_fixed"] += 1
            details["source_url_fixed"].append(slug)

        new_lines.append(line)

    fm_text = "\n".join(new_lines)

    # Check rating/reviews consistency
    rating_m = re.search(r'^rating:\s*(\S+)', fm_text, re.MULTILINE)
    reviews_m = re.search(r'^reviews:\s*(\S+)', fm_text, re.MULTILINE)
    if rating_m and reviews_m:
        try:
            rating = float(rating_m.group(1))
            reviews = int(reviews_m.group(1))
            if reviews == 0 and rating > 0:
                fm_text = re.sub(
                    r'^(rating:\s*)\S+',
                    r'\g<1>0',
                    fm_text,
                    count=1,
                    flags=re.MULTILINE,
                )
                changes.append("rating_zeroed")
                stats["rating_zeroed"] += 1
                details["rating_zeroed"].append(slug)
        except (ValueError, TypeError):
            pass

    return fm_text, changes


def fix_install_section(content, slug):
    """Replace the installation section with the standardized format."""
    # Try both ## Installation and ## Install headings
    install_start = -1
    heading_len = 0
    for heading in ["## Installation", "## Install"]:
        pos = content.find(heading)
        if pos != -1:
            install_start = pos
            heading_len = len(heading)
            break

    if install_start == -1:
        return content, False

    # Extract old section to check if already correct
    rest_after_heading = content[install_start + heading_len:]
    next_heading = re.search(r'\n(## [A-Z])', rest_after_heading)
    if next_heading:
        old_section = content[install_start:install_start + heading_len + next_heading.start()]
    else:
        old_section = content[install_start:]

    # Check if it already matches the correct format
    correct_markers = [
        "### Any Agent",
        "npx skills add agentskillexchange/skills --skill",
        "### Claude Code",
        "-a claude-code",
        "### Cursor",
        "-a cursor",
        "### Codex",
        "-a codex",
        "### OpenClaw",
        "clawhub install",
    ]

    if all(m in old_section for m in correct_markers):
        return content, False

    # Build new install section
    new_install = INSTALL_TEMPLATE.format(slug=slug)

    # Find next ## heading after the install heading
    if next_heading:
        end_pos = install_start + heading_len + next_heading.start()
        content = content[:install_start] + new_install + "\n" + content[end_pos:]
    else:
        # Installation is the last section - preserve trailing newline
        content = content[:install_start] + new_install + "\n"

    return content, True


def process_skill(skill_dir):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return

    slug = skill_dir.name
    stats["total_skills"] += 1

    content = skill_md.read_text(encoding="utf-8")

    # Parse frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return

    fm_text = fm_match.group(1)
    body = content[fm_match.end():]

    # Fix frontmatter
    fixed_fm, fm_changes = fix_frontmatter(fm_text, slug)

    # Fix install section
    fixed_body, install_changed = fix_install_section(body, slug)
    if install_changed:
        stats["install_fixed"] += 1
        details["install_fixed"].append(slug)

    # Count verification tiers
    ver_m = re.search(r'^verification:\s*(\S+)', fixed_fm, re.MULTILINE)
    if ver_m:
        tier = ver_m.group(1)
        if tier == "security_reviewed":
            stats["security_reviewed"] += 1
        elif tier == "listed":
            stats["listed"] += 1

    # Write back if changed
    if fm_changes or install_changed:
        new_content = f"---\n{fixed_fm}\n---{fixed_body}"
        skill_md.write_text(new_content, encoding="utf-8")


def fix_readme_badge(readme_path):
    """Update README.md badge count and trust tier table."""
    if not readme_path.is_file():
        return

    content = readme_path.read_text(encoding="utf-8")
    total = stats["total_skills"]

    # Round to nearest 100 with +
    rounded = int(math.ceil(total / 100) * 100)
    # Could also be floor — use the value that gets a "+" suffix
    # e.g. 1164 → "1,100+"
    badge_count = f"{(total // 100) * 100:,}".replace(",", "%2C")
    badge_label = f"{(total // 100) * 100:,}+"

    # Update skills badge
    content = re.sub(
        r'(skills-)\d[%\d,]*\+?(-6366f1)',
        f'\\g<1>{badge_count}%2B\\2',
        content,
    )

    # Update security reviewed badge count
    sr_count = stats["security_reviewed"]
    sr_rounded = f"{(sr_count // 100) * 100:,}".replace(",", "%2C")
    content = re.sub(
        r'(security_reviewed-)\d[%\d,]*(-10b981)',
        f'\\g<1>{sr_rounded}\\2',
        content,
    )

    # Update the tagline
    content = re.sub(
        r'\*\d[\d,]*\+? skills',
        f'*{badge_label} skills',
        content,
    )

    # Update trust tier table
    trust_table = f"""| Tier | Count | Meaning |
|------|------:|---|
| 📋 **Listed** | {total:,} | Published — backed by a real tool or project |
| 🛡️ **Security Reviewed** | {sr_count:,} | Scanned for malicious patterns, prompt injection, and unsafe instructions |"""

    content = re.sub(
        r'\| Tier \| Count \| Meaning \|.*?(?=\n\nMore:|\n\n---)',
        trust_table,
        content,
        flags=re.DOTALL,
    )

    readme_path.write_text(content, encoding="utf-8")


def main():
    # Process all skills
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if skill_dir.is_dir():
            process_skill(skill_dir)

    # Fix README
    fix_readme_badge(REPO / "README.md")

    # Print summary
    print(f"\n{'='*60}")
    print(f"ASE Repo Quality Review - Fix Summary")
    print(f"{'='*60}")
    print(f"Total skills scanned:           {stats['total_skills']}")
    print(f"Security Reviewed:              {stats['security_reviewed']}")
    print(f"Listed:                         {stats['listed']}")
    print(f"")
    print(f"Fixes applied:")
    print(f"  verified_metadata → listed:   {stats['verified_metadata_to_listed']}")
    print(f"  rating zeroed (0 reviews):    {stats['rating_zeroed']}")
    print(f"  install section normalized:   {stats['install_fixed']}")
    print(f"  source URL /skill/ → /skills/:{stats['source_url_fixed']}")
    print(f"  README badges updated:        yes")

    if details["install_fixed"]:
        print(f"\nInstall sections fixed ({len(details['install_fixed'])}):")
        for s in details["install_fixed"]:
            print(f"  - {s}")

    if details["verified_metadata_to_listed"]:
        print(f"\nverified_metadata → listed ({len(details['verified_metadata_to_listed'])}):")
        for s in details["verified_metadata_to_listed"]:
            print(f"  - {s}")

    if details["rating_zeroed"]:
        print(f"\nRating zeroed ({len(details['rating_zeroed'])}):")
        for s in details["rating_zeroed"]:
            print(f"  - {s}")

    if details["source_url_fixed"]:
        print(f"\nSource URL fixed ({len(details['source_url_fixed'])}):")
        for s in details["source_url_fixed"]:
            print(f"  - {s}")


if __name__ == "__main__":
    main()
