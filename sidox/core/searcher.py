from pathlib import Path
import sys

q = " ".join(sys.argv[1:]).lower()

matches = []

for p in Path("app/src/main/java").rglob("*.kt"):
    text = p.read_text(errors="ignore").lower()
    if q in str(p).lower() or q in text:
        matches.append(str(p))

print("Sidox search results:")
for m in matches:
    print("-", m)

print("Found:", len(matches))
