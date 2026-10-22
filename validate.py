#!/usr/bin/env python3
"""Minimal validator for zoilian-audit-ledger findings.jsonl
Rejects any line that is not valid JSON or is missing required fields,
especially evidence_url (Design Rule 1).
"""

import json
import sys
from pathlib import Path

REQUIRED = ["id", "author", "timestamp", "document", "location", "claim", "finding", "method", "evidence_url", "severity", "status"]

def validate_line(line: str, lineno: int) -> list[str]:
    errors = []
    try:
        obj = json.loads(line)
    except json.JSONDecodeError as e:
        return [f"line {lineno}: invalid JSON — {e}"]

    for key in REQUIRED:
        if key not in obj or obj[key] in (None, ""):
            errors.append(f"line {lineno}: missing or empty required field '{key}'")

    if "evidence_url" in obj and not str(obj["evidence_url"]).startswith(("http://", "https://", "file:")):
        errors.append(f"line {lineno}: evidence_url must be a URL (got {obj.get('evidence_url')!r})")

    return errors

def main(path: str = "findings.jsonl") -> int:
    p = Path(path)
    if not p.exists():
        print(f"ERROR: {path} not found", file=sys.stderr)
        return 1

    all_errors = []
    with p.open() as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            all_errors.extend(validate_line(line, i))

    if all_errors:
        for e in all_errors:
            print(e, file=sys.stderr)
        print(f"\n{len(all_errors)} error(s) — REJECT", file=sys.stderr)
        return 1

    print("OK — all entries pass schema")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "findings.jsonl"))
