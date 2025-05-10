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

    def type_str(s, spacing=delay):
        nonlocal t
        for c in s:
            timeline.append([round(t, 5), "o", c])
            t += spacing

    def press_tab():
        nonlocal t
        timeline.append([round(t, 5), "o", "\t"])
        t += tab_delay

    def press_enter():
        nonlocal t
        timeline.append([round(t, 5), "o", "\r"])
        t += newline_delay

    cmd = cmd.strip()

    if cmd.startswith("apt install"):
        type_str("apt ins")
        press_tab()
        type_str("tall")
        press_enter()

    elif cmd.startswith("git checkout"):
        type_str("gco")
        press_tab()
        type_str(" checkout main")
        press_enter()

    elif cmd.startswith("docker run"):
        type_str("dock")
        press_tab()
        type_str("er run -it ubuntu bash")
        press_enter()

    elif cmd.startswith("kubectl get pods"):
        type_str("kub")
        press_tab()
        type_str("ectl get po")
        press_tab()
        type_str("ds -A")
        press_enter()

    elif cmd.startswith("kubeadm init"):
        type_str("kube")
        press_tab()
        type_str("adm in")
        press_tab()
        type_str("it --pod-network-cidr=10.244.0.0/16")
        press_enter()

    elif cmd.startswith("grep"):
        type_str("gr")
        press_tab()
        type_str("ep 'main' *.py")
        press_enter()

    else:
        # Generic fallback
        type_str(cmd)
        press_enter()

    return timeline

base_time = 0.1

for e in events:
    if e[1] == "o" and any(cmd in e[2] for cmd in [
        "apt install", "git checkout", "docker run",
        "kubectl get", "kubeadm init", "grep"
    ]):
        simulated = simulate_command(e[2], base_time)
        new_events.extend(simulated)
        base_time = simulated[-1][0] + 0.2
    else:
        new_events.append(e)
        base_time = float(e[0]) + 0.1

# Save updated .cast
with open(output_file, "w") as f:
    f.write(json.dumps(header) + "\n")
    for e in new_events:
        f.write(json.dumps(e) + "\n")

print(f"✔ Guru-style simulation with docker/kubectl/etc saved to: {output_file}")