# inventory: product catalog with price and available stock
# cart: stores selected products with their price and quantity
# menu / pick_menu: text menus shown to the user

inventory = {
    "Apple": {"price": 3000, "stock": 9},
    "Rice": {"price": 2000, "stock": 2},
    "Coffee": {"price": 1500, "stock": 3}
}
cart = {}
menu = (""
        "1. Add products to the cart.\n"
        "2. Show shopping cart.\n"
        "3. Delete product.\n"
        "4. Cancel shopping cart.\n"
        "5. Check out / Exit.\n")

pick_menu = (""
             "1. Apple\n"
             "2. Rice\n"
             "3. Coffee\n"
             "4. Exit\n")

# discountStock: reduce inventory stock if enough quantity is available, return True/False
def discountStock(product, quantity):
    available =  inventory[product]["stock"]
    if available >= quantity:
        inventory[product]["stock"] -= quantity
        return True
    else:
        print(f"The product {product} has a stock of {available}")
        return False

# pickProduct: prompt for quantity, validate input, update cart and inventory if valid
def pickProduct(product):
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ValueError
        flag = discountStock(product, quantity)
        if flag:
            price = inventory[product]["price"]
            if product in cart:
                cart[product]["stock"] += quantity
            else:
                cart[product] = {"price": price, "stock": quantity}
            print("Product successfully added to the cart.")
    except ValueError:
        print("Enter only a positive number")

# main loop: show main menu and handle user choices until checkout/exit
while True:
    print("Welcome to your shopping cart.")
    choice = input(menu)
    if choice == "1":
        while True:
            subchoice = input(pick_menu)
            if subchoice == "1":
                pickProduct("Apple")
            elif subchoice == "2":
                pickProduct("Rice")
            elif subchoice == "3":
                pickProduct("Coffee")
            elif subchoice == "4":
                break
            else:
                print("Invalid option.")
    elif choice == "2":
        print("Your shopping cart")
        # Option 2: display cart contents, compute and show each product subtotal
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            for product in cart:
                quantity = cart[product]["stock"]
                subtotal = cart[product]["price"] * quantity
                print(f"{product}: quantity: {quantity}, price: {subtotal}")
    elif choice == "3":
        # Option 3: delete a product from cart and restore its quantity to inventory
        subchoice = input("Enter the name of the product you want to delete: ").capitalize()
        if subchoice in cart:
            quantity = cart[subchoice]["stock"]
            inventory[subchoice]["stock"] += quantity
            cart.pop(subchoice)
            print("Product successfully removed from the cart.")
        else:
            print("The product doesn't seem to exist in your cart.")
    elif choice == "4":
        # Option 4: cancel entire cart, restore all quantities to inventory and clear cart
        subchoice = input("Are you sure you want to delete your shopping cart? Press (Y) to continue: ").capitalize()
        if subchoice == "Y":
            for product in cart:
                quantity = cart[product]["stock"]
                inventory[product]["stock"] += quantity
            cart.clear()
            print("All your shopping cart has been successfully deleted.")
        else:
            print("Deleting process cancelled.")
    elif choice == "5":
        # Option 5: checkout - if cart empty show farewell, otherwise print items, totals and exit
        if (len(cart) == 0):
            print("Thanks for visiting us. Hope you purchase something next time.")
        else:
            total = 0
            for product in cart:
                quantity = cart[product]["stock"]
                subtotal = cart[product]["price"] * quantity
                total += subtotal
                print(f"{product}: quantity: {quantity}, subtotal: {subtotal}")
            print(f"Total cost: {total}. Thank for your purchase.")
        break
    else:
        # Invalid option: notify the user
        print("Invalid option.")