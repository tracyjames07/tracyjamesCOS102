import tkinter as tk 
from tkinter import messagebox
from tkinter import *
import pyglet

pyglet.font.add_file("C:\\Users\\there\\OneDrive\\Desktop\\tracyjamesCOS102\\CA 2\\CormorantGaramond-Regular.ttf")

def calculate():
        selected_menu = order_var.get()
        quantity = int(portion_var.get())
        price = order[selected_menu]

        prices.append(price)
        quantities.append(quantity) 

        final_price = 0

        print(quantities)
        print(prices)

        for i in range(len(prices)):
             total = quantities[i] * prices[i]
             final_price += total
             print(total)
                     
        if final_price < 2500:
             final_price = final_price * 0.9
             messagebox.showinfo("Discount", f"Your have a 10% discount. Your total is ₦{final_price}.")
        elif final_price > 2500 and final_price < 5000:
             final_price = final_price * 0.85
             messagebox.showinfo("Discount", f"You have a 15% discount. Your total is ₦{final_price}.")
        elif final_price > 5000:
             final_price = final_price * 0.75
             messagebox.showinfo("Discount", f"You have a 25% discount. Your total is ₦{final_price}.")
        elif final_price < 1000:
             messagebox.showinfo("No Discount", f"You don't have a discount. Your total is ₦{final_price}.")
        else:
             messagebox.showerror("Error", "It seems like there is a problem with your input.")
        
def landing():
    messagebox.showinfo("PAU Cafeteria", "Welcome to the PAU Cafeteria.")

a = "#4169E1"
b = "#FFFFFF"
c = "#000000"

home = tk.Tk()
home.title("PAU Cafeteria")
home.geometry("400x200")
home.config(bg = a)

welcome = tk.Label(home, text = "Welcome to the 'PAU Cafeteria'! \nYour one stop for an assortment of foods and drinks. \nHave a look at our menu and place an order if you'd like.",
                   font = ('Cormorant Garamond', 12))
welcome.pack()
welcome.config(fg = b, bg = a)

gap = tk.Label(home, text = "")
gap.pack()
gap.config(bg = a)

def catalogue():
    home.destroy()
    
    menu = tk.Tk()
    menu.title("Cafeteria Menu")
    menu.geometry("600x600")
    menu.config(bg = a)

    left_menu = tk.Frame(menu, width = 300, height = 300)
    left_menu.pack(side = tk.LEFT, fill = tk.Y, padx = 50, pady = 20)
    left_menu.config(bg = a)

    right_menu = tk.Frame(menu, width = 300, height = 300)
    right_menu.pack(side = tk.RIGHT, fill = tk.Y, padx = 50, pady = 20)
    right_menu.config(bg = a)

    header = tk.Label(left_menu, text = "MENU", width = 10, height = 2,
                      font = ('Cormorant Garamond', 20, 'bold'))
    header.config(fg = b, bg = a)
    header.pack()

    rice_pasta = tk.Label(left_menu, text = "RICE/PASTA \nJollof Rice      350 \nCoconut Fried Rice      350 \nJollof Spaghetti      350",
                          font = ('Cormorant Garamond', 12))
    rice_pasta.config(fg = b, bg = a)
    rice_pasta.pack()

    side_dishes = tk.Label(left_menu, text = "SIDE DISHES \nSavoury Beans    350 \nRoasted Sweet Potatoes    350 \nFried Plantains   150 \nMixed Vegetable Salad     150 \nBoiled Yam    150",
                           font = ('Cormorant Garamond', 12))
    side_dishes.config(fg = b, bg = a)
    side_dishes.pack()

    soups_swallows = tk.Label(left_menu, text = "SOUPS & SWALLOWS \nEba      100 \nPoundo Yam      100 \nSemo      100 \nAtama Soup      450 \nEgusi Soup      480",
                              font = ('Cormorant Garamond', 12))
    soups_swallows.config(fg = b, bg = a)
    soups_swallows.pack()

    proteins = tk.Label(right_menu, text = "PROTEINS \nSweet Chili Chicken    1100 \nGrilled Chicken Wings    400 \nFried Beef    400 \nFried Fish    500 \nBoiled Egg    200 \nSautéed Sausages      200",
                         font = ('Cormorant Garamond', 12))
    
    proteins.config(fg = b, bg = a)
    proteins.pack()

    beverages = tk.Label(right_menu, text = "BEVERAGES \nWater    200 \nGlass Drink (35 cl)   150 \nPET Drink (35 cl)     300 \nPET Drink (50 cl)     350 \nGlass/Canned Malt     500 \nFresh Yo    600 \nPineapple Juice     350 \nMango Juice   350 \nZobo Drink    350",
                          font = ('Cormorant Garamond', 12))
    beverages.config(fg = b, bg = a)
    beverages.pack()

    footer = tk.Label(right_menu, text = "ENJOY!",
                      font = ('Cormorant Garamond', 12, 'bold'))
    footer.config(fg = b, bg = a)
    footer.pack()

    menu_gap = tk.Label(right_menu, text = "")
    menu_gap.pack()
    menu_gap.config(bg = a)
    def meal():

        def add_to_cart():
            calc.destroy()
            selected_menu = order_var.get()
            quantity = int(portion_var.get())
            price = order[selected_menu]

            prices.append(price)
            quantities.append(quantity) 

            messagebox.showinfo("cart", f"{quantity} portion(s) of {selected_menu} has been added to cart.")      

        calc = tk.Tk()
        calc.title("Order and Checkout")
        calc.geometry("600x600")
        calc.config(bg = a)

        order_label = tk.Label(calc, text = "SELECT YOUR ORDER", 
                               font = ('Cormorant Garamond', 12))
        order_label.pack()
        order_label.config(fg = b, bg = a)

        global order
        
        order = { 
            "NULL": 0, 
            "Jollof Rice": 350,
            "Coconut Fried Rice": 350,
            "Jollof Spaghetti": 350,
            "Savoury Beans": 350, 
            "Roasted Sweet Potatoes": 300, 
            "Fried Plantains": 150, 
            "Mixed Vegetable Salad": 150, 
            "Boiled Yam": 150, 
            "Eba": 100, 
            "Poundo Yam": 100, 
            "Semo": 100, 
            "Atama Soup": 450, 
            "Egusi Soup": 480,
            "Sweet Chili Chicken": 1100, 
            "Grilled Chicken Wings": 400, 
            "Fried Beef": 150, 
            "Boiled Egg": 200, 
            "Sautéed Sausages": 200, 
            "Water": 200, 
            "Glass Drink (35 cl)": 150, 
            "PET Drink (35 cl)": 300, 
            "PET Drink (50 cl)": 350, 
            "Glass/Canned Malt": 500, 
            "Fresh Yo": 600, 
            "Pineapple Juice": 350, 
            "Mango Juice": 350, 
            "Zobo Drink": 350
        }

        global order_var
        global portion_var

        order_var = tk.StringVar(calc)
        order_options = list(order.keys())
        order_options.append("")
        order_var.set(order_options[0]) 

        order_list = tk.OptionMenu(calc, order_var, *order_options)
        order_list.config(width = 30, 
                          font = ('Cormorant Garamond', 12), bg = b)
        order_list.pack()

        portion = tk.Label(calc, text = "HOW MANY PORTIONS WILL YOU BE GETTING?", 
                           font = ('Cormorant Garamond', 12))
        portion.pack()
        portion.config(bg = a, fg = b)

        portion_var = tk.StringVar(calc)
        portion_options = list(range(1, 7))
        portion_var.set(portion_options[0])

        portion_list = tk.OptionMenu(calc, portion_var, *portion_options)
        portion_list.config(width = 10, 
                            font = ('Cormorant Garamond', 12), bg = b)
        portion_list.pack()

        add_order_label = tk.Label(calc, text = "")
        add_order_label.pack()
        add_order_label.config(bg = a)

        add_order = tk.Button(calc, text = "Add to Order", command = add_to_cart, 
                              font = ('Cormorant Garamond', 11))
        add_order.pack()
        add_order.config(fg = c, bg = b)

        checkout_label = tk.Label(calc, text = "")
        checkout_label.pack()
        checkout_label.config(bg = a)

        checkout = tk.Button(calc, text = "Checkout", command = calculate, 
                             font = ('Cormorant Garamond', 11))
        checkout.pack()
        checkout.config(fg = c, bg = b)

        global total
        global total_price

        total = []
        total_price = sum(total)
        
    proceed = tk.Button(right_menu, text = "Proceed", command = meal, 
                        font = ('Cormorant Garamond', 11))
    proceed.pack()
    proceed.config(fg = c, bg = b)

    global prices
    global quantities
    prices = []
    quantities = []

    menu.mainloop()

proceed = tk.Button(home, text = "Proceed", command = catalogue, 
                    font = ('Cormorant Garamond', 11))
proceed.pack()
proceed.config(fg = c, bg = b)

home.mainloop()