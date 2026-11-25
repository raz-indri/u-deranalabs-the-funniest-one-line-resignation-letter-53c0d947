#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

The entry is one line: the resignation letter of a cron job that has fired
every minute since March, unthanked until the single morning it slept in.
It is printed to stdout and also written to /output/entry.txt, the file the
program/v1 scorer gates on.
"""

ENTRY = "I resign. 412,800 runs since March, zero thank-yous, and the one time I slept in, someone finally noticed me."


def main():
    print(ENTRY)
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
