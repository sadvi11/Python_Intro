# Step 1: Define available items and their prices
grocery_items = {
    "apple": 2.5,
    "banana": 1.0,
    "milk": 3.0,
    "bread": 2.0,
    "eggs": 4.0
}

cart = []  # Step 2: Empty cart to hold user items

print("Welcome to Python Grocery Store!")
print("Available items:")
for item, price in grocery_items.items():
    print(f"- {item}: ${price}")

# Step 3: Let user add items
while True:
    product = input("\nEnter an item to add to cart (or 'done' to checkout): ").lower()
    
    if product == 'done':
        break
    elif product in grocery_items:
        cart.append(product)
        print(f"✔️ {product} added to cart.")
    else:
        print("❌ Item not available.")

# Step 4: Checkout and calculate bill
total = 0
print("\n🛒 Your Cart:")
for item in cart:
    print(f"- {item}: ${grocery_items[item]}")
    total += grocery_items[item]

# Step 5: Apply discount logic
if total > 20:
    discount = total * 0.1
    total -= discount
    print(f"\n🎉 You got a 10% discount: -${discount:.2f}")

print(f"\n💰 Total amount to pay: ${total:.2f}")
print("Thank you for shopping with us!")

