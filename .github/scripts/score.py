"""Count tasks passed from pytest's JUnit XML. A task passes only if all its checks pass.

Prints GitHub Actions outputs (passed=N, total=N) and a job summary table.
"""
import os
import re
import sys
import xml.etree.ElementTree as ET

TOTAL = 4
tasks = {n: True for n in range(1, TOTAL + 1)}
for case in ET.parse(sys.argv[1]).getroot().iter("testcase"):
    m = re.match(r"test_task(\d+)_", case.get("name", ""))
    if m and any(child.tag in ("failure", "error", "skipped") for child in case):
        tasks[int(m.group(1))] = False
passed = sum(tasks.values())
print(f"passed={passed}")
print(f"total={TOTAL}")

summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary, "a") as f:
        f.write(f"## Python Readiness Test: {passed}/{TOTAL} tasks passed\n\n")
        f.write("| Task | Result |\n|---|---|\n")
        for n, ok in tasks.items():
            f.write(f"| {n} | {'pass' if ok else 'not yet'} |\n")
