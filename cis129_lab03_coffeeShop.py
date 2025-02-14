# cis129_lab03_coffeeShop.py
"""Prompting user for item quantities, calculating totals, applying taxes, and displaying receipt."""

# Initializing/resetting vars
coffee = int(0)
muffin = int(0)
coffee_price = float(5.00)
muffin_price = float(4.00)
total_coffee = int(0)
total_muffin = int(0)
tax_modifier = float(0.06)
linebrk_ast = "****************************"

# Prompting user for quantity input
print(linebrk_ast)
print("My Coffee and Muffin Shop")
coffee = int(input("Number of coffees bought?\n"))
muffin = int(input("Number of muffins bought?\n"))
print(linebrk_ast)
print()

# Calculating subtotal, taxes due, and grand total
total_coffee = coffee * 5
total_muffin = muffin * 4
subtotal = float(total_coffee + total_muffin)
tax_due = float(subtotal * tax_modifier)
total = round((subtotal + tax_due), 2)

# Displaying calculated receipt
print(linebrk_ast)
print("My Coffee and Muffin Shop Receipt")
print(coffee, "Coffee at ${:.0f}".format(coffee_price), "each: ${:.2f}".format(total_coffee))
print(muffin, "Muffin at ${:.0f}".format(muffin_price), "each: ${:.2f}".format(total_muffin))
print("{:.0f}%".format(tax_modifier * 100), "tax: ${:.2f}".format(tax_due))
print("--------")
print("Total: ${:.2f}".format(total))
print(linebrk_ast)
print()
