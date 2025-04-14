# Complex Vegetable Shop (No functions, just loops and conditionals)

# Sample login system
username = "admin"
password = "1234"

print("=== Welcome to the Vegetable Shop ===")
print("Please login to continue.")

logged_in = False
attempts = 0

while not logged_in and attempts < 3:
    user_input = input("Username: ")
    pass_input = input("Password: ")
    if user_input == username and pass_input == password:
        logged_in = True
        print("Login successful!\n")
    else:
        print("Incorrect username or password.\n")
        attempts += 1

if not logged_in:
    print("Too many failed attempts. Exiting...")
else:
    vegetables = ["Tomato", "Potato", "Onion", "Carrot", "Spinach", "Cabbage", "Cauliflower"]
    prices = [30, 20, 25, 40, 15, 35, 45]
    stock = [100, 80, 75, 60, 90, 50, 40]  # in kg
    cart = [0] * len(vegetables)
    total = 0

    while True:
        print("\n====== Main Menu ======")
        print("1. Show Vegetables")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Vegetables:")
            for i in range(len(vegetables)):
                print(f"{i+1}. {vegetables[i]} - ₹{prices[i]}/kg (Stock: {stock[i]} kg)")

        elif choice == "2":
            print("\nAdd items to your cart (Enter 0 to stop):")
            while True:
                for i in range(len(vegetables)):
                    print(f"{i+1}. {vegetables[i]} - ₹{prices[i]}/kg")
                veg_choice = int(input("Enter item number (0 to stop): "))
                if veg_choice == 0:
                    break
                elif 1 <= veg_choice <= len(vegetables):
                    qty = float(input("Enter quantity (kg): "))
                    index = veg_choice - 1
                    if qty <= stock[index]:
                        cart[index] += qty
                        stock[index] -= qty
                        print(f"Added {qty} kg of {vegetables[index]} to cart.")
                    else:
                        print(f"Only {stock[index]} kg available in stock.")
                else:
                    print("Invalid selection.")

        elif choice == "3":
            print("\n===== Your Cart =====")
            total = 0
            for i in range(len(cart)):
                if cart[i] > 0:
                    item_total = cart[i] * prices[i]
                    print(f"{vegetables[i]} - {cart[i]} kg × ₹{prices[i]} = ₹{item_total}")
                    total += item_total
            print(f"\nSubtotal: ₹{total}")
            discount = 0
            if total >= 500:
                discount = total * 0.1
                print(f"Discount (10%): -₹{discount}")
            elif total >= 300:
                discount = total * 0.05
                print(f"Discount (5%): -₹{discount}")
            taxed_total = total - discount
            gst = taxed_total * 0.05
            final_total = taxed_total + gst
            print(f"GST (5%): +₹{gst}")
            print(f"Total Payable: ₹{final_total}")

        elif choice == "4":
            print("\n===== Final Bill =====")
            total = 0
            for i in range(len(cart)):
                if cart[i] > 0:
                    item_total = cart[i] * prices[i]
                    print(f"{vegetables[i]} - {cart[i]} kg × ₹{prices[i]} = ₹{item_total}")
                    total += item_total
            print(f"\nSubtotal: ₹{total}")
            discount = 0
            if total >= 500:
                discount = total * 0.1
                print(f"Discount (10%): -₹{discount}")
            elif total >= 300:
                discount = total * 0.05
                print(f"Discount (5%): -₹{discount}")
            taxed_total = total - discount
            gst = taxed_total * 0.05
            final_total = taxed_total + gst
            print(f"GST (5%): +₹{gst}")
            print(f"\nAmount to Pay: ₹{final_total}")
            print("\nThank you for shopping with us!")
            break

        elif choice == "5":
            print("Exiting the shop. Thank you!")
            break

        else:
            print("Invalid choice. Please select from the menu.")
