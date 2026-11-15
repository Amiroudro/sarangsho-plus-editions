#!/usr/bin/env python3
"""Structural validator for the renovated Sarangsho Plus edition archive.

This checks JSON shape, coverage, answer keys, source-link presence, and the
Bangla no-English-fallback contract. It does NOT certify factual accuracy,
publisher reuse rights, translation quality, or editorial approval.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDITION_DIR = ROOT / "editions"
INDEX_PATH = EDITION_DIR / "index.json"

WORD_FIELDS = (
    "Headword / phrase",
    "Bangla phonetic",
    "Part of speech / type",
    "Difficulty",
    "Bangla meaning",
    "English definition",
    "Synonyms",
    "Antonyms",
    "Collocations / patterns",
    "Original example",
    "Direct source URL",
)
PHRASE_FIELDS = (
    "Phrase",
    "Type",
    "Bangla meaning",
    "English explanation",
    "Usage / register",
    "Original example 1",
    "Original example 2",
    "Common collocations / grammar pattern",
    "Direct source URL",
)
STORY_FIELDS = ("id", "headline", "summary", "why_it_matters", "exam_facts", "sources")


def nonempty(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
    return None


def main() -> int:
    errors: list[str] = []
    index = load_json(INDEX_PATH, errors)
    if not index:
        print("\n".join(errors))
        return 1

    entries = index.get("editions", [])
    if not entries:
        errors.append("editions/index.json has no editions")

    totals = Counter()
    seen_dates: set[str] = set()
    seen_words: dict[str, str] = {}

    for entry in entries:
        date = entry.get("edition_date", "")
        if not date:
            errors.append("An index entry has no edition_date")
            continue
        if date in seen_dates:
            errors.append(f"Duplicate edition_date in index: {date}")
        seen_dates.add(date)

        en_path = EDITION_DIR / entry.get("file", f"data-{date}.json")
        bn_path = EDITION_DIR / f"bn-{date}.json"
        en = load_json(en_path, errors)
        bn = load_json(bn_path, errors)
        if en is None or bn is None:
            continue

        stories = en.get("stories", [])
        bn_stories = bn.get("stories", {})
        story_ids = [story.get("id") for story in stories]
        if len(story_ids) != len(set(story_ids)):
            errors.append(f"{date}: duplicate English story IDs")
        if set(story_ids) != set(bn_stories):
            errors.append(f"{date}: English/Bangla story ID sets differ")
        if len(stories) != entry.get("stories"):
            errors.append(f"{date}: index story count does not match data file")

        if bn.get("english_fallback_allowed") is not False:
            errors.append(f"{date}: Bangla overlay does not explicitly disable English fallback")

        for story in stories:
            sid = story.get("id", "<missing-id>")
            for field in STORY_FIELDS:
                if not nonempty(story.get(field)):
                    errors.append(f"{date}/{sid}: missing story field {field}")
            qa = story.get("exam_qa", [])
            if len(qa) != 2:
                errors.append(f"{date}/{sid}: expected 2 English short Q&A, found {len(qa)}")
            for item in qa:
                if not nonempty(item.get("q")) or not nonempty(item.get("a")):
                    errors.append(f"{date}/{sid}: incomplete English Q&A item")
            if not story.get("sources"):
                errors.append(f"{date}/{sid}: no source references")

            bn_story = bn_stories.get(sid, {})
            bn_qa = bn_story.get("exam_qa", [])
            if len(bn_qa) != 2:
                errors.append(f"{date}/{sid}: expected 2 Bangla short Q&A, found {len(bn_qa)}")
            for item in bn_qa:
                if not nonempty(item.get("q")) or not nonempty(item.get("a")):
                    errors.append(f"{date}/{sid}: incomplete Bangla Q&A item")
            for field in ("headline", "summary", "why_it_matters", "exam_facts"):
                if not nonempty(bn_story.get(field)):
                    errors.append(f"{date}/{sid}: missing Bangla field {field}")

        mcqs = en.get("mcqs", [])
        if len(mcqs) != 25:
            errors.append(f"{date}: expected 25 MCQs, found {len(mcqs)}")
        answer_counts = Counter()
        for number, question in enumerate(mcqs, start=1):
            options = question.get("options", {})
            if set(options) != {"A", "B", "C", "D"}:
                errors.append(f"{date}/MCQ {number}: options must be A, B, C, D")
            if question.get("correct") not in options:
                errors.append(f"{date}/MCQ {number}: correct key does not match an option")
            if any(not nonempty(options.get(letter)) for letter in ("A", "B", "C", "D")):
                errors.append(f"{date}/MCQ {number}: an option is empty")
            for field in ("question", "explanation", "source"):
                if not nonempty(question.get(field)):
                    errors.append(f"{date}/MCQ {number}: missing {field}")
            answer_counts[question.get("correct")] += 1
        if mcqs and any(not 5 <= answer_counts[letter] <= 8 for letter in "ABCD"):
            errors.append(f"{date}: MCQ answer positions are outside the 5–8 balance band: {dict(answer_counts)}")

        words = en.get("words", [])
        if len(words) != 20:
            errors.append(f"{date}: expected 20 vocabulary entries, found {len(words)}")
        for word in words:
            headword = str(word.get("Headword / phrase", "")).strip().casefold()
            if not headword:
                errors.append(f"{date}: vocabulary entry has no headword")
            elif headword in seen_words:
                errors.append(f"{date}: duplicate headword {headword!r}; first used in {seen_words[headword]}")
            else:
                seen_words[headword] = date
            for field in WORD_FIELDS:
                if not nonempty(word.get(field)):
                    errors.append(f"{date}/{headword}: missing vocabulary field {field}")

        phrases = en.get("phrases", [])
        if len(phrases) != 10:
            errors.append(f"{date}: expected 10 phrase entries, found {len(phrases)}")
        for phrase in phrases:
            name = str(phrase.get("Phrase", "")).strip()
            for field in PHRASE_FIELDS:
                if not nonempty(phrase.get(field)):
                    errors.append(f"{date}/{name}: missing phrase field {field}")

        totals["editions"] += 1
        totals["stories"] += len(stories)
        totals["english_qa"] += sum(len(story.get("exam_qa", [])) for story in stories)
        totals["bangla_qa"] += sum(len(story.get("exam_qa", [])) for story in bn_stories.values())
        totals["mcqs"] += len(mcqs)
        totals["words"] += len(words)
        totals["phrases"] += len(phrases)

    if errors:
        print(f"FAIL: {len(errors)} validation issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: renovated edition archive is structurally consistent")
    for key in ("editions", "stories", "english_qa", "bangla_qa", "mcqs", "words", "phrases"):
        print(f"{key}: {totals[key]}")
    print("Scope note: structural checks only; factual accuracy, reuse rights, and editorial approval require separate review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
