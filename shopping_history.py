import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pandas as pd

class History:
    
    def show_history(order_id):
        orders_df = pd.read_csv('files/Orders.csv')
        items_df = pd.read_csv('files/Items.csv')

        orders_df['Item_id'] = orders_df['Item_id'].astype(int)
        items_df['Item_id'] = items_df['Item_id'].astype(int)
        

        # Merge the DataFrames on the Item_id column
        merged_df = pd.merge(orders_df, items_df, on='Item_id')
        try:
            username = merged_df.loc[merged_df['Orderid'] == order_id, 'Username'].iloc[0]
            user_orders = merged_df[merged_df['Username'] == username]
            
            # Total price for each order
            user_orders['Total Price'] = user_orders['Quantity'] * user_orders['Item Price']
            
            # Total price for each Orderid
            order_totals = user_orders.groupby('Orderid')['Total Price'].sum().reset_index()
            
            order_history_window=Toplevel()
            order_history_window.title("Shopping History")
           
            
            # Treeview to display the order details
            columns = ['Orderid', 'Item Name', 'Item Price', 'Quantity','Date', 'Total Price']
            tree = ttk.Treeview(order_history_window, columns=columns, show='headings')
            
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, anchor=tk.CENTER)
            
            # Insert data into the treeview
            for _, row in user_orders.iterrows():
                tree.insert("", "end", values=(row['Orderid'], row['Item Name'], row['Item Price'], row['Quantity'],row['Date'], row['Total Price']))
            
            # Show total price for each Orderid
            total_label = tk.Label(order_history_window, text="Total Prices for Each Order:")
            total_label.pack(pady=10)
            
            for _, row in order_totals.iterrows():
                tk.Label(order_history_window, text=f"Order ID {row['Orderid']}: {row['Total Price']}").pack()
            
            tree.pack(fill='both', expand=True)
        except IndexError:
            messagebox.showerror("Error", "Order ID not found")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        order_history_window.mainloop()
