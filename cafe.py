menu = {
    "espresso": {"description": "A shot of bold, concentrated coffee", "price": 100},
    "cappuccino": {"description": "Espresso with steamed milk and foam", "price": 150},
    "latte": {"description": "Espresso with steamed milk", "price": 140},
    "americano": {"description": "Espresso diluted with hot water", "price": 110},
    "tea": {"description": "A selection of herbal and black teas", "price": 80},
    "croissant": {"description": "A buttery, flaky pastry", "price": 90},
    "muffin": {"description": "A variety of freshly baked muffins", "price": 100},
    "scone": {"description": "A traditional British baked good", "price": 110},
    "bagel": {"description": "A chewy, circular bread", "price": 80},
    "avocado toast": {"description": "Toasted bread with mashed avocado", "price": 180}
}

def display_menu():
    print("Welcome to our Cafe!")
    print("Here's our menu:")
    for item, details in menu.items():
        print(f"{item.capitalize()}: {details['description']} - ₹{details['price']}")

def place_order():
    order = []
    total = 0
    while True:
        item = input("Enter an item to order (or 'q' to finish): ").lower()
        if item == 'q':
            break
        if item in menu:
            order.append(menu[item]['description'])
            total += menu[item]['price']
            print(f"{menu[item]['description']} added to your order.")
        else:
            print("Sorry, that item is not on the menu.")
    return order, total

def main():
    display_menu()
    order, total = place_order()
    print("\nYour order:")
    for item in order:
        print(f"- {item}")
    print(f"\nTotal: ₹{total}")

if __name__ == "__main__":
    main()