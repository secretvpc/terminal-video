#!/usr/bin/env python3
# simulate-guru.py – Simulate Linux guru behavior in asciinema .cast file

import sys
import json

if len(sys.argv) < 3:
    print("Usage: ./simulate-guru.py input.cast output.cast")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Load .cast content
with open(input_file, "r") as f:
    lines = f.readlines()

header = json.loads(lines[0])
events = [json.loads(line) for line in lines[1:]]

new_events = []
delay = 0.05  # base delay per character
tab_delay = 0.1
newline_delay = 0.2

def simulate_command(cmd, base_time):
    timeline = []
    t = base_time

    if cmd.startswith("apt install"):
        # Simulate typing "apt ins" + TAB + "tall"
        for c in "apt ins":
            timeline.append([round(t, 5), "o", c])
            t += delay
        timeline.append([round(t, 5), "o", "\t"])
        t += tab_delay
        for c in "tall":
            timeline.append([round(t, 5), "o", c])
            t += delay
        timeline.append([round(t, 5), "o", "\r"])
        t += newline_delay
    elif cmd.startswith("git checkout"):
        # Simulate alias: gco + expansion + Enter
        for c in "gco":
            timeline.append([round(t, 5), "o", c])
            t += delay
        timeline.append([round(t, 5), "o", "\t"])
        t += tab_delay
        for c in " checkout main":
            timeline.append([round(t, 5), "o", c])
            t += delay
        timeline.append([round(t, 5), "o", "\r"])
        t += newline_delay
    else:
        # Generic typing
        for c in cmd:
            timeline.append([round(t, 5), "o", c])
            t += delay
        timeline.append([round(t, 5), "o", "\r"])
        t += newline_delay

    return timeline

base_time = 0.1

for e in events:
    if e[1] == "o" and any(cmd in e[2] for cmd in ["apt install", "git checkout"]):
        simulated = simulate_command(e[2].strip(), base_time)
        new_events.extend(simulated)
        base_time = simulated[-1][0] + 0.2
    else:
        new_events.append(e)
        base_time = float(e[0]) + 0.1

# Save new .cast
with open(output_file, "w") as f:
    f.write(json.dumps(header) + "\n")
    for e in new_events:
        f.write(json.dumps(e) + "\n")

print(f"✔ Guru-style simulation saved to: {output_file}")