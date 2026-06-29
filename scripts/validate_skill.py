#!/usr/bin/env python3
"""Validate the ganhuo-seo-geo-skill repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PRIMARY_SKILL = "ganhuo-seo-geo-engineer"
SKILL_ROOT = ROOT / "skills" / PRIMARY_SKILL

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "manifest.json",
    SKILL_ROOT / "SKILL.md",
    SKILL_ROOT / "manifest.json",
    SKILL_ROOT / "templates" / "article-brief.md",
    SKILL_ROOT / "evals" / "trigger_cases.json",
    SKILL_ROOT / "evals" / "expected_artifacts.json",
]

REQUIRED_REFERENCES = [
    SKILL_ROOT / "references" / "geo-material-notes.md",
    SKILL_ROOT / "references" / "geo-playbook.md",
    SKILL_ROOT / "references" / "geo-output-standard.md",
    SKILL_ROOT / "references" / "geo-anti-patterns.md",
]

REQUIRED_EXAMPLES = [
    ROOT / "examples" / "01-real-brief.md",
    ROOT / "examples" / "02-ideal-output.md",
    ROOT / "examples" / "03-failure-cases.md",
]

PLACEHOLDER_PATTERNS = [
    "TODO",
    "TBD",
    "lorem ipsum",
    "PLACEHOLDER",
    "your skill name",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not UTF-8: {exc}")


def load_json(path: Path) -> dict:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is invalid JSON: {exc}")


def validate_required_files() -> None:
    missing = [
        str(path.relative_to(ROOT))
        for path in REQUIRED_FILES + REQUIRED_REFERENCES + REQUIRED_EXAMPLES
        if not path.exists()
    ]
    if missing:
        fail("Missing required files: " + ", ".join(missing))


def validate_manifest() -> None:
    manifest = load_json(ROOT / "manifest.json")
    if manifest.get("repo_name") != "ganhuo-seo-geo-skill":
        fail("manifest.repo_name must be ganhuo-seo-geo-skill")
    if manifest.get("primary_skill") != PRIMARY_SKILL:
        fail(f"manifest.primary_skill must be {PRIMARY_SKILL}")

    skills = manifest.get("skills")
    if not isinstance(skills, list) or len(skills) != 1:
        fail("manifest.skills must contain exactly one skill")

    skill = skills[0]
    if skill.get("name") != PRIMARY_SKILL:
        fail(f"manifest skill name must be {PRIMARY_SKILL}")
    if not skill["name"].startswith("ganhuo-seo-"):
        fail("skill name must start with ganhuo-seo-")
    if skill.get("path") != f"skills/{PRIMARY_SKILL}/SKILL.md":
        fail("manifest skill path is incorrect")


def parse_frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    frontmatter: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or ":" not in line or line.startswith("metadata:"):
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter


def validate_skill_frontmatter() -> None:
    skill_text = read_text(SKILL_ROOT / "SKILL.md")
    frontmatter = parse_frontmatter(skill_text)
    if frontmatter.get("name") != PRIMARY_SKILL:
        fail(f"SKILL.md frontmatter name must be {PRIMARY_SKILL}")

    description = frontmatter.get("description", "")
    if len(description) < 120:
        fail("SKILL.md description is too short to route reliably")
    for phrase in ["existing article", "GEO", "Do not use"]:
        if phrase not in description:
            fail(f"SKILL.md description must mention: {phrase}")


def validate_links_and_references() -> None:
    skill_text = read_text(SKILL_ROOT / "SKILL.md")
    for ref in REQUIRED_REFERENCES:
        rel = ref.relative_to(SKILL_ROOT).as_posix()
        if rel not in skill_text:
            fail(f"SKILL.md does not reference {rel}")

    for match in re.finditer(r"\(([^)]+\.md)\)", skill_text):
        rel_path = match.group(1)
        target = (SKILL_ROOT / rel_path).resolve()
        if not target.exists():
            fail(f"SKILL.md has broken Markdown link: {rel_path}")


def validate_json_files() -> None:
    for path in [
        ROOT / "manifest.json",
        SKILL_ROOT / "manifest.json",
        SKILL_ROOT / "evals" / "trigger_cases.json",
        SKILL_ROOT / "evals" / "expected_artifacts.json",
    ]:
        load_json(path)


def validate_non_empty_examples() -> None:
    for path in REQUIRED_EXAMPLES:
        if len(read_text(path).strip()) < 80:
            fail(f"{path.relative_to(ROOT)} is too thin")


def validate_no_outputs_or_placeholders() -> None:
    if (ROOT / "outputs").exists():
        fail("outputs/ must not be committed")

    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.relative_to(ROOT).as_posix() == "scripts/validate_skill.py":
            continue
        text = read_text(path)
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern in text:
                fail(f"{path.relative_to(ROOT)} contains placeholder marker: {pattern}")


def validate_readme_alignment() -> None:
    readme = read_text(ROOT / "README.md")
    if PRIMARY_SKILL not in readme:
        fail("README.md must mention the primary skill")
    if "python3 scripts/validate_skill.py" not in readme:
        fail("README.md must include the validation command")


def main() -> None:
    validate_required_files()
    validate_manifest()
    validate_skill_frontmatter()
    validate_links_and_references()
    validate_json_files()
    validate_non_empty_examples()
    validate_no_outputs_or_placeholders()
    validate_readme_alignment()
    print("ganhuo-seo-geo-skill validation passed.")


if __name__ == "__main__":
    main()
