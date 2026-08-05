#code for inventory management system

products = [
    [101, "Rice", 50, 20],
    [102, "Sugar", 45, 15],
    [103, "Oil", 120, 10],
    [104, "Salt", 20, 30],
    [105, "Tea", 180, 8]
    ]

while True:
    print("\n")
    print("---- Inventory Management System ----")
    print("\n")
    print("1. View Product")
    print("2. Add New Product")
    print("3. Update Product Price")
    print("4. Add Stock")
    print("5. Sell Product")
    print("6. Remove Product")
    print("7. Search Product")
    print("8. View Low Stock Product")
    print("9. Calculate Total Inventory Value")
    print("10. Exit")
    print("\n")

    choice = input("Enter Your Choice(1-10): ")

    match choice:
        case '1':
            #view product
            #check for exception
            if 0 < len(products):
                print("ID    Name    Price    Stock")
                #loop for viewing products
                for item in products:
                    print(f"{item[0]}    {item[1]}    {item[2]}    {item[3]}")
            else:
                print("No Product Available!")

        case '2':
            #add new product
            new = []
            
            product_id = int(input("Enter Product ID: "))
            product_name = input("Enter Product Name: ")
            product_price = int(input("Enter Product Price: "))
            stock_quantity = int(input("Enter Stock Quantity: "))

            #exceptions
            if product_id < 0:
                print("Invalid Input, please enter positive ID!")
            elif product_price < 0:
                print("Invalid Input, please enter positive price!")
            elif stock_quantity < 0:
                print("Invalid Input, please enter positive stock!")
            else:
                new.append(product_id)
                new.append(product_name)
                new.append(product_price)
                new.append(stock_quantity)

                #check if id exists
                count = 0
                for num in range(len(products)):
                    if new[0] == products[num][0]:
                        print("Product Already Exists!")
                    else:
                        pass
                        count += 1

                if len(products) == count:
                    print("Product Added Successfully!")
                    products.append(new)

        case '3':
            #update product price
            product_id = int(input("Enter Product ID: "))

            current_list = []
            count = 0

            #check if products in list
            if 0 < len(products):
                for i in range(len(products)):
                    if products[i][0] == product_id:
                        current_list = products[i]
                        print(f"Current Price: Rs{current_list[2]}")
                        new_price = int(input("Enter New Price(Rs): "))

                        #updating original list
                        del current_list[2]
                        current_list.insert(2, new_price)
                        del products[i]
                        products.insert(i, current_list)
                        print("Price Updated Successfully!")
                    else:
                        pass
                        count += 1

                if 0 < len(products) == count:
                    print("Product Not Found!")

            else:
                print("No Product Available!")

        case '4':
            #add stock
            product_id = int(input("Enter Product ID: "))

            current = []
            count = 0

            for i in range(len(products)):
                if products[i][0] == product_id:
                    current = products[i]
                    print(f"Current Stock: {current[3]}")
                    new_stock = int(input("Enter Quantity to Add: "))
                    new_stock += current[3]

                    #updating original list
                    del current_list[3]
                    current.insert(3, new_stock)
                    del products[i]
                    products.insert(i, current)
                    print(f"Updated Stock: {products[i][3]}")
                else:
                    pass
                    count += 1

            if len(products) == count:
                print("Product Not Found!")

        case '5':
            #sell stock
            product_id = int(input("Enter Product ID: "))

            current = []
            count = 0

            #check if products in list
            if 0 < len(products):
                for i in range(len(products)):
                    if products[i][0] == product_id:
                        current = products[i]
                        sell_quantity = int(input("Enter Quantity to sell: "))

                        #check quantity if available
                        if current[3] >= sell_quantity:
                            #reduce quantity and calculate bill
                            current[3] -= sell_quantity
                            sell_price = current[2] * sell_quantity
                            

                            #print statements
                            print(f"Product Name: {current[1]}")
                            print(f"Quantity Sold: {sell_quantity}")
                            print(f"Total Bill: {sell_price}")
                            print(f"Remaining Stock: {current[3]}")

                            del products[i]
                            products.insert(i, current)

                        else:
                            print("Insufficiant Stock!")

                    else:
                        pass
                        count += 1

                if 0 < len(products) == count:
                    print("Product Not Found!")

            else:
                print("No Product Available!")

        case '6':
            #remove product
            product_id = int(input("Enter Product ID: "))
            
            current = []
            count = 0

            #check if products in list
            if 0 < len(products):
                for i in range(len(products)):
                    if products[i][0] == product_id:
                        del products[i]
                        print("Product Removed Successfully!")
                        count -= 1
                        break

                    else:
                        pass
                        count += 1

                if len(products) == count: 
                    print("Product Not Found!")

            else:
                print("No Products Available!")

        case '7':
            #search product
            product = input("Enter Product ID or Name: ")

            count = 0

            #check if products in list
            if 0 < len(products):
                if product[0].isalpha():
                    for i in range(len(products)):
                        if products[i][1].lower() == product.lower():
                            print(f"ID    Name    Price    Quantity")
                            print(f"{products[i][0]}    {products[i][1]}    {products[i][2]}    {products[i][3]}")
                        else:
                            pass
                            count += 1
                elif product[0].isdigit():
                    for i in range(len(products)):
                        if products[i][0] == int(product):
                            print(f"ID    Name    Price    Quantity")
                            print(f"{products[i][0]}    {products[i][1]}    {products[i][2]}    {products[i][3]}")
                        else:
                            pass
                            count += 1

                if 0 < len(products) == count:
                    print("Product Not Found!")

            else:
                print("No Product Available!")

        case '8':
            #low stock products
            #check if products in list
            if 0 < len(products):
                min_stock = 10
                print("Minimum Stock Level: ", min_stock)
                count = 0
                low_stock = []
                #loop for checking in products 
                for item in range(len(products)):
                    #check for low stock products
                    if products[item][3] <= min_stock:
                        low_stock.append(products[item])
                    else:
                        pass
                        count += 1

                if len(low_stock) > 0:
                    print("ID    Name    Stock")
                    for num in low_stock:
                        print(f"{num[0]}    {num[1]}    {num[3]}")

                if 0 < len(products) == count:
                    print("Now Low Stock Product!")
            else:
                print("No Product Available!")

        case '9':
            #calculate total inventory value
            total_value = product_value = 0

            #check if products in list
            if 0 < len(products):
                #loop for calculating total value
                for items in products:
                    product_value = items[2] * items[3]
                    total_value += product_value

                    print(f"Total Value of {items[1]}(Rs): {product_value}")

                print("Total Inventory Value(Rs): ",total_value)
            else:
                print("No Product Available!")


        case '10':
            #exit 
            print("Exiting the program....")
            print("Exited Successfully!")
            exit()

        case _:
            #exception
            print("Invalid Input, Please enter from given option!")
