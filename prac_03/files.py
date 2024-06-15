# 1
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)
# 2
with open('name.txt', 'r') as file:
    name = file.read().strip()
print(f"Hi {name}!")
# 3
with open('numbers.txt', 'r') as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
    result = first_number + second_number
print(result)
# 4
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())
print(total)