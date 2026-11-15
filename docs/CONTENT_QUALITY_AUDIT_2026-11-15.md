# Sarangsho Plus content-quality audit
**Audit date:** 15 November 2026  
**Scope:** Uploaded Android APK plus the public edition feed at `Amiroudro/sarangsho-plus-editions`. This is a structural and sample-source audit, not a full independent fact-check of every claim.

## 1. What was inspected

- The uploaded APK is a Flutter Android package, namespace `com.sarangsho.plus`.
- It bundles English edition JSON and Bengali overlays for 1–13 November 2026.
- The app's configured update feed is `https://amiroudro.github.io/sarangsho-plus-editions/editions/index.json`.
- The public feed index lists published editions through 15 November 2026. The two newest dates are therefore available from the feed but are not bundled in this APK.
- The public feed README says the app downloads editions newer than its bundled editions.

## 2. Edition inventory

The APK contains 13 editions:
- 186 story records in total.
- 260 vocabulary records, 130 phrases, 325 MCQs and 65 revision words.
- Every bundled English story has a matching Bengali story overlay. The overlays contain Bengali headlines, summaries, facts, relevance explanations, recall cards and other story fields.
- The live feed index currently lists 15 editions and 213 story records. Edition story counts range from 12 to 15; the smaller editions are explicitly described in the index as not padded.

The app and feed are therefore not empty. The APK is a bundled snapshot; the public feed is the update source.

## 3. Findings requiring correction or review

### A. Source concentration
Across the 15 feed editions, the source fields contain 284 references. The Daily Star appears 105 times, Prothom Alo English 80 times, and The Business Standard 54 times. Together these three account for 239/284 references (84.2%). This is a source-reference count, not a count of unique stories or unique outlets. The remaining references include other newspapers, news agencies and institutional sources.

**Risk:** The feed is useful but does not yet demonstrate broad, balanced coverage of Bangladesh's newspaper ecosystem. A wider source pool should be actively monitored, with source diversity measured by edition and topic.

### B. Malformed exam questions
A scan of the 13 APK-bundled editions found at least 13 awkwardly generated English `exam_qa` prompts, including:
- “What is demanded minimum wage?”
- “What is factories shut?”
- “What is zero-pass institutions?”

**Risk:** These are unsuitable as exam practice in their current form. Generate questions from typed fact labels and validate grammar, answerability and factual grounding before publication.

### C. Incomplete key-fact labels
The APK's 186 stories contain 702 `key_facts` entries. Of these, 130 have an empty `label` field (18.5%). Examples include values such as “project 1 July 2026-30 June 2031” and “UNGA granted a three-year preparatory period” without a named fact label.

**Risk:** Unlabelled facts are harder to scan, search, translate and convert into reliable questions. Require a non-empty, meaningful label and a concise value; do not silently treat a date or explanatory sentence as a label.

### D. Duplicate headline across editions
The feed contains the same headline, “Bangladesh Bank orders minimum cash margins on 10 Ramadan imports”, in both 9 and 10 November editions (CA06 and CA10).

**Risk:** This may be a legitimate follow-up or an accidental repeat. Compare source URLs, article dates and substantive changes. If it is the same story without a material update, link it to the earlier event and avoid presenting it as a new story.

### E. Bengali overlay field parity
The Bengali overlay covers every bundled story, but its story schema does not include the English `exam_relevance` field. The overlay has `why_it_matters` and `exam_facts`, which provide related material, but the field-level schemas are not identical.

**Risk:** Depending on the app renderer, the missing localized field may cause an English fallback or inconsistent display. Decide whether to add a Bengali `exam_relevance` field or deliberately map the English value to the Bengali equivalent.

### F. Editorial classification and balance
Across the 15 feed editions, categories are: Economy & Banking 87; Bangladesh 39; World 24; Jobs & Education 23; Politics 22; Editorial & Opinion 13; Technology 5.

**Risk:** Economy and banking appropriately receive strong emphasis for bank examinations, but technology/science coverage is very thin. Topic quotas should be based on the day's actual news, not forced padding; the index already records that some days were published with fewer than 15 stories.

### G. Review-policy wording is inconsistent
The public README says editions are “Human-reviewed before publish”. The index says that, from 13 November, editions passing the automated 17/17 checks and a longest-correct-answer threshold auto-publish under the owner's rule.

**Risk:** These statements can be read as contradictory. Document the actual gate precisely: which checks are automated, which checks require a human, and which editions were auto-published. Passing a structural checklist is not independent confirmation of factual accuracy.

### H. Publication cadence
The index describes the daily engine as running at 08:00 Asia/Dhaka. This repository evidence does not establish a second 18:00 run.

## 4. Sample source verification

A search-indexed copy of The Business Standard's 15 November article, “Bangladesh seeks new debt strategy amid rising repayment pressure”, matches the feed's headline and describes the Cox's Bazar debt conference, public-debt pressure, financing options and debt-management reforms. This is a positive sample match, not a verification of every statistic in the edition.

The TBS article on Islami Bank's proposed Tk6,000 crore government investment and possible 78.8% state ownership is also discoverable under the exact headline and date recorded in the 15 November edition. Its article text attributes the proposal to the bank and describes the central bank's letter and the former governor's opposition. The summary must preserve that distinction between a proposal, official correspondence and an approved government investment.

Direct page fetching of several publisher URLs was blocked (HTTP 403) in this audit environment. A blocked fetch is not evidence that a URL is broken. Links requiring further checking should be retried through publisher RSS, search indexing or a browser.

## 5. Recommended remediation order

1. Fix the question generator: reject ungrammatical stems, empty prompts, answer leakage and questions whose answer is not a specific fact.
2. Enforce `key_facts` schema validation: non-empty label, concise value, source trace and date/unit validation.
3. Resolve the 9–10 November duplicate by comparing the underlying article URLs and content; preserve both editions' history.
4. Define Bengali/English field parity and prevent accidental English fallback for localized exam fields.
5. Expand source monitoring and publish a per-edition source-diversity report. Prioritize national Bangla dailies, regional papers, business press, news agencies and authoritative primary sources.
6. Separate automated structural checks from human editorial review and factual verification in the README and index metadata.
7. Add an 18:00 run only if it is intentionally configured and monitored; the current index documents only the 08:00 run.

## 6. What this audit does not claim

- It does not claim that all 213 feed stories have been independently fact-checked.
- It does not claim that every publisher URL is live; some direct requests were blocked by publisher access controls.
- It does not claim that the 17/17 automated checks validate the truth of every statistic or the quality of every translation.
- It does not modify or delete any published edition.

**Principle:** Preserve the existing editions. Correct confirmed errors through traceable, versioned changes, and never overwrite a published fact without retaining its source and correction history.
