import tkinter as tk

def topping():
    return True
    
def on_submit():
    '''To run when the user submits the form'''
    # Get user inputs
    name = name_inp.get()
    size = size_var.get()
    crust = crust_var.get()
    toppings = [topping_opts[i] for i, topping in enumerate(topping_vars) if topping.get()]
    
    # Create the order summary message
    message = f'Thanks for ordering, {name}! You ordered a {size} {crust} crust pizza with {", ".join(toppings)} toppings.'
    output_line.configure(text=message)
# Create the root window
root = tk.Tk()
root.title('Pizza Ordering System')
root.geometry('800x600+300+300')
root.resizable(True, True)

# Add widgets to the window
title = tk.Label(root, text='Welcome to our Pizza Ordering System!', font=('Arial', 20), pady=10)

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
topping_opts = ['Pepperoni', 'Mushrooms','BellPepper','Tomatoes', 'Onions','Pineapple', 'Sausage', 'Bacon']
topping_chks = [tk.Checkbutton(root, text=opt, variable=topping_vars[i]) for i, opt in enumerate(topping_opts)]

# Submit button
submit_btn = tk.Button(root, text='Submit Order', command=on_submit)

# Output message
output_line = tk.Label(root, text='', anchor='w', justify='left', pady=10)

# Arrange widgets on the window
title.grid(row=0, column=0, columnspan=2)

# Name input
name_label.grid(row=1, column=0, sticky='w')
name_inp.grid(row=1, column=1, sticky='e')

# Size selection
size_label.grid(row=2, column=0, sticky='w')
size_inp.grid(row=2, column=1, sticky='e')

# Crust selection
crust_label.grid(row=3, column=0, sticky='w')
crust_inp.grid(row=3, column=1, sticky='e')

# Toppings selection
toppings_label.grid(row=4, column=0, sticky='w')
for i, chk in enumerate(topping_chks):
    chk.grid(row=5+i//2, column=i%2)

# Submit button
submit_btn.grid(row=99, column=0, columnspan=2)

# Output message
output_line.grid(row=100, column=0, columnspan=2, sticky='NSEW')

root.mainloop()
