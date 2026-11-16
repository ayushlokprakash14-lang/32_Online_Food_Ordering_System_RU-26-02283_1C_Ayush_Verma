menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 80,
    "Coke": 40
}

cart = []
coupon = False


def showmenu():
    print("\n----- FOOD MENU -----")

    for item in menu:
        print(item, ":", "₹", menu[item])


def additem():
    item = input("Enter item name: ").strip().title()

    if item not in menu:
        print("Item not available.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid quantity.")
        return

    found = False

    for food in cart:
        if food["name"] == item:
            food["quantity"] += quantity
            found = True
            break

    if not found:
        cart.append({
            "name": item,
            "quantity": quantity
        })

    print(item, "x", quantity, "added to cart.")
    print("Cart Total:", "₹", getsubtotal())


def getsubtotal():
    subtotal = 0

    for food in cart:
        item = food["name"]
        quantity = food["quantity"]

        subtotal += menu[item] * quantity

    return subtotal


def showcart():
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    print("\n----- YOUR CART -----")

    for food in cart:
        item = food["name"]
        quantity = food["quantity"]

        print(item, "x", quantity, "=", "₹", menu[item] * quantity)

    print("Cart Total:", "₹", getsubtotal())


def removeitem():
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    item = input("Enter item to remove: ").strip().title()

    for food in cart:
        if food["name"] == item:

            try:
                quantity = int(input("Enter quantity to remove: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    return

            except ValueError:
                print("Please enter a valid quantity.")
                return

            if quantity >= food["quantity"]:
                cart.remove(food)
                print(item, "removed from cart.")
            else:
                food["quantity"] -= quantity
                print(quantity, item, "removed from cart.")

            return

    print("Item not found in cart.")


def applycoupon():
    global coupon

    if coupon:
        print("Coupon already applied.")
        return

    code = input("Enter coupon code: ").strip().upper()

    if code == "SAVE10":
        coupon = True
        print("Coupon applied successfully!")
    else:
        print("Invalid coupon code.")


def checkout():
    if len(cart) == 0:
        print("Your cart is empty.")
        return False

    subtotal = getsubtotal()

    discount = 0

    if coupon:
        discount = subtotal * 10 / 100

    amount = subtotal - discount
    gst = amount * 5 / 100

    delivery = 40

    if amount >= 300:
        delivery = 0

    total = amount + gst + delivery

    print("\n----- FINAL BILL -----")
    showcart()

    print("\nSubtotal:", "₹", format(subtotal, ".2f"))
    print("Discount:", "₹", format(discount, ".2f"))
    print("GST (5%):", "₹", format(gst, ".2f"))
    print("Delivery Charge:", "₹", format(delivery, ".2f"))
    print("----------------------")
    print("Total Amount:", "₹", format(total, ".2f"))
    print("Thank you for ordering!")

    return True


while True:

    print("\n===== FOOD ORDERING SYSTEM =====")
    print("1. Show Menu")
    print("2. Add Item")
    print("3. View Cart")
    print("4. Remove Item")
    print("5. Apply Coupon")
    print("6. Checkout")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        showmenu()

    elif choice == "2":
        additem()

    elif choice == "3":
        showcart()

    elif choice == "4":
        removeitem()

    elif choice == "5":
        applycoupon()

    elif choice == "6":
        if checkout():
            break

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")