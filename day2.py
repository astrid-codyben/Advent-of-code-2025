
# Advent of Code 2025 - Day 2
# Gift Shop

from pathlib import Path

# Read input
input_file = Path(__file__).parent / "inputs" / "day2-input.txt"

with open(input_file, "r") as file:
    puzzle_input = file.read().strip()

# Parse ID ranges
ranges = []

for item in puzzle_input.replace("\n", "").split(","):
    if not item:
        continue

    start, end = map(int, item.split("-"))
    ranges.append((start, end))


def find_invalid_ids(start, end, part):
    """Find invalid IDs according to the puzzle rules."""

    invalid_ids = set()
    max_length = len(str(end))

    for pattern_length in range(1, max_length // 2 + 1):

        for total_length in range(
            2 * pattern_length,
            max_length + 1,
            pattern_length
        ):

            repetitions = total_length // pattern_length

            # Part 1: exactly 2 repetitions
            if part == 1 and repetitions != 2:
                continue

            # Build the repeated pattern multiplier
            factor = sum(
                10 ** (pattern_length * i)
                for i in range(repetitions)
            )

            min_prefix = max(
                10 ** (pattern_length - 1),
                (start + factor - 1) // factor
            )

            max_prefix = min(
                10 ** pattern_length - 1,
                end // factor
            )

            for prefix in range(min_prefix, max_prefix + 1):
                invalid_ids.add(prefix * factor)

    return invalid_ids


def solve(part):
    """Calculate the sum of invalid IDs for a given part."""

    all_invalid_ids = set()

    for start, end in ranges:
        all_invalid_ids.update(
            find_invalid_ids(start, end, part)
        )

    return all_invalid_ids, sum(all_invalid_ids)


# Solve both parts
for part in (1, 2):

    invalid_ids, total = solve(part)

    print(f"\n--- Part {part} ---")
    print(f"Number of invalid IDs: {len(invalid_ids)}")
    print(f"Sum of invalid IDs: {total}")
