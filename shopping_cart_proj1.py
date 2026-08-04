#code for shopping cart system using functions

#products tuple
products = (("apple", 20), ("banana", 30), ("mango", 40))

#empty cart
cart = []

def show_products(tuple):
    #loop for showing products
    print("Product Name    Price(Rs)")
    for i in range(len(tuple)):
        print(f"{i+1}. {tuple[i][0]} : Rs{tuple[i][1]}")

def add_item(tuple, list):
    #function call to show products
    show_products(tuple)

    #taking input to add item into cart
    item = int(input("Enter Item Number to Add: "))

    #check for exception
    if 0 < item <= len(tuple):
        list.append(tuple[item-1])
        print("Item Addedd!")
    else:
        print("Invalid Input!")

def view_cart(list):
    #check if cart is empty
    if 0 < len(list):
        print("Item Name    Price(Rs)")
        #loop for showing items
        for items in list:
            print(f"{items[0]} :  {items[1]}")
    else:
        print("Cart is Empty!")

def remove_item(list):
    #check cart if cart is empty
    if len(list) > 0:
        print("S.No  Item Name    Price(Rs)")
        for product in range(len(list)):
            print(f"{product+1}. {list[product][0]}   {list[product][1]}")
        
        remove_item = int(input("Enter Item Number to Remove: "))

        #check for exception
        if 0 < remove_item <= len(cart):
            del list[remove_item - 1]
            print("Item Removed!")
        else:
            print("Invalid Input!")
    else:
        print("Cart is Empty!")

def total_bill(list):
    #check if cart is empty
    if 0 < len(list):
        sum = 0
        #loop for summing all item prices
        view_cart(list)
        for price in list:
            sum += price[1]
        
        print("Total Bill: ", sum)
    else:
        print("Cart is Empty!")

def shopping_cart():
    print("----SHOPPING CART SYSTEM----")

    #infinite loop
    while True:
        print("Menu: ")
        print("1. Show Prodcuts")
        print("2. Add Item")
        print("3. View Cart")
        print("4. Remove Item")
        print("5. Total Bill")
        print("6. Exit")

        choice = int(input("Choose an option(1-6): "))

        match choice:
            case 1:
                #unction call for showing products
                show_products(products)

            case 2:
                #function call for adding item
                add_item(products, cart)

            case 3:
                #function call for viewing cart
                view_cart(cart)

            case 4:
                #function call for removing item
                remove_item(cart)       

            case 5:
                #function call for calculating bill
                total_bill(cart)

            case 6:
                #exit program
                print("Exiting Shopping Cart System....")
                print("Thank you for Shopping!")
                exit()

            case _:
                #exception handling
                print("Invalid Input, Please enter from the given options!")

shopping_cart()