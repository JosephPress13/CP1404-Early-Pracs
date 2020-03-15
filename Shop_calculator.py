number = int(input("Number of items: "))
cost = 0
total = 0
final = 0

while number <= 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))

for n in range(number):
    price = float(input("Cost of item: $"))
    total += price

if total > 99:
    final = total * 0.9
    print("Total price for {} items is: $ {}".format(number, final))

else:
    final = total
    print("Total price for {} items is: $ {}".format(number, final))
