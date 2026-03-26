customer_name = input("Enter customer name: ")

subtotal = 0
count = 0

#A1
while True:
    product_name = input("Enter product name (or 'done' to finish): ")
    
    if product_name.lower() == "done":
        break
    
    price = float(input("Enter price: "))
    
    subtotal += price
    count += 1

print("="*30)
print("SHOP RECEIPT".center(30))
print("="*30)

print(f"Customer : {customer_name.upper()}")
print(f"Items : {count}")
print(f"Subtotal : {subtotal} KZT")

#A2
if subtotal < 3000:
    discount_rate = 0
    tier = "No discount"
elif subtotal < 7000:
    discount_rate = 0.05
    tier = "5% discount"
else:
    discount_rate = 0.15
    tier = "15% discount"

discount = subtotal * discount_rate
total = subtotal - discount

print("-"*30)
print(f"Discount tier : {tier}")
print(f"Discount : {discount} KZT")
print(f"Total : {total} KZT")

#A3
print("-"*30)
print(f"Name uppercase : {customer_name.upper()}")
print(f"Name lowercase : {customer_name.lower()}")
print(f"Name length : {len(customer_name)}")

if len(customer_name) > 5:
    print("Long name")
else:
    print("Short name")