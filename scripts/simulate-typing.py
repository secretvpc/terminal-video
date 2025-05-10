#!/usr/bin/env python3
# simulate-typing.py – Convert pasted text in .cast to per-char simulated typing

import sys
import json

if len(sys.argv) < 3:
    print("Usage: ./simulate-typing.py input.cast output.cast")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Load cast file
with open(input_file, "r") as f:
    lines = f.readlines()

header = json.loads(lines[0])
events = [json.loads(line) for line in lines[1:]]

new_events = []
delay_increment = 0.05  # 50ms per char

for event in events:
    if event[1] == "o" and len(event[2]) > 1:
        # Simulate typing: split string into chars
        base_time = float(event[0])
        for i, char in enumerate(event[2]):
            timestamp = round(base_time + i * delay_increment, 5)
            new_events.append([timestamp, "o", char])
    else:
        new_events.append(event)

# Write new cast file
with open(output_file, "w") as f:
    f.write(json.dumps(header) + "\n")
    for e in new_events:
        f.write(json.dumps(e) + "\n")

print(f"✔ Simulated typing saved to: {output_file}")