
child_meal = float(input(f"What is the price of a child's meal?\n$ "))
adult_meal = float(input(f"What is the price of an adult's meal?\n$ "))
children = int(input(f"How many children are there?\n"))
adults = int(input(f"How many adults are there?\n"))
tax_rate = float(input(f"What is the sales tax rate?\n"))

subtotal = (child_meal * children) + (adult_meal * adults)
print("Subtotal: $ " + str(subtotal))

tip_porcentage = (subtotal / 10)
print(f"Tip porcentage: $ {tip_porcentage:.2f}")

sales_tax = ((subtotal * tax_rate) / 100)
print(f"Sales Tax: $ {sales_tax:.2f}")

total = (subtotal + sales_tax + tip_porcentage)
print(f"Total: $ {total:.2f}")

payment = float(input(f"What is the payment amount?\n$ "))

change = (payment - total)
print(f"Change: $ {change:.2f}")