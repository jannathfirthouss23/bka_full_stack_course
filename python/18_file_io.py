"""
# FILE MODES
#   "r"  read (default), fails if file is missing
#   "w"  write, overwrites existing file
#   "a"  append, creates if missing
#   "x"  create only, fails if file exists
#   "b"  binary mode (e.g. "rb", "wb")
"""

# WRITING

with open("helpers/notes.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("This is line 2.\n")

# READING (whole file)

with open("helpers/notes.txt", "r") as f:
    content = f.read()

print(content)

# READING LINE BY LINE

with open("helpers/notes.txt", "r") as f:
    for line in f:
        print(line.rstrip())

# APPENDING

with open("helpers/notes.txt", "a") as f:
    f.write("appended line.\n")

with open("helpers/notes.txt", "r") as f:
    print(f.read())

# JSON

import json

data = {"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}

with open("helpers/person.json", "w") as f:
    json.dump(data, f, indent=2)

with open("helpers/person.json", "r") as f:
    loaded = json.load(f)

print(loaded)
print(loaded["name"])

# CSV

import csv

rows = [
    ["name", "age", "city"],
    ["Alice", 30, "Boston"],
    ["Bob", 25, "NYC"],
]

with open("helpers/people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open("helpers/people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# PATH LIB (path handling)

from pathlib import Path

p = Path("helpers/notes.txt")
print(p.exists())
print(p.name)
print(p.suffix)
print(p.stat().st_size, "bytes")

# CLEANUP

for name in ["helpers/notes.txt", "helpers/person.json", "helpers/people.csv"]:
    Path(name).unlink(missing_ok=True)
