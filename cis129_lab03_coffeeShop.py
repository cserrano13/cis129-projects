# cis129_lab03_coffeeShop.py
"""Prompting user for item quantities, calculating totals, applying taxes, and displaying receipt."""

# Initializing/resetting vars
coffee = int(0)
muffin = int(0)
tea = int(0)
apple = int(0)
coffee_price = float(5.00)
muffin_price = float(4.00)
tea_price = float(3.00)
apple_price = float(0.50)
total_coffee = int(0)
total_muffin = int(0)
total_tea = int(0)
total_apple = int(0)
tax_modifier = float(0.06)
linebrk_ast = "****************************"

# Prompting user for quantity input
print(linebrk_ast)
print("My Cafe")
coffee = int(input("Number of coffees bought?\n"))
muffin = int(input("Number of muffins bought?\n"))
tea = int(input("Number of teas bought?\n"))
apple = int(input("Number of apples bought?\n"))
print(linebrk_ast)
print()

# Calculating subtotal, taxes due, and grand total
total_coffee = coffee * coffee_price
total_muffin = muffin * muffin_price
total_tea = tea * tea_price
total_apple = apple * apple_price
subtotal = float(total_coffee + total_muffin + total_tea + total_apple)
tax_due = float(subtotal * tax_modifier)
total = round((subtotal + tax_due), 2)

# Displaying calculated receipt
print(linebrk_ast)
print("My Cafe")
print(coffee, "Coffee at ${:.2f}".format(coffee_price), "each: ${:.2f}".format(total_coffee))
print(muffin, "Muffin at ${:.2f}".format(muffin_price), "each: ${:.2f}".format(total_muffin))
print(tea, "Tea at ${:.2f}".format(tea_price), "each: ${:.2f}".format(total_tea))
print(apple, "Apple at ${:.2f}".format(apple_price), "each: ${:.2f}".format(total_apple))
print("{:.2f}%".format(tax_modifier * 100), "tax: ${:.2f}".format(tax_due))
print("------------")
print("Total: ${:.2f}".format(total))
print(linebrk_ast)
print()
