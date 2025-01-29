with open("output.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
#write_file.py
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")

with open("output.txt", "a") as file:
    file.write("This is appended text.\n")
#write_numbers
with open("output.txt", "w") as file:
    for number in range(1, 11):
        file.write(f"{number}\n")
    print("Numbers written successfuly.")
