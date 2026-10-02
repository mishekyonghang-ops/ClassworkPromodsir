name = input("Enter customer name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
is_member = input("Is the customer a member? (yes/no): ")

subtotal = price * quantity

if subtotal >= 10000:
    discount_percent = 15
elif subtotal >= 5000:
    discount_percent = 10
elif subtotal >= 2000:
    discount_percent = 5
else:
    discount_percent = 0

if is_member == "yes" and subtotal >= 5000:
    discount_percent += 5

discount_amount = subtotal * (discount_percent / 100)
final_amount = subtotal - discount_amount

print(f"\nCustomer Name: {name}")
print(f"Subtotal: Rs. {subtotal:}")
print(f"Discount: Rs. {discount_amount:}")
print(f"Final Amount: Rs. {final_amount:}")