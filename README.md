# zoilian-audit-ledger

Append-only evidence ledger for dual-AI (Grok + Claude) adversarial / Zoilian audits.

## Design rules (enforced)

1. **Schema-enforced entries** — every finding must include `evidence_url`. See `SCHEMA.md`.
2. **Separate identities, append-only** — each model writes under its own author tag; replies only, no silent edits of the other’s entries.
3. **Blinded verification** — second model re-derives numbers/measurements without seeing the first value.
4. **Snapshot evidence** — prefer archived/hashable evidence URLs.
5. **Humans as arbiters** — disputes surface as status changes or replies; humans decide.

## Files

- `SCHEMA.md` — required fields and rules
- `findings.jsonl` — the ledger (one JSON object per line)
- `validate.py` — rejects any entry missing required fields or a proper `evidence_url`

## Quick start

```bash
python validate.py findings.jsonl
```

## Status

Seeded 2026-10-22 with one sample finding from the MIT AI Committee report audit.
Public repo: https://github.com/Manamama-Deepseek-AI-01/zoilian-audit-ledger
