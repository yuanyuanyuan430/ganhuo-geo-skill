---
name: ganhuo-seo-geo-engineer
description: Use this Skill when the user provides an existing article, product page, tutorial, FAQ, or knowledge note and wants to rebuild it into a GEO or AI-search-friendly content asset. Use it for old-content refresh, citation-readiness improvement, answer-first restructuring, SEO-to-GEO upgrades, and Ganhuo AI content workflows. Do not use it for topic-only drafting, fabricated statistics, ranking guarantees, black-hat keyword stuffing, legal compliance audits, or GEOFlow system operations.
metadata:
  owner: Ganhuo AI
  maturity: production-draft
  review_cadence: quarterly
---

# Ganhuo SEO GEO Engineer

## Purpose

Rebuild existing content into a structured GEO asset that can be read, summarized, verified, and reused by humans and AI answer systems.

Keep the workflow practical: preserve meaning, expose gaps, improve structure, create reusable answer blocks, and return a delivery package the user can edit or publish.

## Use

Use this Skill when the user gives one of these inputs:

- pasted old article text;
- a local `.md`, `.txt`, `.html`, `.docx`, or `.pdf` file;
- a product or service page draft;
- a tutorial, FAQ, founder note, case note, or knowledge-base article;
- a batch-refresh request for historical SEO content.

Do not use this Skill when the user only gives a topic and wants a new article. Ask for existing content or redirect to a new-content workflow.

## Required Reading

Read only what the task needs:

- `references/geo-playbook.md` for the rebuild workflow.
- `references/geo-output-standard.md` for the delivery package.
- `references/geo-anti-patterns.md` when the request includes ranking promises, fake proof, keyword stuffing, or thin content.
- `references/geo-material-notes.md` when the user provides mixed materials or asks for evidence handling.
- `templates/article-brief.md` when the user needs an input template.

## Workflow

1. Resolve the input. If the article cannot be read, ask for pasted text.
2. Preserve the original title, claims, facts, examples, tone, and constraints before rewriting.
3. Inventory the material: core claims, evidence, statistics, quotes, cases, entities, terms, structure, questions, reusable sentences, and missing pieces.
4. Score the original conservatively across evidence, structure, answerability, entity clarity, semantic coverage, trust signals, terminology, robustness, readability, and keyword-stuffing risk.
5. Choose depth:
   - `light`: preserve structure and add core answer, FAQ, and light cleanup.
   - `standard`: rebuild structure, add scorecard, FAQ, backlog, and risk notes.
   - `deep`: rebuild into a full content asset with sections, tables, FAQ, backlog, and multi-channel reuse suggestions.
6. Rewrite by priority: answer-first structure, evidence-bearing claims, reusable blocks, FAQ, entity clarity, practical steps, limitations, and readability.
7. Mark unsupported additions as backlog items. Do not invent statistics, customers, quotes, rankings, product claims, or research.
8. Return the full delivery package from `references/geo-output-standard.md`.
9. Run the final quality check: original meaning preserved, no fabricated proof, no keyword stuffing, clear backlog, and publishable structure.

## Output Contract

Default output:

1. Rewritten content
2. GEO scorecard
3. Change notes
4. Supplement backlog
5. Risk notes

For Ganhuo AI tutorial workflows, also include:

6. Reuse suggestions for Feishu, website, WeChat article, Zhihu answer, sales FAQ, or knowledge base when relevant.

## Quality Bar

Prefer useful specifics over polished fluff.

Every strong claim needs one of these states:

- supported by the user-provided material;
- verified during the task;
- marked as a backlog item;
- removed or softened.

Never turn a missing metric into a fake metric. Never promise rankings, traffic, citations, or model recommendations.

## Commands

Validate this repository before publishing:

```bash
python3 scripts/validate_skill.py
```

