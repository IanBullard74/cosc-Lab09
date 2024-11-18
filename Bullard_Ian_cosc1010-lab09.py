# Ian Bullard
# UWYO COSC 1010
# Submission Date 11/11/24
# Lab 09
# Lab Section: 14
# Sources, people worked with, help given to:  Pierson Klam, a grad student in Colorado, He helped me pretty my code up and fix my pizzeria class as it wouldn't append my toppings
# Your
# Comments
# Here
# 
# 
# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria
# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list


# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
# - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.

# - This method needs to be able to handle multiple values.
# - Append all elements to the list.
# Create a method that returns the amount of toppings.

# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.
 
 
 
# Part 2
# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost perinch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
# - This one does not need to take in any extra parameters.
# - It should create and set the attributes defined above.
# - placeOrder():
# - This method will allow a customer to order a pizza.
# - Which will increment the number of orders.
# - It will need to create a pizza object.
# - You will need to prompt the user for:
# - the size
# - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
# - all the toppings the user wants, ending prompting on an empty string.
# - Implementation of this is left to you; you can, for example:
# - have a while loop and append new entries to a list
# - have the user separate all toppings by a space and turn that into a list.
# - Upon completion, create the pizza object and store it in the list.
# - getPrice()
# - You will need to determine the price of the pizza.
# - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
# - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
# - Creates a receipt of the current pizza.
# - Show the sauce, size, and toppings.
# - Show the price for the size.
# - The price for the toppings.
# - The total price.
# - getNumberOfOrders()
# - This will simply return the number of orders.
# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.
# 
# 
# Example output:
# """
# Would you like to place an order? exit to exit
# yes
# Please enter the size of pizza, as a whole number. The smallest size is 10
# 20
# What kind of sauce would you like?
# Leave blank for red sauce
# garlic
# Please enter the toppings you would like, leave blank when done
# pepperoni
# bacon
# You ordered a 20" pizza with garlic sauce and the following toppings:
# cheese
# pepperoni
# bacon
# You ordered a 20" pizza for 12.0
# You had 3 topping(s) for $0.8999999999999999
# Your total price is $12.9
# Would you like to place an order? exit to exit

class Pizza:
    def __init__(self, size, sauce="red"):
        """Defines the size, sauce, and toppings for the pizza."""
        self.set_size(size)  # Validate and set size
        self.sauce = sauce
        self.toppings = ["cheese"]  # Default toppings include cheese

    def get_size(self):
        """Returns the size of the pizza."""
        return self.size

    def set_size(self, size):
        """Sets the size of the pizza, ensuring it is at least 10 inches."""
        if isinstance(size, int) and size >= 10:
            self.size = size
        else:
            self.size = 10

    def get_sauce(self):
        """Returns the sauce of the pizza."""
        return self.sauce

    def get_toppings(self):
        """Returns the toppings of the pizza."""
        return self.toppings

    def add_toppings(self, *new_toppings):
        """Adds multiple toppings to the pizza."""
        self.toppings.extend(new_toppings)

    def get_topping_count(self):
        """Returns the number of toppings."""
        return len(self.toppings)


class Pizzaria:
    price_per_topping = 0.30  # Static value for price per topping
    price_per_inch = 0.60  # Static value for price per inch

    def __init__(self):
        """Initialize the pizzeria."""
        self.orders = []  # List to store all pizza orders
        self.order_count = 0  # Counter for the number of orders

    def place_order(self):
        """Place a new order for a pizza."""
        size = int(input("Enter the size of your pizza (minimum 10 inches):\n"))
        sauce = input("Enter the sauce for your pizza (leave blank for red sauce):\n") or "red"

       
        toppings = []
        print("Enter the toppings you want one by one. Type 'exit' when finished:")
        while True:
            topping = input("Enter a topping: ").strip().lower()
            if topping == "exit":
                break
            toppings.append(topping)

        
        pizza = Pizza(size, sauce)
        pizza.add_toppings(*toppings)
        price = self.get_price(pizza)

        
        self.orders.append((pizza, price))
        self.order_count += 1

        
        self.get_receipt(pizza, price)

    def get_price(self, pizza):
        """
        Calculate the price of a pizza.
        Price = (size * price_per_inch) + (number of toppings * price_per_topping)
        """
        size_price = pizza.get_size() * self.price_per_inch
        topping_price = (pizza.get_topping_count() - 1) * self.price_per_topping  # Exclude cheese
        return size_price + topping_price

    def get_receipt(self, pizza, price):
        """Prints the receipt for a single pizza order."""
        print("\n--- Receipt ---")
        print(f"Size: {pizza.get_size()} inches")
        print(f"Sauce: {pizza.get_sauce()}")
        print(f"Toppings: {', '.join(pizza.get_toppings())}")
        print(f"Price for size: ${pizza.get_size() * self.price_per_inch:.2f}")
        print(f"Price for toppings: ${(pizza.get_topping_count() - 1) * self.price_per_topping:.2f}")
        print(f"Total Price: ${price:.2f}")
        print("---------------\n")

    def get_number_of_orders(self):
        """Returns the total number of orders placed."""
        return self.order_count

    def show_all_orders(self):
        """Displays all orders with their details and prices."""
        if not self.orders:
            print("No orders have been placed yet.")
            return

        print("\n--- All Orders ---")
        total_price = 0
        for i, (pizza, price) in enumerate(self.orders, start=1):
            print(f"Order {i}:")
            print(f"  - Size: {pizza.get_size()} inches")
            print(f"  - Sauce: {pizza.get_sauce()}")
            print(f"  - Toppings: {', '.join(pizza.get_toppings())}")
            print(f"  - Price: ${price:.2f}")
            total_price += price
        print(f"Total Revenue: ${total_price:.2f}")
        print("------------------")



if __name__ == "__main__":
    pizzeria = Pizzaria()

    while True:
        action = input("Welcome to Bully's Pizzeria!\nWould you like to place an order? Type 'yes' to order, 'exit' to exit:\n").lower()
        if action == "exit":
            print("\nFinal Summary:")
            pizzeria.show_all_orders()
            print(f"Total orders placed: {pizzeria.get_number_of_orders()}")
            print("Thank you for visiting Bully's pizzeria!")
            break
        elif action == "yes":
            pizzeria.place_order()
        else:
            print("Please type 'yes' to order or 'exit' to leave.")
