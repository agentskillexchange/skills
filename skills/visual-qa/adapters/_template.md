# Visual QA adapter: `<project>`

The adapter is the project-specific contract. Keep secrets, credentials, and real-account data out of this file.

## Project

- **repository:** repository-relative location or neutral identifier
- **application type:** web, native desktop, mobile, static, or other
- **supported themes:** light, dark, high-contrast, or project-specific
- **capture prerequisites:** runtime, package manager, browser/device, and local services

## Capability discovery

- **project-owned capture command:** exact command, if one exists
- **fallback capture tool:** only a tool verified to exist in the current host
- **image inspection tool:** how reviewers can open local screenshots
- **unsupported surfaces:** anything this setup cannot capture or inspect honestly

## Capture

- **command:** one command that builds, starts, drives, and captures the app
- **shots directory:** repository-relative and ignored by Git
- **manifest:** repository-relative `manifest.json` path
- **determinism:** how clock, timezone, locale, randomness, animations, and fixtures are pinned
- **flows:** user journeys with stable selectors or native accessibility identifiers
- **states:** default, empty, long-content, loading, error/offline, disabled, first-run, and relevant transitions
- **breakpoints/devices:** exact widths or device profiles
- **themes:** each supported theme
- **fixture seam:** how non-sensitive deterministic states are injected

## Verification

- **install command:**
- **unit command:**
- **build command:**
- **integration/end-to-end command:**
- **recapture command:**

## Committee

- **default tier:** quick, full, or deep
- **always-on specialists:** slugs from `roster.md`
- **deactivated specialists:** slugs that do not apply, with reasons
- **product-specific expert:** optional lens and negative constraint owned by this project

## Human-owned

- brand and taste decisions;
- real-account or sensitive-data judgment;
- approval of new golden images;
- authorization for external or irreversible actions.
