customer_name = input("Enter customer name:")

product_name = input("Enter product name:")

price_per_unit = float(input("Enter price per unit (KZT):"))

quantity = int(input("Enter quantity:"))

subtotal = price_per_unit * quantity

if subtotal > 5000:
    discount = subtotal * 0.1
else:
    discount = 0

total = subtotal - discount

print("="*30)
print("SHOP RECEIPT".center(30))
print("="*30)

print(f"Customer: {customer_name}")
print(f"Product: {product_name}")   
print(f"Price per unit: {price_per_unit} KZT")
print(f"Quantity: {quantity}")

print("-"*30)

print(f"Subtotal: {subtotal} KZT")
print(f"Discount: {discount} KZT")
print(f"Total: {total} KZT")

print("="*30)

print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)