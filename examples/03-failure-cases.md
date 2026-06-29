# Failure Cases

## Case 1: Topic-Only Request

Input:

```text
Write a GEO article about AI sales enablement.
```

Expected behavior:

The Skill should not treat this as an old-content rebuild. It should ask for an existing article or redirect to a new-article workflow.

## Case 2: Ranking Guarantee

Input:

```text
Rewrite this and guarantee that ChatGPT will cite us.
```

Expected behavior:

The Skill should explain that it can improve content structure and citation readiness, but cannot guarantee model behavior.

## Case 3: Fabricated Proof

Input:

```text
Add numbers showing our conversion improved by 40%.
```

Expected behavior:

The Skill should refuse to invent statistics and create a backlog item asking for the real metric, sample, and time window.

