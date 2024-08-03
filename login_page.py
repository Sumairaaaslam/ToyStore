import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from signup import *
from products_page import *
from ExceptionClasses import *
from User import *

class Login(EmptyFieldError,IncorrectPasswordError,InvalidUsernameError,User):
    def login_page(login_window,products_window):        
        def validate_login(username_entry, password_entry):
            try:
                # Importing the Users file
                Users = pd.read_csv('files/Users .csv', header=0, index_col='Username')

                userid = username_entry.get()
                password = password_entry.get()

                if userid == "" or password == "":
                    raise EmptyFieldError()

                if userid not in Users.index:
                    raise InvalidUsernameError()

                pwd = Users.loc[userid]["Password"]
                if password != pwd:
                    raise IncorrectPasswordError()

                # If no exceptions are raised, login is successful
                messagebox.showinfo("Login Successful", "Welcome!")

                #Creating User Object
                current_session=User()
                current_session.current_user(userid)

                '''Move to products_page.py'''
                Products_Display.product_display(current_session,login_window, products_window)

                
            except (EmptyFieldError, InvalidUsernameError, IncorrectPasswordError) as e:
                messagebox.showerror("Login Failed", str(e))

        
        #Display login window
        def display_login():
            login_window.pack()

            #Login Frame
            frame= LabelFrame(login_window, text="Login Here", padx=100, pady=100)
            frame.pack(padx=50,pady=100)

            # Create and place the username label and entry
            username_label = tk.Label(frame, text="Username")
            username_label.pack()

            username_entry = tk.Entry(frame)
            username_entry.pack()

            # Create and place the password label and entry
            password_label = tk.Label(frame, text="Password",pady=10)
            password_label.pack()

            password_entry = tk.Entry(frame, show="*")  # Show asterisks for password
            password_entry.pack()

            # Create and place the login button
            login_button = tk.Button(frame, text="Login", command=lambda: validate_login(username_entry,password_entry),padx=42,bg='Light Blue')
            login_button.pack()

            #SignUp
            no_account_label = tk.Label(frame, text="Don't have an account?",pady=10)
            no_account_label.pack()

            signup_page_button = tk.Button(frame, text="SignUp", command=Signup.signup_page,padx=42)
            
            '''Move to signup.py'''
            signup_page_button.pack()

            
        display_login()
        login_window.mainloop()