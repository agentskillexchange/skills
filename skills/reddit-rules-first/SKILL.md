---
name: "Reddit Rules First"
slug: "reddit-rules-first"
description: "Post to Reddit the way communities accept it: read each subreddit's rules (self-promotion limits, promo threads, flair, account minimums) before writing, write one fresh post per community, disclose affiliation, and check at 1, 6 and 24 hours whether each post stayed up."
verification: "listed"
source: "https://github.com/amflimited/threadfox-lite"
author: "amflimited"
publisher_type: "organization"
category: "Content Writing & SEO"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "amflimited/threadfox-lite"
---

# Reddit, rules first

Most Reddit promotion fails for the same reasons: the post ignores the community's rules, the same text goes to many subreddits, or nobody checks whether it was removed. Use this workflow whenever you are asked to share, launch or promote something on Reddit.

## Before writing

1. Pick communities where the product answers a question people there already ask. Fit comes before size.
2. Read each community's rules the day you post: `https://www.reddit.com/r/<name>/about/rules` and the sidebar. With the ThreadFox Lite MCP server (same source repo), call `subreddit_rules`; `find_communities` lists candidates with their promotion rules flagged, and `account_check` shows whether the account's recent posts are being removed or hidden.
3. Look for self-promotion limits (for example a 10% rule), a weekly promo thread, required flair, link bans, and account age or karma minimums. If self-promotion isn't allowed, use the promo thread or don't post the link.

## Writing

4. Write a new title and body for each community. Never paste the same post twice.
5. Say it's yours in the first lines ("I built this", "I'm with the team").
6. Lead with something useful on its own: what you learned, real numbers, a how-to. The link is the footnote.

## Posting

7. Space posts out: minutes between them, never a burst of communities in one hour.
8. Stay for the comments and answer real questions in the first few hours.

## After posting

9. Check at 1, 6 and 24 hours whether each post is still up (ThreadFox Lite: `post_status`).
10. If a community removes you twice, stop posting there. Don't repost removed content.
