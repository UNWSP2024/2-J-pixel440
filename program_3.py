def calculate_total_purchase():
item_1 = float(input("Enter the price of item 1:"))
item_2 = float(input("Enter the price of item 2:"))
item_3 = float(input("Enter the price of item 3:"))
item_4 = float(input("Enter the price of item 4:"))
item_5 = float(input("Enter the price of item 5:"))

sales_tax_rate=0.07
subtotal_of_sale = item_1 + item_2 + item_3 + item_4 + item_5
sales_tax = subtotal_of_sale * sales_tax_rate
total = subtotal_of_sale + sales_tax


print(f"Subtotal: ${subtotal_of_sale:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")


calculate_total_purchase()
