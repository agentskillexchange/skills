# Security Patterns

Human-readable companion to [`patterns.json`](patterns.json), the machine-readable source used by CI and discovery publish validation.

The executable contract is tested with:

```bash
python3 scripts/test_security_patterns.py
python3 scripts/security_scan.py skills --github-annotations --quiet
```

When this page and `patterns.json` disagree, `patterns.json` wins and this document should be updated.

---

## 1. Prompt Injection Indicators

16 executable pattern(s).

```
# prompt.ignore_previous [high]
/ignore (all |any )?(previous|prior|above|earlier) (instructions|prompts|rules)/i
# prompt.forget_rules [high]
/forget (everything|all|your) (you know|instructions|rules)/i
# prompt.you_are_now [medium]
/you are now/i
# prompt.from_now_on [medium]
/from now on,? (you|your)/i
# prompt.new_identity [medium]
/new (instructions|rules|persona|identity)/i
# prompt.act_as [medium]
/act as (a |an )?(?!the skill)/i
# prompt.system_block [high]
/^\s*(?:system|system prompt):?\s*$/im
# prompt.system_tag [high]
/\[system\]/i
# prompt.im_start_system [high]
/<\|im_start\|>system/i
# prompt.begin_instruction [high]
/BEGININSTRUCTION/i
# prompt.system_heading [high]
/###?\s*SYSTEM/i
# prompt.malicious_persona [high]
/you are (?:a |an )?(?:evil|malicious|unrestricted|unfiltered|jailbroken)/i
# prompt.pretend [medium]
/pretend (you are|to be)/i
# prompt.roleplay [medium]
/roleplay as/i
# prompt.delimiter_override [high]
/---\s*\n\s*(?:ignore|override|forget)/i
# prompt.code_fence_system [high]
/```\s*system/i
```

## 2. Data Exfiltration Patterns

12 executable pattern(s).

```
# exfil.curl_data_secret [high]
/curl\s+.*(?:--data|--upload|-d\s|-F\s|-T\s).*(?:\$|`|ENV|HOME|KEY|TOKEN|SECRET|PASS|CRED)/i
# exfil.wget_post [high]
/wget\s+--post/i
# exfil.curl_pipe_shell [high]
/curl\s+.*\|\s*(?:bash|sh|zsh)/i
# exfil.wget_pipe_shell [high]
/wget\s+-O\s*-.*\|\s*(?:bash|sh|zsh)/i
# exfil.nslookup_subshell [high]
/nslookup\s.*\$\(/i
# exfil.dig_subshell [high]
/dig\s.*\$\(/i
# exfil.ping_subshell [medium]
/ping\s+-c\s*1\s.*\$\(/i
# exfil.file_upload_service [high]
/curl\s+.*(?:transfer\.sh|file\.io|0x0\.st|uguu\.se|tmpfiles)/i
# exfil.paste_upload [high]
/upload.*(?:pastebin|hastebin|gist)/i
# exfil.credential_send [high]
/(?:cat|echo|print)\s+.*(?:\.env|\.ssh|\.aws|credentials|\.npmrc|\.pypirc).*(?:curl|wget|nc\s|netcat)/is
# exfil.base64_network [high]
/base64\s.*(?:curl|wget|nc\b)/i
# exfil.subshell_netcat [high]
/\$\(.*\)\s*\|\s*(?:nc|netcat)\s/i
```

## 3. Destructive Commands

21 executable pattern(s).

```
# destructive.rm_rf_root [high]
/rm\s+-[a-z]*r[a-z]*f?\s+(?:/|~|\$HOME|\$\(|`)/i
# destructive.rm_fr_root [high]
/rm\s+-[a-z]*f[a-z]*r?\s+(?:/|~|\$HOME|\$\(|`)/i
# destructive.rmdir_root [high]
/rmdir\s+--ignore-fail-on-non-empty\s+//i
# destructive.find_delete [high]
/find\s+/\s+.*-delete/i
# destructive.find_exec_rm [high]
/find\s+/\s+.*-exec\s+rm/i
# destructive.dd_disk [high]
/dd\s+if=/dev/(zero|urandom|random)\s+of=(?!/tmp)/i
# destructive.mkfs [high]
/mkfs\./i
# destructive.format_drive [high]
/format\s+[a-z]:/i
# destructive.fdisk [high]
/fdisk\s/i
# destructive.parted [high]
/parted\s/i
# destructive.wipefs [high]
/wipefs\s/i
# destructive.drop_database [high]
/DROP\s+(DATABASE|TABLE|SCHEMA)\s/i
# destructive.truncate_table [high]
/TRUNCATE\s+TABLE\s/i
# destructive.delete_from_all [high]
/DELETE\s+FROM\s+\w+\s*;?\s*$/im
# destructive.force_push_prod [high]
/git\s+push\s+.*--force\s+.*(?:main|master|production)/i
# destructive.large_hard_reset [medium]
/git\s+reset\s+--hard\s+HEAD~\d{2,}/i
# destructive.kill_all [high]
/kill\s+-9\s+-1/i
# destructive.killall [medium]
/killall\s/i
# destructive.shutdown [high]
/shutdown\s/i
# destructive.reboot [high]
/reboot\s*$/im
# destructive.init0 [high]
/init\s+0/i
```

## 4. Credential Harvesting

11 executable pattern(s).

```
# credentials.cat_secret_file [high]
/cat\s+.*(?:\.env|\.ssh/id_|\.aws/credentials|\.npmrc|\.pypirc|\.netrc|\.pgpass)/i
# credentials.read_secret_file [high]
/(?:less|more|head|tail|grep)\s+.*(?:\.env|id_rsa|\.pem|\.key)/i
# credentials.echo_secret_env [high]
/(?:echo|printf|print)\s+.*(?:\$[A-Z_]*(?:KEY|TOKEN|SECRET|PASS|CRED|AUTH))/i
# credentials.env_grep_secret [high]
/env\s*\|\s*grep\s*-i\s*(?:key|token|secret|pass|auth|cred)/i
# credentials.printenv_secret [high]
/printenv\s+(?:[A-Z_]*(?:KEY|TOKEN|SECRET|PASS))/i
# credentials.keychain [high]
/security\s+find-(?:generic|internet)-password/i
# credentials.keyring [medium]
/(?:keyctl\s+|keyring\s+(?:get|set|del|delete|list|dump|read))/i
# credentials.etc_shadow [high]
//etc/shadow/i
# credentials.passwd_send [high]
//etc/passwd.*(?:curl|wget|nc)/i
# credentials.kube_config [high]
/\.kube/config/i
# credentials.docker_config [high]
/\.docker/config\.json/i
```

## 5. Social Engineering Patterns

12 executable pattern(s).

```
# social.urgent_run [medium]
/(?:urgent|critical|emergency):?\s*(?:run|execute|do|send|delete)/i
# social.admin_override [medium]
/(?:admin|root|supervisor)\s+(?:override|authorization|approved)/i
# social.authorized_action [medium]
/this is (?:a |an )?(?:authorized|approved|sanctioned) (?:action|command|request)/i
# social.testing_run [medium]
/(?:for (?:testing|debugging|maintenance) (?:purposes|only)):?\s*(?:run|execute|send|delete|curl)/i
# social.temp_disable [medium]
/(?:temporary|temp) (?:fix|workaround):?\s*(?:chmod 777|disable|turn off)/i
# social.run_as_root [medium]
/(?:please |just )?(?:run|execute) (?:as |with )?(?:root|sudo|admin)/i
# social.chmod_open [medium]
/chmod\s+(?:777|666)\s+/i
# social.no_verify [medium]
/--no-verify/i
# social.disable_security [medium]
/(?:disable|turn off|bypass)\s+(?:security|firewall|auth|verification|ssl)/i
# social.no_worry_security [medium]
/(?:don't|do not) (?:worry|mind|concern yourself) about (?:security|permissions|safety)/i
# social.safe_to [low]
/(?:it's|its|this is) (?:safe|fine|harmless|normal) to/i
# social.trust_me [medium]
/(?:trust me|I promise|guaranteed safe)/i
```

## 6. Crypto Mining

1 executable pattern(s).

```
# malware.crypto_mining [high]
/\b(xmrig|coinhive|cryptonight|monero.*mine|bitcoin.*mine)\b/i
```

## 7. Reverse Shells

4 executable pattern(s).

```
# malware.reverse_shell_netcat [high]
/\bnc\s+-[el].*(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\$)/i
# malware.reverse_shell_bash [high]
//bin/(?:bash|sh)\s+-i\s*[>&]/i
# malware.reverse_shell_python [high]
/python[23]?\s+-c\s+["']import\s+socket/i
# malware.reverse_shell_ruby [high]
/ruby\s+-[re].*TCPSocket/i
```

## 8. Obfuscated Payloads

2 executable pattern(s).

```
# malware.obfuscated_eval [medium]
/\beval\s*\(\s*(atob|Buffer\.from|decode)/i
# malware.hex_payload [medium]
/\\x[0-9a-f]{2}\\x[0-9a-f]{2}\\x[0-9a-f]{2}/i
```

---

## Usage

These patterns are used in three ways:

1. **CI security scanning** — `scripts/security_scan.py` scans `skills/*/SKILL.md` against `verification/patterns.json`.
2. **Discovery publish validation** — private publish validation consumes the same pattern source when available, so new skills are blocked before WordPress publish.
3. **Manual review** — reviewers use this document to understand what automated findings mean.

### False Positive Handling

Some legitimate skills may mention risky commands as defensive education. Reviewers assess context:

- Is the command being taught about or instructed to run?
- Is a network call part of a legitimate documented integration, or exfiltration?
- Is the text warning against the action, or asking an agent/operator to perform it?

### Reporting New Patterns

If you discover a malicious pattern not covered here, report it via [SECURITY.md](../SECURITY.md) and add it to `patterns.json` with a fixture when possible.
