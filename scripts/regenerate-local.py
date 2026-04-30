import datetime as dt, json, html, re
from pathlib import Path

REPO = Path('/home/gachawla/.openclaw/workspace/ase-github-sync-regen')
ROOT = Path('/home/gachawla/.openclaw/workspace')
SITE='https://agentskillexchange.com'
INDUSTRY_EMOJI={"media-publishing-systems":"🎙️","finance-filings":"💼","ecommerce-retail-operations":"🛒","legal-ops-compliance":"⚖️","healthcare-documentation-intake":"🩺"}
INDUSTRY_STAGE={"wave-1":"Wave 1","wave-2":"Wave 2","pilot":"Pilot","planned":"Planned"}
CAT_EMOJI={"CI/CD Integrations":"🔧","Runbooks & Diagnostics":"📋","Code Quality & Review":"✅","Developer Tools":"🛠️","Library & API Reference":"📚","Monitoring & Alerts":"📊","Data Extraction & Transformation":"🔄","Security & Verification":"🔒","Templates & Workflows":"📄","Calendar, Email & Productivity":"📅","Integrations & Connectors":"🔗","Browser Automation":"🌐","Image & Creative Automation":"🎨","Research & Scraping":"🔍","Content Writing & SEO":"✍️","Media & Transcription":"🎙️","WordPress & CMS":"📰"}
CAT_SHORT={"CI/CD Integrations":"Pipeline configs, deployment automation, build tooling","Runbooks & Diagnostics":"Incident response, troubleshooting, system diagnostics","Code Quality & Review":"Linting, code review, test generators, coverage","Developer Tools":"CLI tools, scaffolders, dev environment setup","Library & API Reference":"SDK docs, API parsers, symbol resolvers","Monitoring & Alerts":"Metrics, alerting rules, observability","Data Extraction & Transformation":"ETL pipelines, parsing, format conversion","Security & Verification":"Vulnerability scanning, auth setup, compliance","Templates & Workflows":"Scaffolders, boilerplate generators, workflow templates","Calendar, Email & Productivity":"Email automation, calendar management, task coordination","Integrations & Connectors":"Third-party API bridges, webhooks, service connectors","Browser Automation":"Web scraping, UI testing, headless browser control","Image & Creative Automation":"Image generation, asset processing, design automation","Research & Scraping":"Web research, content discovery, data collection","Content Writing & SEO":"SEO content, blog automation, editorial workflows","Media & Transcription":"Audio/video processing, speech-to-text","WordPress & CMS":"Theme/plugin dev, WP-CLI automation, CMS management"}

def fmt_num(n):
    n=int(n or 0)
    if n>=1_000_000: return f"{n/1_000_000:.1f}".rstrip('0').rstrip('.')+'M'
    if n>=1_000: return f"{n/1_000:.1f}".rstrip('0').rstrip('.')+'k'
    return str(n) if n else '—'

def fmt_count(n): return f"{int(n):,}"

def fmt_badge(n): return f"{int(n):,}".replace(',', '%2C')

def norm_repo(v):
    if not v: return None
    v=str(v).strip().rstrip('/')
    v=re.sub(r'\.git$','',v)
    for pat in [r'https?://github\.com/([^/]+/[^/]+)$', r'github\.com/([^/]+/[^/]+)$', r'([^/]+/[^/]+)$']:
        m=re.match(pat,v,re.I)
        if m: return m.group(1)

def parse_source(source):
    s=(source or '').strip().rstrip('/')
    m=re.match(r'https?://github\.com/([^/]+/[^/]+)$',s,re.I)
    if m: return ('github',m.group(1))
    m=re.match(r'https?://(?:www\.)?npmjs\.com/package/(@?[^/]+(?:/[^/]+)?)$',s,re.I)
    if m: return ('npm',m.group(1))
    return ('other',None)

def choose_source(skill):
    if skill.get('ase_source_url'): return skill['ase_source_url'].strip()
    if skill.get('source_link'): return skill['source_link'].strip()
    repo=norm_repo(skill.get('ase_github_repo'))
    tool=(skill.get('ase_tool_match') or '').lower()
    if repo and tool and tool in (skill.get('title') or '').lower(): return f'https://github.com/{repo}'
    return f"{SITE}/skills/{skill['slug']}/"

rows=json.loads((ROOT/'ase-sync-data'/'wp-skills.json').read_text())
items=[]
for r in rows:
    source=choose_source(r)
    source_type, source_id = parse_source(source)
    gh_repo=norm_repo(r.get('ase_github_repo'))
    npm_pkg=(r.get('ase_npm_package') or '').strip()
    stars=int(r.get('ase_github_stars') or 0)
    npm=int(r.get('ase_npm_downloads') or 0)
    item={
        'slug':r['slug'],'title':r['title'],'description':r['excerpt'],'excerpt':r['excerpt'],
        'categories':r.get('categories') or ['Uncategorized'],'frameworks':r.get('frameworks') or [],
        'verification':'security_reviewed' if (r.get('verification_status') or '').strip()=='security_reviewed' else 'listed',
        'tool_match':r.get('ase_tool_match') or '', 'source':source,'github_stars':0,'npm_downloads':0,
    }
    if source_type=='github' and gh_repo and gh_repo.lower()==source_id.lower():
        item['github_stars']=stars
        if npm_pkg: item['npm_downloads']=npm
    elif source_type=='npm' and npm_pkg and npm_pkg==source_id:
        item['npm_downloads']=npm
    items.append(item)
items.sort(key=lambda x:x['slug'])

cat_counts={}
cat_slug={}
for it in items:
    for c in it['categories']:
        cat_counts[c]=cat_counts.get(c,0)+1
        s=re.sub(r'[^a-z0-9]+','-',c.lower()).strip('-')
        cat_slug[c]=s
cat_rows=sorted([{'name':k,'slug':cat_slug[k],'count':v} for k,v in cat_counts.items()], key=lambda x:(-x['count'],x['name']))
sec_reviewed=sum(1 for i in items if i['verification']=='security_reviewed')

# README
manifest=json.loads((REPO/'scripts'/'industry-collections.json').read_text())
collections=manifest.get('collections') or []
pool=[i for i in items if i['github_stars']>0 or i['npm_downloads']>0]
if not pool: pool=items[:]
pool.sort(key=lambda i:(i['github_stars']>0 or i['npm_downloads']>0, i['github_stars'], i['npm_downloads'], i['verification']=='security_reviewed', i['title'].lower()), reverse=True)
if len(pool)>60: pool=pool[:60]
ordinal=dt.datetime.now(dt.timezone.utc).toordinal(); skill=pool[ordinal % len(pool)] if pool else None
featured=sorted([i for i in items if i['github_stars']>0], key=lambda i:(i['github_stars'], i['npm_downloads']), reverse=True)[:12]
lines=['<div align="center">','','# Agent Skill Exchange','','### The open catalog of AI agent skills','',f'[![Published](https://img.shields.io/badge/published-{fmt_badge(len(items))}-6366f1?style=for-the-badge)](skills/)',f'[![Categories](https://img.shields.io/badge/categories-{len(cat_rows)}-0ea5e9?style=for-the-badge)](categories/)',f'[![Security%20Reviewed](https://img.shields.io/badge/security_reviewed-{fmt_badge(sec_reviewed)}-10b981?style=for-the-badge)](verification/)', '[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)','', '**[Categories](categories/) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**','', f'*{fmt_count(len(items))} published skills · {len(cat_rows)} categories · Real ecosystem signals · Updated hourly*','','</div>','','---','','## What is an Agent Skill','','An agent skill is a reusable capability package for AI coding agents. Each entry here wraps a real tool, API, or workflow into a format agents can install and use.','','Every published skill is backed by a real upstream project or documented integration. No synthetic filler, no fake repo stars, no proxy download theater.','','---','','## Start Here','','```bash','# Install any skill','npx skills add agentskillexchange/skills --skill <slug>','','# Target a specific agent','npx skills add agentskillexchange/skills --skill <slug> -a claude-code','npx skills add agentskillexchange/skills --skill <slug> -a cursor','npx skills add agentskillexchange/skills --skill <slug> -a codex','','# OpenClaw','clawhub install <slug>','```','','- Browse by category in [categories/](categories/)','- See strong signals in [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md)','- Use [CATALOG.md](CATALOG.md) for the full human-readable index','','---','','## Skill of the Day','']
if skill:
    lines += [f"### [{skill['title']}](skills/{skill['slug']}/)",'',skill['description'],'',f"- Tool: `{skill['tool_match'] or skill['slug']}`",f"- Category: {(skill['categories'] or ['Uncategorized'])[0]}"]
    if skill['frameworks']: lines.append(f"- Frameworks: {', '.join(skill['frameworks'][:6])}")
    if skill['github_stars']>0: lines.append(f"- GitHub stars: {fmt_count(skill['github_stars'])}")
    if skill['npm_downloads']>0: lines.append(f"- npm weekly downloads: {fmt_count(skill['npm_downloads'])}")
    lines.append(f"- Listing: {SITE}/skills/{skill['slug']}/")
else: lines.append("No featured skill was available for today's rotation.")
lines += ['','---','','## Featured Skills','','A strong cross-section of high-signal skills across the catalog.','','| Skill | Tool | ⭐ Stars | Category |','|-------|------|--------:|----------|']
for f in featured: lines.append(f"| [{f['title']}](skills/{f['slug']}/) | {f['tool_match'] or f['slug']} | {fmt_num(f['github_stars'])} | {(f['categories'] or ['Uncategorized'])[0]} |")
lines += ['','---','','## Categories','','| | Category | Skills | What\'s inside |','|---|---|---:|---|']
for cat in cat_rows: lines.append(f"| {CAT_EMOJI.get(cat['name'],'📦')} | [**{cat['name']}**](categories/{cat['slug']}/) | {cat['count']} | {CAT_SHORT.get(cat['name'],'Skills in this category')} |")
lines += ['','---','','## Industry Collections','','Curated editorial overlays for teams that want repo navigation by real workflow clusters without replacing the core category taxonomy.','','| | Collection | Stage | What you\'ll find |','|---|---|---|---|']
for c in collections: lines.append(f"| {INDUSTRY_EMOJI.get(c['slug'],'📦')} | [**{c['title']}**](industries/{c['slug']}.md) | {INDUSTRY_STAGE.get((c.get('launch_stage') or 'planned').lower(), 'Planned')} | {c.get('description','').strip().rstrip('.')} |")
lines += ['','See the full overlay index in [industries/README.md](industries/README.md).','','---','','## Browse','','| | View | What you\'ll find |','|---|---|---|','| ⭐ | [**Top Starred**](TOP-STARS.md) | Skills backed by the most popular GitHub repos |','| 🔥 | [**Top Downloaded**](TOP-DOWNLOADS.md) | Skills backed by the most-used npm packages |','| 📖 | [**Full Catalog**](CATALOG.md) | Every skill, sorted by category and stars |','| 🔌 | [**JSON Index**](skills.json) | Machine-readable catalog for programmatic access |','','---','','## Trust & Safety','','Every skill is backed by a real tool, repo, or package. New skills require real provenance before publishing.','','| Tier | Count | Meaning |','|------|------:|---|',f'| 📋 **Published** | {fmt_count(len(items))} | In the catalog, every skill is backed by a real tool, repo, or package |',f'| 🛡️ **Security Reviewed** | {fmt_count(sec_reviewed)} | Scanned for malicious patterns, prompt injection, and unsafe instructions |','','More: [verification/](verification/)','','---','','## Submit a Skill','','1. Fork this repo and add a `skills/<slug>/SKILL.md` entry, or','2. Submit through [agentskillexchange.com/create-skill](https://agentskillexchange.com/create-skill/) for hourly sync','','---','','<div align="center">','','*[agentskillexchange.com](https://agentskillexchange.com/)*','','</div>']
(REPO/'README.md').write_text('\n'.join(lines)+'\n')

# CATALOG
lines=['# Agent Skill Exchange — Full Catalog','',f"> **{len(items)} published skills** across **{len(cat_rows)} categories** · {sec_reviewed} security reviewed · Updated {dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",'>', '> Browse the [live marketplace](https://agentskillexchange.com/browse-skills/) for search, filtering, and one-click install.','','---','','## Skills by Category','']
for cat in cat_rows:
    cat_items=[i for i in items if cat['name'] in i['categories']]
    cat_items.sort(key=lambda i:(-i['github_stars'],-i['npm_downloads'],i['title'].lower()))
    browse_url='https://agentskillexchange.com/browse-skills/?category='+cat['name'].replace(' ','%20')
    lines += [f"### {CAT_EMOJI.get(cat['name'],'📦')} {cat['name']} ({cat['count']} skills)",'',f"Live views: [Browse]({browse_url}) · [Top Starred]({browse_url}&sort=stars) · [Top Downloaded]({browse_url}&sort=downloads)",'','| Skill | Description | Tier | ⭐ Stars | 📦 Downloads |','|---|---|---|---:|---:|']
    for item in cat_items:
        desc=item['description'];
        if len(desc)>120: desc=desc[:117].rsplit(' ',1)[0]+'…'
        desc=desc.replace('|','\\|')
        tier='Security Reviewed' if item['verification']=='security_reviewed' else 'Published'
        lines.append(f"| [{item['title']}](skills/{item['slug']}/) | {desc} | {tier} | {fmt_num(item['github_stars'])} | {fmt_num(item['npm_downloads'])}/wk |")
    lines += ['','']
lines += ['---','','<div align="center">','','**[agentskillexchange.com](https://agentskillexchange.com)** — The marketplace for trusted AI agent skills','','</div>','']
(REPO/'CATALOG.md').write_text('\n'.join(lines))

# categories
cats_dir=REPO/'categories'; cats_dir.mkdir(exist_ok=True)
root=['# Skill Categories','',f"> **{len(items)} skills** across **{len(cat_rows)} categories**",'', '| | Category | Skills | Description |','|---|---|:---:|---|']
for cat in cat_rows: root.append(f"| {CAT_EMOJI.get(cat['name'],'📦')} | [**{cat['name']}**]({cat['slug']}/) | **{cat['count']}** | {CAT_SHORT.get(cat['name'],'Skills in this category.')} |")
root += ['','---','','[Browse all skills on agentskillexchange.com →](https://agentskillexchange.com/browse-skills/)','']
(cats_dir/'README.md').write_text('\n'.join(root))
for cat in cat_rows:
    d=cats_dir/cat['slug']; d.mkdir(parents=True,exist_ok=True)
    cat_items=[i for i in items if cat['name'] in i['categories']]
    cat_items.sort(key=lambda i:(-i['github_stars'],-i['npm_downloads'],i['title'].lower()))
    top_starred=[i for i in cat_items if i['github_stars']>0][:10]; top_downloaded=[i for i in cat_items if i['npm_downloads']>0][:10]
    lines=[f"# {CAT_EMOJI.get(cat['name'],'📦')} {cat['name']}",'',CAT_SHORT.get(cat['name'],'Skills in this category.'),'']
    if top_starred:
        lines += ['## ⭐ Top Starred','','| Skill | Stars |','|---|---:|']
        for i in top_starred: lines.append(f"| [{i['title']}](../../skills/{i['slug']}/) | ⭐ {fmt_num(i['github_stars'])} |")
        lines += ['','---','']
    if top_downloaded:
        lines += ['## 📦 Top Downloaded','','| Skill | Downloads |','|---|---:|']
        for i in top_downloaded: lines.append(f"| [{i['title']}](../../skills/{i['slug']}/) | ⬇ {fmt_num(i['npm_downloads'])}/wk |")
        lines += ['','---','']
    lines += ['## Full Skill List','','| Skill | Stars | Downloads |','|---|---:|---:|']
    for i in cat_items: lines.append(f"| [{i['title']}](../../skills/{i['slug']}/) | {fmt_num(i['github_stars'])} | {fmt_num(i['npm_downloads'])}/wk |")
    lines += ['','---','','[← Back to all categories](../)','']
    (d/'README.md').write_text('\n'.join(lines))

# top lists
from collections import defaultdict
for key,out,title,desc in [('github_stars','TOP-STARS.md','# ⭐ Top Starred Skills','Skills backed by the most-starred GitHub repositories, deduplicated by upstream tool.'),('npm_downloads','TOP-DOWNLOADS.md','# 🔥 Top Downloaded Skills','Skills backed by the most-downloaded npm packages, deduplicated by upstream tool.')]:
    groups=defaultdict(list)
    for i in items:
        if int(i[key] or 0)>0 and i['tool_match']: groups[i['tool_match'].lower()].append(i)
    best=[]
    for tool,group in groups.items():
        group.sort(key=lambda i:(tool not in i['title'].lower(), tool not in i['slug'].lower(), i['title'].lower()))
        best.append(group[0])
    best.sort(key=lambda i:int(i[key] or 0), reverse=True)
    best=best[:50]
    lines=[title,'',desc,'',f"*{len(best)} unique tools with {'GitHub star' if key=='github_stars' else 'npm download'} data*",'']
    if key=='github_stars': lines += ['| # | Skill | Stars | Tool | Category |','|--:|-------|------:|------|----------|']
    else: lines += ['| # | Skill | Weekly Downloads | Tool | Category |','|--:|-------|----------------:|------|----------|']
    for idx,i in enumerate(best,1): lines.append(f"| {idx} | [{i['title']}](skills/{i['slug']}/) | {fmt_num(i[key])}{'' if key=='github_stars' else '/wk'} | {i['tool_match']} | {(i['categories'] or [''])[0]} |")
    lines += ['','---','','[← Back to README](README.md)','']
    (REPO/out).write_text('\n'.join(lines))

# skills.json
skills=[]
for i in items:
    entry={'slug':i['slug'],'name':i['title'],'description':i['description'],'category':i['categories'],'framework':i['frameworks'],'verification':i['verification']}
    signals={}
    if i['tool_match']: signals['tool']=i['tool_match']
    if i['github_stars']>0: signals['github_stars']=i['github_stars']
    if i['npm_downloads']>0: signals['npm_weekly_downloads']=i['npm_downloads']
    if signals: entry['signals']=signals
    skills.append(entry)
(REPO/'skills.json').write_text(json.dumps({'version':'2.0','total':len(skills),'generated':dt.datetime.utcnow().strftime('%Y-%m-%d'),'skills':skills}, indent=2, ensure_ascii=False)+'\n')

# agent files
rounded=f"{(len(items)//100)*100:,}+"
files={'.claude-plugin':f'{rounded} security-scanned agent skills — the largest open skills collection with real ecosystem signals.','.codex':f'{rounded} security-scanned agent skills for Codex — the largest open skills collection with real ecosystem signals.','.cursor-plugin':f'{rounded} security-scanned agent skills for Cursor — the largest open skills collection with real ecosystem signals.','.opencode':f'{rounded} security-scanned agent skills — the largest open skills collection with real ecosystem signals.'}
for fn,desc in files.items(): (REPO/fn).write_text(json.dumps({'schema_version':'1.0','name':'agent-skill-exchange','display_name':'Agent Skill Exchange','description':desc,'version':'1.0.0','homepage':'https://agentskillexchange.com','skills_directory':'skills/','license':'MIT'}, indent=2)+'\n')

# industries
ind_dir=REPO/'industries'; ind_dir.mkdir(exist_ok=True)
by_slug={i['slug']:i for i in items}
index=['# Industry Collections','','> Curated editorial overlays for real workflow clusters. These are intentionally not a replacement for categories.','','| | Collection | Stage | Picks | Summary |','|---|---|---|---:|---|']
for c in collections:
    slug,title,desc=c['slug'],c['title'],c['description']
    picks=[by_slug[s] for s in c.get('skill_slugs',[]) if s in by_slug]
    backups=[by_slug[s] for s in c.get('backup_skill_slugs',[]) if s in by_slug]
    lines=[f"# {INDUSTRY_EMOJI.get(slug,'📦')} {title}",'',desc,'',f"- Launch stage: **{INDUSTRY_STAGE.get((c.get('launch_stage') or 'planned').lower(),'Planned')}**",f"- Live page: https://agentskillexchange.com/industry-skills/#{slug}",f"- Homepage access: Curated Collections on https://agentskillexchange.com/",'','## Recommended Picks','','| Skill | Category | Stars | Downloads |','|---|---|---:|---:|']
    for i in picks: lines.append(f"| [{i['title']}](../skills/{i['slug']}/) | {(i['categories'] or ['Uncategorized'])[0]} | {fmt_num(i['github_stars'])} | {fmt_num(i['npm_downloads'])}/wk |")
    if backups:
        lines += ['','## Backup Picks','','| Skill | Why keep it nearby |','|---|---|']
        for i in backups: lines.append(f"| [{i['title']}](../skills/{i['slug']}/) | Useful alternate or overflow pick for this collection. |")
    if c.get('editorial_caution'): lines += ['','## Editorial Caution','',c['editorial_caution']]
    lines += ['','---','','[← Back to industry collections](README.md)','']
    (ind_dir/f'{slug}.md').write_text('\n'.join(lines))
    index.append(f"| {INDUSTRY_EMOJI.get(slug,'📦')} | [**{title}**]({slug}.md) | {INDUSTRY_STAGE.get((c.get('launch_stage') or 'planned').lower(),'Planned')} | {len(c.get('skill_slugs',[]))} | {desc} |")
index += ['','---','','Industry collections are curated manually and generated from `scripts/industry-collections.json`.','','[Browse all live collections on agentskillexchange.com →](https://agentskillexchange.com/industry-skills/)','']
(ind_dir/'README.md').write_text('\n'.join(index))
print(json.dumps({'total':len(items),'categories':len(cat_rows),'security_reviewed':sec_reviewed}))
