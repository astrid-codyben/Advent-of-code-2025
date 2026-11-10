# Advent of Code 2025 - Day 1
# Part 1: Secret Entrance

from pathlib import Path

# Read the input file located in the same directory as this script
input_file = Path(__file__).parent / "inputs" / "day1-input.txt"

with open(input_file, "r") as file:
    rotations = file.readlines()

# Initial position of the dial
position = 50

# Number of times the dial points at 0 after a rotation
password = 0

# Process each rotation
for rotation in rotations:
    rotation = rotation.strip()

    if not rotation:
        continue

    direction = rotation[0]
    distance = int(rotation[1:])

    if direction == "R":
        position = (position + distance) % 100
    elif direction == "L":
        position = (position - distance) % 100

    # Count every time the dial ends a rotation at 0
    if position == 0:
        password += 1

# Display the result
print(f"The password is: {password}")