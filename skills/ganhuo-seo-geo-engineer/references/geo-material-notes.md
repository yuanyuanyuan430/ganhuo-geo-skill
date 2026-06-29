# GEO Material Notes

## Material States

Use these internal states when handling material:

| State | Meaning | Action |
| --- | --- | --- |
| supplied | Present in the user material | Can be used |
| verified | Checked during the task | Can be used with care |
| missing | Needed but absent | Add to backlog |
| risky | May be outdated, private, or unsupported | Soften or remove |

## Mixed Materials

When the user provides multiple files, pages, notes, or screenshots:

1. Build a material inventory.
2. Deduplicate repeated claims.
3. Separate facts from opinions.
4. Keep privacy-sensitive material out of public examples.
5. Return unresolved gaps as backlog items.

## Time-Sensitive Facts

Market data, laws, product pricing, platform rules, model behavior, rankings, and search features can change. Verify them when the task depends on current accuracy; otherwise, mark them as backlog.

## Public Output Hygiene

Before creating a public artifact:

- remove private customer data;
- remove API keys, tokens, and internal URLs;
- anonymize examples unless the user confirms they are public;
- do not include raw private prompts or outputs.

