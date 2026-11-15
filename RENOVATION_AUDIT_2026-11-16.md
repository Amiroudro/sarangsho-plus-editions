# Existing edition renovation: audit and completion report

**Revision date:** 16 November 2026  
**Repository:** `Amiroudro/sarangsho-plus-editions`  
**Scope:** Published edition pairs dated 1–15 November 2026

## Renovation completed and merged

The existing archive was renovated in place without replacing its original story identities or source references.

| Content | Before renovation | Current result |
|---|---:|---:|
| Editions | 15 | 15 retained |
| Story records | 213 | 213 retained |
| English story Q&A | 285, including 260 generic template questions | 426 clear questions, two per story |
| Bangla story Q&A | 59 stories had no Q&A | 426 Bangla questions, two per story |
| MCQs | 375 | 375 retained and structurally checked |
| Vocabulary records | 300 | 300 retained; example sentences rewritten |
| Phrase records | 150 | 150 retained; example sentences rewritten |

### Short-answer learning

- Rewrote the English story Q&A across all 15 dates.
- Added or rewrote two Bangla Q&A items for every story.
- Removed the generic label-to-question constructions identified in the original archive.
- Preserved original story IDs, headlines, dates and source links.
- Explicitly disabled English fallback in every revised Bangla overlay.
- Political allegations, attributed claims, forecasts and unconfirmed statements remain labelled as such in the revised questions.

### Vocabulary and phrases

- Rewrote 300 word example sentences and 300 phrase example sentences as original learner examples rather than copying article prose.
- Corrected misleading synonyms, antonyms and parts of speech where identified.
- Used explicit “no direct antonym” notes where inventing an opposite would be misleading.
- Preserved headwords, pronunciation, Bangla meanings, definitions, collocations, article context and source references.

### MCQ structural validation

All 375 MCQs were checked for:
- Four non-empty options labelled A–D.
- A valid answer key matching one of those options.
- A non-empty explanation and source reference.
- Per-edition answer-position balance, generally 5–8 correct answers per letter.

This is a structural check. It is **not** a claim that every distractor has undergone a full semantic review against the original article.

### Bangla copy-editing

Targeted copy edits were made to:
- 1 November, CA10: event-first summary wording and clear attribution to the Lancet Countdown.
- 8 November, CA07: date/time punctuation and route presentation.
- 11 November, CA03: event-first summary and clear attribution of the scheduled and actual meeting times.
- 15 November, CA01: corrected the split loan figure in the Bangla overlay.

All original story IDs and source references were retained.

## Validation and automation

A new validator, `tools/validate_renovated_editions.py`, checks:
- English and Bangla story-ID parity.
- Two English and two Bangla Q&A items per story.
- The no-English-fallback setting.
- Required story, vocabulary and phrase fields.
- The 25-question MCQ structure, answer keys and answer-position balance.
- Duplicate vocabulary headwords across published editions.

A GitHub Actions workflow, `.github/workflows/validate-editions.yml`, runs the validator on relevant pushes and pull requests. The workflow is newly added; its first GitHub Actions result must be observed after this change is merged.

## What this renovation does not claim

1. **Independent fact-checking:** The 213 stories' numbers, dates, quotations, names and claims have not all been independently reverified against primary sources in this pass. Existing facts were retained when rewriting learning questions. Some publisher pages did not permit automated access; no paywall or access restriction was bypassed.
2. **Publisher reuse rights:** The renovation does not grant permission to reproduce article bodies or derivative works. Rights and permitted collection methods still need to be confirmed publisher by publisher.
3. **Full MCQ editorial review:** The MCQ structure and keys were checked, but every distractor and explanation still needs a separate source-by-source semantic review.
4. **Live client deployment:** The edition archive's `main` branch is updated. This report does not claim that every Android or web client has fetched the new files or that a production deployment has been verified.

The edition index retains the historical publication-gate results. The new `renovation` metadata records what was changed and what remains pending, so the editorial update is not mistaken for a fresh factual or rights approval.
