---
name: "Pangolinfo Amazon Scraper"
slug: "pangolinfo-amazon-scraper"
description: "Retrieve structured Amazon product, keyword search, category, seller and bestseller data with Pangolinfo APIs for e-commerce research and agent workflows."
category: "Research & Scraping"
framework: "OpenClaw"
verification: listed
source: "https://github.com/Pangolin-spg/openclaw-skills/tree/main/pangolinfo-amazon-scraper"
---

# Pangolinfo Amazon Scraper

This skill connects an OpenClaw workflow to the documented Pangolinfo Amazon Scraper API. Use it when a user needs structured product details, keyword search results, category listings, seller product lists, or bestseller data for e-commerce research. The upstream package includes a SKILL.md, a Python helper, and reference documentation. Python 3.6 or later is required; the helper uses the standard library.

Choose the parser that matches the user request: amzProductDetail for a product URL, amzKeyword for keyword search, amzProductOfCategory for category pages, amzProductOfSeller for seller pages, or amzBestSellers for bestseller pages. The helper accepts a ZIP code for localized pricing and supports JSON, raw HTML, or Markdown output. Preserve source URLs and distinguish unavailable fields from zero values when reporting results.

Pangolinfo is an independent data provider, not an official Amazon service. The skill source is MIT licensed, but API access requires a Pangolinfo account and credentials. Limited trial credits are available; subsequent API usage is paid. This listing does not assert a security review or testing in every agent client.

## Installation

Clone the canonical upstream repository and install the complete skill folder using your OpenClaw skill workflow:

```bash
git clone https://github.com/Pangolin-spg/openclaw-skills.git
cd openclaw-skills/pangolinfo-amazon-scraper
```

Keep scripts/ and references/ alongside SKILL.md; copying this catalog summary alone is not a functional installation. Set PANGOLIN_TOKEN in your local environment, or use PANGOLIN_EMAIL and PANGOLIN_PASSWORD as documented upstream. Never put real credentials in prompts, commits, or public submissions. Review the upstream code before running it.

From the installed skill directory, a keyword request is:

```bash
python3 scripts/pangolinfo.py --q "wireless mouse" --parser amzKeyword
```

Make only the requests authorized by the user, and confirm the expected usage cost before a large batch.

## Documentation

- [Skill product page](https://www.pangolinfo.com/amazon-scraper-skill/)
- [Amazon Scraper API](https://www.pangolinfo.com/amazon-scraper-api/)
- [API reference](https://docs.pangolinfo.com/en-api-reference/amazonApi/amazonScrapeAPI)
- [Canonical source and full installation files](https://github.com/Pangolin-spg/openclaw-skills/tree/main/pangolinfo-amazon-scraper)
