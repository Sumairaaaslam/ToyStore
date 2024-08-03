import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from view_cart import *
import sys

items = pd.read_csv('files/Items.csv', header=0, index_col='Item_id')

class Products_Display:

    def product_display(current_session,login_window, parent_prod):
        login_window.pack_forget()

        # Show the products window
        parent_prod.pack(fill=tk.BOTH, expand=True)

        # Function to create a label with an image and price
        def create_image_label(parent_frame, image_path, price):
            image = Image.open(image_path)
            image = image.resize((250, 250))
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(parent_frame, image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack()
            # Price label
            price_label = tk.Label(parent_frame, text=f"Price: {price}", font=("Arial", 12))
            price_label.pack()

        # Function to change button text to "Added to Cart" and disable it
        def added(button, item_no):
            button.config(text="Added to Cart!", state=tk.DISABLED, bg="Black", fg="White")
            current_session.cart.append(item_no + 1)

        # Frame for the header
        header_frame = tk.Frame(parent_prod)
        header_frame.pack(side=tk.TOP, fill=tk.X)

        # Header label
        header_label = tk.Label(header_frame, text="Toy Store", font=("Arial", 16))
        header_label.pack(side=tk.LEFT, padx=10)

        view_cart_link = tk.Label(header_frame, text="View Cart", font=("Arial", 12), fg="blue", cursor="hand2")
        view_cart_link.pack(side=tk.RIGHT, padx=10)
        view_cart_link.bind("<Button-1>", lambda event: (view_cart(current_session)))

        # Create a frame to contain both the canvas and the label
        canvas_frame = tk.Frame(parent_prod)
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

        # Create frames
        image_paths = list(items['Item Image'])

        buttons = []

        for index, image_path in enumerate(image_paths):
            row = index // 3
            col = index % 3

            frame = tk.LabelFrame(frame_container, text=items.loc[index + 1]["Item Name"], padx=20, pady=20)
            frame.grid(row=row, column=col)
            create_image_label(frame, image_path, items.loc[index + 1]["Item Price"])
            button = tk.Button(frame, text="Add to Cart", padx=5, pady=5, bg="Gray", width=35)
            button.config(command=lambda btn=button, btn_index=index: added(btn, btn_index))
            button.pack(ipadx=10, ipady=5)
            buttons.append(button)

        # Footer label
        footer_label = tk.Label(parent_prod, text="TOY STORE", font=("Arial", 16))
        footer_label.pack(side=tk.TOP, pady=10)

        #Tkinter event loop
        parent_prod.mainloop()

    def exit():
        sys.exit(1)
