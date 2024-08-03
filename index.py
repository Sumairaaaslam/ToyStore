import tkinter as tk
from tkinter import *
from login_page import *

#Creating the Parent Window
parent = tk.Tk()
parent.title("Toy Store")
parent.geometry("950x950")

# Login window
login_window = tk.Frame(parent)

# Products window
products_window = tk.Frame(parent)

# Initially hide the products window
products_window.pack_forget()

#Display login_page
Login.login_page(login_window,products_window)

# Start the Tkinter event loop
parent.mainloop()
