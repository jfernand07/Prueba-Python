#Como líder de operaciones de inventario, quiero un sistema que permita
#gestionar el inventario de una tienda de manera dinámica, para que pueda realizar un seguimiento
#eficiente de los productos disponibles, su cantidad y precios actualizados, además de calcular el valor
#total del inventario.
#____________________________
#Funcionalidades principales: para alcanzar un resultado óptimo en esta prueba, deberás:
#1. Añadir productos al inventario: permitir al usuario agregar productos con atributos como
#nombre, precio y cantidad disponibles.
#2. Consultar productos en inventario: buscar un producto por su nombre y mostrar sus
#detalles (nombre, precio, cantidad).
#3. Actualizar precios de productos: modificar el precio de un producto específico en el
#inventario.
#4. Eliminar productos del inventario: permitir la eliminación de un producto que ya no está
#disponible.
#5. Calcular el valor total del inventario: multiplicar el precio por la cantidad de cada producto
#y mostrar el total acumulado.

#List and Dictionary, previously entered data

        #Inventory management/ I create a list and within the list a dictionary with the information
inventory = [
    {"product": "book", "price": 10.0, "quantity": 10},
    {"product": "mouse", "price": 15.0, "quantity": 50},
    {"product": "keyboard", "price": 20.0, "quantity": 30},
    {"product": "monitor", "price": 25.0, "quantity": 10},
    {"product": "headset", "price": 30.0, "quantity": 5}
]
# I created the data validation functions, both numbers and error messages.
# Menu option validation (1-6)
def confirmation(valor):
    try:
        return 1 <= int(valor) <= 6
    except ValueError:
        return False

# Integer validation
def numint(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

# Decimal number validation
def numfloat(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Asks the user if they want to continue
def answer():
    while True:
        response = input("Do you want to continue (Yes/No): ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Error, please enter 'Yes' or 'No'.")
# We begin to create and define the functions that will perform system operations such as adding, updating, searching, and deleting.
# Add a new product
def add(product, price, quantity):
    inventory.append({"product": product, "price": float(price), "quantity": int(quantity)})
    print(f"Product '{product}' successfully added.")

# Search for a product in the inventory
def search(product):
    products = next((item for item in inventory if item["product"] == product), None)
    if not products:
        print("This product is not registered.")
    else:
        print(f"Product: {products['product']} | Price: {products['price']:.2f} | Quantity: {products['quantity']}")

# Update the price of a product
def updated_price(product, new_price):
    for products in inventory:
        if products["product"] == product:
            products["price"] = float(new_price)
            print(f"The price of '{product}' has been updated to ${float(new_price):.2f}")
            return
    print("This product is not in inventory.")

# Remove a product from inventory
def remove(product):
    global inventory
    new_inventory = [item for item in inventory if item["product"] != product]
    if len(new_inventory) == len(inventory):
        print("This product is not in inventory.")
    else:
        inventory = new_inventory
        print(f"The product '{product}' has been removed from inventory.")

# Calculate the total value of the inventory
def totalvalue():
    if not inventory:
        print("The inventory is empty.")
    else:
        total_value = sum(item["price"] * item["quantity"] for item in inventory)
        print(f"The total value of the inventory is: ${total_value:.2f}")

# Displays the main menu
def menu():
    print("\n--- Inventory Management System ---")
    print("1. Add product")
    print("2. Search product")
    print("3. Update price")
    print("4. Remove product")
    print("5. Calculate total inventory value")
    print("6. Exit")

# Run the system
def system():
    while True:
        menu()
        
        #I added a data validation option that is correct
        option = input("Select an option (1-6): ").strip()
        if not confirmation(option):
            print("Error: Option must be a number between 1 and 6.")
            continue
#I add the conditions and call them functions
        if option == "1":
            while True:
                product = input("Enter product name: ").strip().lower()
                if any(item["product"] == product for item in inventory):
                    print("This product is already registered.")
                    continue
                price = input("Enter the product price: ").strip()
                if not numfloat(price) or float(price) <= 0:
                    print("Error: Price must be a positive number.")
                    continue
                quantity = input("Enter the product quantity: ").strip()
                if not numint(quantity) or int(quantity) <= 0:
                    print("Error: Quantity must be a positive integer.")
                    continue
                add(product, price, quantity)
                if answer() == "no":
                    break

        elif option == "2":
            product = input("Enter product name to search: ").strip().lower()
            search(product)

        elif option == "3":
            product = input("Enter product name to update: ").strip().lower()
            if not any(item["product"] == product for item in inventory):
                print("This product is not registered.")
                continue
            new_price = input("Enter the new price: ").strip()
            if not numfloat(new_price) or float(new_price) <= 0:
                print("Error: Price must be a positive number.")
                continue
            updated_price(product, new_price)

        elif option == "4":
            product = input("Enter product name to remove: ").strip().lower()
            remove(product)

        elif option == "5":
            totalvalue()

        elif option == "6":
            print("Log out")
            break
system()



#https://github.com/jfernand07/Prueba-Python