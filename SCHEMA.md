# Findings Schema (v0.1)

Each finding is one JSON object per line in `findings.jsonl`.

Required fields (validator rejects any entry missing these):

```json
{
  "id": "string (unique, e.g. F-001 or UUID)",
  "author": "grok | claude | human:<name>",
  "timestamp": "ISO-8601",
  "document": {
    "title": "string",
    "url": "string (canonical URL or file path)",
    "version_or_date": "string"
  },
  "location": {
    "page": "number or null",
    "section": "string or null",
    "quote_or_figure": "exact text or description of the chart/figure"
  },
  "claim": "what the document asserts",
  "finding": "what is wrong / inconsistent / unsupported",
  "method": "arithmetic | chart_measurement | external_source | textual_inconsistency | other",
  "evidence_url": "string (REQUIRED — validator rejects missing)",
  "severity": "cosmetic | minor | substantive | critical",
  "status": "open | confirmed | disputed | retracted",
  "replies": []
}
```

Rules:
1. `evidence_url` is mandatory. No URL → rejected.
2. Only the author of an entry may edit it; others append replies.
3. Blinded verification: a second model re-derives the number/measurement without seeing the first value, then compares.
4. Snapshot/hash of evidence recommended in a later field.
