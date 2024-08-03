import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
from shopping_history import History

class Checkout:
    items_df = pd.read_csv('files/Items.csv', header=0)

    def checkout(cart_item_quantity, order_id):
        orders_df = pd.read_csv('files/Orders.csv', header=0)
        checkout_win = Toplevel()
        checkout_win.title("Checkout")
        checkout_win.geometry("400x400")

        # Create a frame for the header
        header_frame = tk.Frame(checkout_win)
        header_frame.pack(side=tk.TOP, fill=tk.X)

        # Header label
        header_label = tk.Label(header_frame, text="Checkout", font=("Arial", 16))
        header_label.pack(side=tk.LEFT, padx=10)

        # EXIT LINK
        exit_link = tk.Label(header_frame, text="Exit", font=("Arial", 12), fg="blue", cursor="hand2")
        exit_link.pack(side=tk.RIGHT, padx=10)
        from products_page import Products_Display
        exit_link.bind("<Button-1>", lambda event: (Products_Display.exit()))

        # SHOPPING HISTORY LINK
        history_link = tk.Label(header_frame, text="Shopping History", font=("Arial", 12), fg="blue", cursor="hand2")
        history_link.pack(side=tk.RIGHT, padx=10)
        history_link.bind("<Button-1>", lambda event: (History.show_history(order_id)))

        # Create a frame to contain both the canvas and the label
        canvas_frame = tk.Frame(checkout_win)
        canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a canvas to contain the frames
        canvas = tk.Canvas(canvas_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add scrollbar
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        # Configure canvas scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Function to update scrollregion when canvas resized
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_configure)

        # Create a frame to hold all the frames
        frame_container = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_container, anchor="nw")

        # Creating Frame for each product
        my_order = orders_df[orders_df['Orderid'] == order_id]
        items = list(my_order["Item_id"])
        quantity = list(my_order["Quantity"])
        total_price = 0

        for i in range(len(items)):
            frame = tk.LabelFrame(frame_container, padx=20, pady=20)
            frame.grid(row=i, column=0, columnspan=3)

            image_path = list(Checkout.items_df['Item Image'][Checkout.items_df['Item_id'] == items[i]])
            image = Image.open(image_path[0])
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(frame, image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack(side=tk.LEFT)  # Pack the image label on the left

            image_label = list(Checkout.items_df['Item Name'][Checkout.items_df['Item_id'] == items[i]])
            item_name_label = tk.Label(frame, text=image_label[0], font=("Arial", 16))
            item_name_label.pack(side=tk.TOP)  # Pack the item name label on the top

            quantity_label = tk.Label(frame, text=f"Quantity: {quantity[i]}")
            quantity_label.pack(side=tk.TOP)

            price = list(Checkout.items_df['Item Price'][Checkout.items_df['Item_id'] == items[i]])
            price_label = tk.Label(frame, text=f"Price: {price[0] * quantity[i]}")
            price_label.pack(side=tk.TOP)

            total_price += price[0] * quantity[i]

        # Display total price
        total_price_label = tk.Label(checkout_win, text=f"Total Price: {total_price}", font=("Arial", 16))
        total_price_label.pack(side=tk.BOTTOM, pady=10)

        checkout_win.mainloop()
