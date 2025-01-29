with open("andengintro.txt", "r") as file:
    for line in file:
        print(line.strip())

print(f"\nTotal lines: {len(line)}")
print(f"Total words: {sum(len(line.split()) for line in line)}")
print(f"Total characters: {sum(len(line) for line in line)}")

