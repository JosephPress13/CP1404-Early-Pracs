
def bonus_calculator():
    sales = float(input("Enter sales: $"))
    bonus = 0

    while bonus == 0:
        if sales > 999:
            bonus = (sales * 0.15)
            print("Bonus from sale is: $ ", float(bonus))
            sales = float(input("Enter sales: $"))
            bonus = 0
        elif sales >= 0:
            bonus = (sales * 0.1)
            print("Bonus from sale is: $ ", float(bonus))
            sales = float(input("Enter sales: $"))
            bonus = 0
        else:
            print("Value incorrect")
            break


bonus_calculator()