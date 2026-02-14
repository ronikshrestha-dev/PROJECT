# Cafe Retro Management System
print("Welcome to Ronik's Cafe! Chill spot for your weekends..")

# Menu items
menu = [
    {"name": "Espresso", "price": 70},
    {"name": "Cappuccino", "price": 100},
    {"name": "Latte", "price": 120},
    {"name": "Sandwich", "price": 150},
    {"name": "Pasta", "price": 200},
    {"name": "Milkshake", "price": 90}
]

# Function to show menu
def show_menu():
    print("\n--- Cafe Retro Menu ---")
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item['name']} - Rs {item['price']}")

# Function to take order
def take_order():
    order = []
    while True:
        try:
            choice = int(input("\nEnter the item number you want to order (0 to finish): "))
            if choice == 0:
                break
            if choice < 1 or choice > len(menu):
                print("❌ Invalid choice, try again!")
                continue

            quantity = int(input(f"How many {menu[choice-1]['name']} do you want? "))
            if quantity < 1:
                print("❌ Quantity must be at least 1")
                continue

            # Add to order
            order.append({
                "item": menu[choice-1]['name'],
                "quantity": quantity,
                "total": menu[choice-1]['price'] * quantity
            })

            print(f"✅ Added {quantity} x {menu[choice-1]['name']} to your order")

        except ValueError:
            print("❌ Please enter a valid number!")

    return order

# Function to print bill
def print_bill(order):
    if order:
        print("\n--- Your Order ---")
        grand_total = 0
        for item in order:
            print(f"{item['quantity']} x {item['item']} = Rs {item['total']}")
            grand_total += item['total']
        print(f"\nTotal Bill: Rs {grand_total}")
        print("Thank you for visiting Cafe Retro! ☕")
    else:
        print("No items ordered. Goodbye!")

# Main program loop
def main():
    while True:
        print("\n1. Show Menu")
        print("2. Place Order")
        print("3. Exit")

        choice = input("Enter your choice: ").lower()

        if choice in ["1", "show menu", "menu"]:
            show_menu()
        elif choice in ["2", "place order", "order"]:
            show_menu()
            order = take_order()
            print_bill(order)
        elif choice in ["3", "exit", "quit"]:
            print("👋 Goodbye! Visit Cafe Retro again!")
            break
        else:
            print("❌ Invalid choice, try again!")

# Start program
if __name__ == "__main__":
    main()
