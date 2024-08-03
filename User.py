import pandas as pd
from Cart import *
from datetime import date

class User:
    users_df = pd.read_csv('files/Users .csv')
    

    #Called after successful signup
    def create_user(self, name, username, pwd):
        self.name=name
        self.username=username
        self.pwd=pwd
        new_user = {'Name': name, 'Username': username, 'Password': pwd}
        User.users_df = User.users_df._append(new_user, ignore_index=True)
        User.users_df.to_csv('files/Users .csv', index=False)  # Update the CSV file

    #Called after successful login
    def current_user(self,username):
        self.username=username
        self.cart=[]#Nested list with item and quantity
        self.date=date.today()

    def show_user_details(self):
        user_data = User.users_df.loc[len(self.users_df.index)-1]
        print("Name:", user_data['Name'])
        print("Username:", user_data['Username'])
        print("Password:", user_data['Password'])


    def create_cart(self):
        self.cartInstance=Cart(self.username)
        self.cartInstance.add_item(self.cart)

        return self.cartInstance
