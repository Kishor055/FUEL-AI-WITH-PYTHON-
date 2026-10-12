with open("notes.txt") as f:
    for line in f:
        print(line.strip())

with open("notes.txt") as f:
    lines = f.readlines()

print(len(lines))
