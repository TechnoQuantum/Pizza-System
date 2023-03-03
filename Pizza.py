# %%
import csv
from datetime import datetime
import os.path

# %%
# Create Menu.txt
with open("Menu.txt", "w") as f:
    f.write("* Please Choose a Pizza Base:\n\n")
    f.write("1: Classic\n")
    f.write("2: Margherita\n")
    f.write("3: TurkPizza\n")
    f.write("4: PlainPizza\n\n")
    f.write("* and sauce of your choice:\n\n")
    f.write("11: Olives\n")
    f.write("12: Mushrooms\n")
    f.write("13: GoatCheese\n")
    f.write("14: Meat\n")
    f.write("15: Onions\n")
    f.write("16: Corn\n\n")
    f.write("* Thank you!")

# Create superclass Pizza
class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"
        self.cost = 0.0
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

# Create subclasses for each type of pizza
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Classic Pizza"
        self.cost = 10.0

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 12.0

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizza"
        self.cost = 15.0

class DominosPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Dominos Pizza"
        self.cost = 20.0

# Create superclass Decorator
class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

# Define sauce classes
class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Olives"
        self.cost = 1.0

class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mushrooms"
        self.cost = 1.5

class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Goat Cheese"
        self.cost = 2.0

class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Meat"
        self.cost = 2.5

class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Onions"
        self.cost = 1.0

class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Corn"
        self.cost = 1.5

# %%
def my_and_func(lst): 
    res = True
    for e in lst:
        res = res and e
    return res

def get_input(input_message, conditions):
    inp = input(input_message)
    while not my_and_func([cond(inp) for cond in conditions]):
        inp = input("Incorrect input. Please try again.\n")
    return inp

# %%
# Create main function
def main():
    # Display menu
    with open("Menu.txt", "r") as f:
        print(f.read())
    
    # Create Database as CSV
    class OrdersDatabase:
    
     def __init__(self, filename):
        self.filename = filename
    
    # prompt the user for name, id number, credit card number, and password
    name = input('Please enter your name: ')
    
    def is_numeric(x):
        return x.isnumeric()
    
    def check_len16(x):
        return len(x) == 16
    
    def check_len3(x):
        return len(x) == 3
    
    
    id_number = get_input("Please enter your ID number: ", [is_numeric])
    
    card_number = get_input('Please enter your credit card number: ', [is_numeric, check_len16])
    
    card_password = get_input("Please enter your CVV: ", [is_numeric, check_len3])
        
    # print the menu
    f = open("Menu.txt", "r")
    print('Menu:')
    print(f.read())

    # prompt the user for pizza and sauce choices
    def get_pizza_choice():
        while True:
            try:
                choice = int(input("Enter the number corresponding to your pizza choice: "))
                if choice < 1 or choice > 4:
                    raise ValueError("Invalid pizza choice. Please enter a number between 1 and 4")
                else:
                    return choice
            except ValueError as ve:
                print(ve)

    def get_sauce_choice():
        while True:
            try:
                choice = int(input("Enter the number corresponding to your sauce choice: "))
                if choice < 11 or choice > 16:
                    raise ValueError("Invalid sauce choice. Please enter a number between 1 and 16")
                else:
                    return choice
            except ValueError as ve:
                print(ve)
    pizza_choice = get_pizza_choice()
    sauce_choice = get_sauce_choice()
    # create the pizza and sauce objects
    if pizza_choice == 1:
        pizza = ClassicPizza()
    elif pizza_choice == 2:
        pizza = MargheritaPizza()
    elif pizza_choice == 3:
        pizza = TurkPizza()
    elif pizza_choice == 4:
        pizza = DominosPizza()

    if sauce_choice == 11:
        sauce = Olives(pizza)
    elif sauce_choice == 12:
        sauce = Mushrooms(pizza)
    elif sauce_choice == 13:
        sauce = GoatCheese(pizza)
    elif sauce_choice == 14:
        sauce = Meat(pizza)
    elif sauce_choice == 15:
        sauce = Onions(pizza)
    elif sauce_choice == 16:
        sauce = Corn(pizza)

    # calculate the total cost of the order
    total_cost = sauce.get_cost()

    # get the description of the order
    order_description = sauce.get_description()

    # get the current time
    current_time = datetime.now()
   
    # print the order details
    print('\nOrder Summary:')
    print('Pizza:', pizza.get_description())
    print('Sauce:', sauce.get_description())
    print('Total Cost:', total_cost)
    print('Order Time:', current_time)


   # Define the header for the CSV file
    Siparis_header = ['Name', 'User ID', 'Credit Card Number', 'Description of the order', 'Credit Card CVV', 'Time of order']

    # Define the actual data
    Siparis_data = [name, id_number, card_number, sauce.get_description(), card_password, current_time]

# Check if the file exists
    if os.path.exists('Orders_Database.csv'):
    # File already exists, so open in append mode and skip the header row
        with open('Orders_Database.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(Siparis_data)
    else:
    # File doesn't exist, so create a new file and write the header row
        with open('Orders_Database.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(Siparis_header)
            writer.writerow(Siparis_data)
    


# %%
main()


