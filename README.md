# ganhuo-seo-geo-skill

`ganhuo-seo-geo-skill` is a compact, original Skill repository for turning existing articles, product pages, tutorials, and knowledge materials into GEO and AI-search-friendly content assets.

The first Skill is `ganhuo-seo-geo-engineer`: a practical old-content rebuild workflow for Ganhuo AI and compatible agent runtimes. It focuses on content truth, structure, evidence gaps, reusable outputs, and reviewable delivery.

## What This Repo Is

This is a single-Skill repo, not a large framework collection.

It helps an agent:

- preserve the original article's meaning before rewriting;
- diagnose evidence, structure, entity, question, and readability gaps;
- rebuild the content into an AI-answer-friendly asset;
- mark unsupported improvements as action items instead of inventing data;
- return a reusable delivery package with score, change notes, backlog, and risk notes.

## What It Is Not

- It does not guarantee rankings, traffic, citations, or model recommendations.
- It does not fabricate statistics, quotes, cases, customers, or research.
- It is not a GEOFlow operations wrapper.
- It is not a generic copywriting assistant.
- It is not a black-hat keyword-stuffing tool.

## Install / Use

Copy the Skill folder into your local agent Skill directory:

```bash
cp -R skills/ganhuo-seo-geo-engineer ~/.codex/skills/
```

Then ask your agent to use `ganhuo-seo-geo-engineer` for an existing article rewrite, for example:

```text
Use ganhuo-seo-geo-engineer to rebuild this old article into a GEO-friendly content asset.
Keep the original claims, do not invent data, and return the rewritten article, scorecard, change notes, backlog, and risk notes.
```

## Repo Layout

```text
ganhuo-seo-geo-skill/
├── README.md
├── LICENSE
├── manifest.json
├── scripts/
│   └── validate_skill.py
├── examples/
│   ├── 01-real-brief.md
│   ├── 02-ideal-output.md
│   └── 03-failure-cases.md
└── skills/
    └── ganhuo-seo-geo-engineer/
        ├── SKILL.md
        ├── manifest.json
        ├── templates/
        │   └── article-brief.md
        ├── evals/
        │   ├── trigger_cases.json
        │   └── expected_artifacts.json
        └── references/
            ├── geo-material-notes.md
            ├── geo-playbook.md
            ├── geo-output-standard.md
            └── geo-anti-patterns.md
```

## Validation

Run the repository validator before publishing changes:

```bash
python3 scripts/validate_skill.py
```

The validator checks the manifest, Skill frontmatter, required examples, eval files, relative links, naming rules, and common half-finished placeholders.

## Examples

- `examples/01-real-brief.md`: realistic Ganhuo AI request.
- `examples/02-ideal-output.md`: compact target output shape.
- `examples/03-failure-cases.md`: common ways this Skill should refuse or redirect.

## License

MIT

