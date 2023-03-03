from tkinter import *
import tkinter.messagebox as messagebox
from datetime import datetime
import csv
from Pizza import Pizza

root = Tk()
root.title("Pizza Order System")

# Create labels for each input field
Label(root, text="Name:").grid(row=0, column=0)
Label(root, text="User ID:").grid(row=1, column=0)
Label(root, text="Credit Card Number:").grid(row=2, column=0)
Label(root, text="Credit Card CVV:").grid(row=3, column=0)
Label(root, text="Choose a Pizza:").grid(row=4, column=0)
Label(root, text="Choose a Sauce:").grid(row=5, column=0)

# Create entry widgets for input
name_entry = Entry(root)
id_entry = Entry(root)
card_entry = Entry(root)
cvv_entry = Entry(root)
name_entry.grid(row=0, column=1)
id_entry.grid(row=1, column=1)
card_entry.grid(row=2, column=1)
cvv_entry.grid(row=3, column=1)

# Create option menus for pizza and sauce selection
pizza_var = StringVar()
sauce_var = StringVar()
pizza_var.set("Choose a pizza")
sauce_var.set("Choose a sauce")
pizza_option = OptionMenu(root, pizza_var, "Margherita", "Pepperoni", "Vegetarian", "Hawaiian")
sauce_option = OptionMenu(root, sauce_var, "Tomato", "Alfredo", "Pesto")
pizza_option.grid(row=4, column=1)
sauce_option.grid(row=5, column=1)

def place_order():
    name = name_entry.get()
    id_number = id_entry.get()
    card_number = card_entry.get()
    card_password = cvv_entry.get()
    pizza_choice = pizza_var.get()
    sauce_choice = sauce_var.get()

    # Check if all fields are filled out
    if not name or not id_number or not card_number or not card_password or pizza_choice == "Choose a pizza" or sauce_choice == "Choose a sauce":
        messagebox.showerror("Error", "Please fill out all fields.")
        return

    # Create a Pizza and Sauce object based on user selection
    try:
        pizza = Pizza(pizza_choice)
        sauce = Pizza(sauce_choice)
    except ValueError:
        messagebox.showerror("Error", "Invalid pizza or sauce selection.")
        return

    # Add the order to the database
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Siparis_header = ['Name', 'User ID', 'Credit Card Number', 'Description of the order', 'Credit Card CVV', 'Time of order']
    Siparis_data = [name, id_number, card_number, sauce.get_description(), card_password, current_time]
    with open('Orders_Database.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(Siparis_data)

    # Display a success message and clear the input fields
    messagebox.showinfo("Success", "Your order has been placed!")
    name_entry.delete(0, END)
    id_entry.delete()
    root.mainloop()
