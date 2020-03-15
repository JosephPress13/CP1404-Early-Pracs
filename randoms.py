import random
print(random.randint(5, 20))  # line 1
# smallest number is 5, largest is 20
print(random.randrange(3, 10, 2))  # line 2
# smallest number is 3, largest is 9
# cannot produce 4, increasing from 3 in increments of 2
print(random.uniform(2.5, 5.5))  # line 3
# smallest 2.5, largest 5.5
print(random.randint(0,101)) # line 4