'''
Krutik Patel
Date: 5/13/2023
Version 1.0
This is a GUI Tkinter Application that deals with/potrays a Pizza Ordering System for Kuku's Pizzeria.
'''
import tkinter as tk
from tkinter import messagebox

def on_submit():
    '''To run when the user submits the form'''
    # Get user inputs
    name = name_inp.get()
    if not name:
        messagebox.showerror('Error', "Please enter your name!")
        return
    size = size_var.get()
    crust = crust_var.get()
    toppings = [topping for i, topping in enumerate(topping_opts) if topping_vars[i].get()]
    
    if not toppings:
        messagebox.showerror('Error', 'Please select at least one topping.')
        return
        
    # Create the order summary message
    message = f'Thanks for ordering, {name}! You ordered a {size} {crust} crust pizza with {", ".join(toppings)} toppings.'
    
    #Create a new window to display the output message
    output_window = tk.Toplevel(root)
    output_window.title('Order Summary')
 
    # Display the order summary message
    message_label = tk.Label(output_window, text=message)
    message_label.pack()

    # Add a button to close the output window
    close_button = tk.Button(output_window, text='Close', command=output_window.destroy)
    close_button.pack()

    # Set the size of the output window
    output_window.geometry('800x400')

def on_clear():
    '''To run when the user clicks the clear button'''
    name_inp.delete(0, tk.END)
    size_var.set('Small')
    crust_var.set('Thin')
    for topping_var in topping_vars:
        topping_var.set(False)
    output_line.configure(text='')

def on_about():
    '''To run when the user clicks the about button'''
    messagebox.showinfo('About', 'This is a pizza ordering system developed using Tkinter.')

def on_exit():
    '''To run when the user clicks the exit button'''
    if messagebox.askokcancel('Exit', 'Are you sure you want to exit?'):
        root.destroy()

# Create the root window
root = tk.Tk()
root.title('Pizza Ordering System')
root.geometry('800x600+300+300')
root.resizable(True, True)

# Add widgets to the window
title = tk.Label(root, text="Welcome to Kuku's Pizzera!", font=('Arial', 20),bg = 'yellow', fg = 'red', pady=10)

# Name information
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root)

# Size selection
size_label = tk.Label(root, text='What size pizza do you want?')
size_var = tk.StringVar(root, 'Small')
size_opts = ['Small', 'Medium', 'Large']
size_inp = tk.OptionMenu(root, size_var, *size_opts)

# Crust selection
crust_label = tk.Label(root, text='What type of crust do you want?')
crust_var = tk.StringVar(root, 'Thin')
crust_opts = ['Thin', 'Thick', 'Stuffed']
crust_inp = tk.OptionMenu(root, crust_var, *crust_opts)

# Toppings selection
toppings_label = tk.Label(root, text='Select your toppings:')
topping_vars = [tk.BooleanVar(root) for _ in range(8)]
topping_opts = ['Pepperoni', 'Mushrooms', 'Onions','Bellpepper','Tomatoes','Pineapple', 'Sausage', 'Bacon']
topping_chks = [tk.Checkbutton(root, text=opt, variable=topping_vars[i]) for i, opt in enumerate(topping_opts)]

# Submit button
submit_btn = tk.Button(root, text='Submit Order', command=on_submit)

# Clear button
clear_btn = tk.Button(root, text='Clear Form', command=on_clear)

# About button
about_btn = tk.Button(root, text='About', command=on_about)

# Exit button
exit_btn = tk.Button(root, text='Exit', command=on_exit)

# Output message
output_line = tk.Label(root, text='', anchor='w', justify='left', pady=10)
error_line = tk.Label(root, text='', anchor='w', justify='left', pady=10)
# Arrange widgets on the window
title.grid(row=0, column=0, columnspan=2)

# Name input
name_label.grid(row=1, column=0, sticky='w')
name_inp.grid(row=1, column=1, sticky='e')

# Size selection
size_label.grid(row=2, column=0, sticky='w')
size_inp.grid(row=2, column=1,sticky='e')

#crust selection
crust_label.grid(row=3, column=0, sticky='w')
crust_inp.grid(row=3, column=1, sticky='e')

#Toppings selection
toppings_label.grid(row=4, column=0, sticky='w')
for i, chk in enumerate(topping_chks):
    chk.grid(row=5+i//2, column=i%2)

#Submit button location
submit_btn.grid(row = 99, column=0, columnspan=1, sticky='NSEW')

#Exit Button Location
exit_btn.grid(row =100, column=0, columnspan=2, sticky='NSEW')

#About Button Location
about_btn.grid(row=0, column = 3, sticky ='NSEW')

#Clear Button Location
clear_btn.grid(row =99, column=1, columnspan=1, sticky='NSEW')

#error message location
error_line.grid(row=101,column=0)


root.mainloop()
