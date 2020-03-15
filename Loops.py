for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n = int(input("How many stars would you like? "))
for i in range(0, n):
    for i in range(0, i):
        print("*", end=" ")
    print("*")
print()