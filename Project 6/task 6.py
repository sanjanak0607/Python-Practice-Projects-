# Inventory Management System

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "price": price }
        print("Item added successfully.")

    def view_items(self):
        if not self.items:
            print("No Items Present Right Now.")
            return
        for name, details in self.items.items():
            print(f"Name: {name}, Quantity: {details['quantity']}, Price: {details['price']}")

    def remove_item(self, name):
        if name not in self.items:
            raise ValueError("Item not found.")
        del self.items[name]
        print("Item removed successfully.")

    def update_item(self, name, quantity=None, price=None):
        if name not in self.items:
            raise ValueError("Item not found.")
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            self.items[name]["quantity"] = quantity
        if price is not None:
            if price < 0:
                raise ValueError("Price cannot be negative.")
            self.items[name]["price"] = price
        print("Item updated successfully.")

store = Inventory()
while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View Inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")
    try:
        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            store.add_item(name, quantity, price)
        elif choice == "2":
            name = input("Enter item name to remove: ")
            store.remove_item(name)
        elif choice == "3":
            name = input("Enter item name to update: ")
            qty_input = input("Enter new quantity (leave blank to skip): ")
            price_input = input("Enter new price (leave blank to skip): ")
            quantity = int(qty_input) if qty_input else None
            price = float(price_input) if price_input else None
            store.update_item(name, quantity, price)
        elif choice == "4":
            store.view_items()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
    except ValueError as e:
        print("Error:", e)