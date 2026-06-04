# Contribution Guide

Every update should make the repository more useful to a curious reader.

## Entry Contract

A daily entry must:

1. State one precise, falsifiable claim.
2. Include a deterministic Python experiment that uses only the standard
   library.
3. Explain the observation without overstating what the experiment proves.
4. Cite at least one primary or official source.
5. Avoid duplicating an existing entry.
6. Pass `python scripts/verify.py`.
7. Update the table in `README.md` and the checkbox in `TOPICS.md`.

## File Names

Use the current local date and a short topic slug:

```text
entries/YYYY/YYYY-MM-DD-topic-slug.md
experiments/YYYY/YYYY-MM-DD-topic_slug.py
```

## Publishing Rules

- Publish at most one entry per day.
- Do not create empty commits or change commit dates.
- Do not fabricate sources, output, or conclusions.
- Do not add secrets, personal data, generated caches, or external
  dependencies.
- If the quality bar cannot be met, skip the update.
