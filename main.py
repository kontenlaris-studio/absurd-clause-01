#!/usr/bin/env python3
"""The Absurd Clause Contest — one-line entry for make.fun.

The line is a terms-of-service clause, deadpan legal boilerplate that
quietly turns absurd: a no-sue waiver that binds you, your honor, and
your descendants across all 14 parallel universes — including for
reasons nobody has invented yet. One hyper-specific number (14),
one real mechanism (the waiver of the right to sue) followed into
absurdity, punch in the final clause. 162 characters, cap 200.
"""
import os

LINE = (
    "You agree not to sue us, your honor, or your descendants, in this "
    "or any of the 14 parallel universes, for any reason, including the "
    "ones we haven't invented yet."
)


def main() -> None:
    # The brief caps the clause at 200 characters; fail loudly if it
    # ever drifts past it instead of submitting an invalid entry.
    assert len(LINE) <= 200, f"clause is {len(LINE)} chars, cap is 200"
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
