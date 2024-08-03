import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from User import *
from ExceptionClasses import *

Users = pd.read_csv('files/Users .csv',header=0, index_col='Username')
class Signup(EmptyFieldError,UsernameTakenError,User):
    def signup_page():

        def validate_signup(signup_window,name_entry,username_entry,password_entry):
            try:
                name = name_entry.get()
                userid = username_entry.get()
                password = password_entry.get()

                if name == "" or userid == "" or password == "":
                    raise EmptyFieldError()

                if userid in Users.index:
                    raise UsernameTakenError()

                new_user = User()
                new_user.create_user(name, userid, password)
                messagebox.showinfo("Registered", "Login to continue")
                signup_window.destroy()

            except (EmptyFieldError, UsernameTakenError) as e:
                messagebox.showerror("SignUp Failed", str(e))

        def display_signup():
            signup=Toplevel()
            signup.title("Sign Up")
            signup.geometry("800x800")

            #SignUp Frame
            frame= LabelFrame(signup, text="Sign Up Here", padx=100, pady=100)
            frame.pack(padx=50,pady=100)
            name_var=tk.StringVar()
            passw_var=tk.StringVar()
            
            #User's full Name
            name_label = tk.Label(frame, text="Enter your full Name")
            name_label.pack()

            name_entry = tk.Entry(frame,textvariable = name_var)
            name_entry.pack()

            # Create and place the username label and entry
            username_label = tk.Label(frame, text="Enter Username",pady=10)
            username_label.pack()

            username_entry = tk.Entry(frame)
            username_entry.pack()

            # Create and place the password label and entry
            password_label = tk.Label(frame, text="Enter Password",pady=10)
            password_label.pack()

            password_entry = tk.Entry(frame, show="*",textvariable = passw_var)  # Show asterisks for password
            password_entry.pack()

            # Create and place the signup button
            signup_button = tk.Button(frame, text="SignUp", command=lambda: validate_signup(signup,name_var,username_entry,passw_var),padx=42,bg='Light Blue')
            signup_button.pack()
        display_signup()
