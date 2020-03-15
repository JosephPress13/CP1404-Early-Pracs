# write
out_file = open("name.txt", "w")
name = str(input("What is your name? "))
print(name, file=out_file)

out_file.close()

# read
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()

print("Your name is {}".format(name))

# numbers
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

# sum of all
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()