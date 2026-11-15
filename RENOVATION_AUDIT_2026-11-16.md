# Existing edition renovation audit

**Audit date:** 16 November 2026  
**Repository:** `Amiroudro/sarangsho-plus-editions`  
**Scope:** All published edition pairs dated 1–15 November 2026  
**Purpose:** Establish the actual repair work required before rewriting or republishing the archive.

## Executive finding

The archive contains substantial existing study content and must be renovated in place through reviewed replacements, not treated as an empty project. This audit inspected all 15 English edition JSON files, all 15 Bangla overlays, and the publication index.

The 15-day archive contains:

- **213 story records** across 15 editions (12–15 stories per day).
- **375 MCQs** (25 per edition).
- **300 vocabulary records** (20 per edition).
- **150 phrase records** (10 per edition).
- **285 story-level short Q&A records** in English.

The archive is not ready for an unconditional quality endorsement. Passing the historical automated publication gate is not the same as a fresh editorial, translation, source-rights or factual review.

## Findings from the structural audit

### 1. Short-answer questions need substantial rewriting

Of the 285 English story-level Q&A records, **260 use the generic “What is …?” construction**. Examples include:

- “What is demanded minimum wage?” → “Tk 30,000”
- “What is factories shut?” → “177”
- “What is + accused?” → “2,300”

These are not acceptable exam questions. They often turn a label or fragment into a question and do not test a clear concept. Rewrite each question from the underlying verified fact, retain the correct answer, and add a concise explanation or source trace where useful. Do not mechanically disguise the same template.

### 2. Bangla learning coverage is incomplete

Across the 213 Bangla story overlays, **59 have an empty `exam_qa` array**. The affected editions include 12 November (all 12 stories) and 13 November (all 13 stories). The Bangla overlay's top-level note explicitly says that missing fields fall back to English text. That behaviour conflicts with the Bangla-first, no-English-fallback editorial requirement.

Repair by supplying reviewed Bangla content for every displayed learning field or by explicitly marking the field as unavailable in Bangla. Never silently substitute English text in Bangla mode.

### 3. MCQ answer-position balance is not the primary problem

Every edition contains 25 MCQs. In each of the 15 editions, the correct-answer letters are distributed across A, B, C and D, generally 5–8 occurrences per letter. This is a useful structural property to preserve.

However, balanced answer letters do not establish that distractors are plausible, options are parallel, the question is unambiguous, or the answer is supported by the cited source. Those checks require item-level review.

### 4. Bangla overlays are structurally present, but need editorial validation

All 15 overlays contain the expected story IDs and core fields (headline, summary, why-it-matters and exam facts). This is a positive structural result, not proof that every translation is accurate or natural.

A specific formatting defect is present in the 15 November overlay: the loan figure in CA01 is split across a line break as `২,` and `৫৪২` in the same sentence. Number grouping, dates, units and proper-name rendering need a dedicated final pass.

### 5. Historical publication-gate status

The archive index records:

| Edition dates | Historical gate recorded in index | Renovation interpretation |
|---|---|---|
| 1–6 Nov | 12/12 checks, backfilled | Retain, but re-audit against the current editorial standard |
| 7 Nov | Proof edition; not formally checked against the Phase 2 12-check list | Review status is weaker than the surrounding editions |
| 8 Nov | 11/12 checks | One recorded check did not pass |
| 9–15 Nov | 17/17 checks | Automated checks passed; editorial defects above still remain |

Do not represent these historical gate results as a fresh 2026-11-16 audit.

## Renovation rules

1. Preserve every original edition file and its Git history. Work on replacement candidates in a separate staging path or branch.
2. Preserve edition dates, story IDs, original headlines, publishers, publication dates and source URLs unless a documented correction is approved.
3. Check every material number, date, name, quote and institutional claim against the linked article and, where possible, an authoritative primary source.
4. Distinguish reported fact, allegation, official statement, analysis and opinion.
5. Rewrite Bangla as natural, self-contained Bangla. Keep source names and unavoidable technical terms accurate; do not leave accidental English fragments or malformed digit grouping.
6. Remove the silent English fallback from Bangla-mode content. A missing Bangla field must be visibly marked as pending or unavailable.
7. Rewrite generic short questions into precise questions that test the actual fact or concept. Do not invent answers or explanations.
8. Review all MCQs for one defensible answer, parallel options, plausible distractors, answer-key correctness and source support. Preserve balanced answer positions without forcing artificial distributions.
9. Review vocabulary for part of speech, Bangla meaning, definition, pronunciation, synonyms, antonyms, collocations and a source-grounded example. Do not add a synonym or antonym merely to fill a field.
10. Recalculate quality gates after editorial review. Do not mark an edition renovated or approved merely because its JSON parses or its automated checks pass.
11. Keep publisher reuse rights separate from public accessibility. Do not fetch paywalled or robots-disallowed body text or imply that RSS availability grants republication rights.
12. Publish replacement editions only after the human editorial gate is satisfied.

## Work status

This file records the first full-archive structural audit. **It does not claim that the 213 stories, 375 MCQs, 300 vocabulary records or 150 phrases have already been rewritten or fact-checked.** No published edition JSON or publication-index entry was changed by this audit.

The next repair pass should work date by date, beginning with the most recent edition and moving backwards, with each date producing a complete English/Bangla replacement pair and a review report. The original published files remain untouched until a replacement passes review.
