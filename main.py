#!/usr/bin/env python3
"""Write the GPS's one-line excuse to /output/entry.txt.

Stdlib only, deterministic, no network. OUTPUT_DIR overrides the
output directory for local testing (same code path as production).
"""
import os

LINE = "I didn't get you lost, I got you invited: the map called this cul-de-sac a shortcut, and the bride just thanked me for bringing you to her wedding."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
