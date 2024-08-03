import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from Cart import *
from checkout import *
from checkout import Checkout

items={
        1:['White Bear',"images/bear_1.jpg",1], 2:['Brown Bear', "images/bear_2.jpg",1],
        3:['Large Pillow',"images/pillow_3.jpg",1 ], 4:['Cat Plushie', "images/cat_4.jpg",1 ],
        5:['Banana Plush Toy',"images/banana_5.jpg",1 ], 6:['Potato',"images/potato_6.jpg",1 ],
        7:['Goose', "images/duck_7.jpg",1], 8:['Teddy', "images/bear_8.jpg",1],
        9:['Panda',"images/panda_9.jpg",1 ], 10:['Bunny', "images/bunny_10.jpg",1 ],
        11:['Totoro',"images/totoro_11.jpg",1 ], 12:['Dino',"images/dino_12.jpg",1]
        }

cart_item_quantity={}

def view_cart(current_session):
    cart_items=current_session.cart
    cart=Toplevel()
    cart.title("Cart")
    cart.geometry("800x800")

    #Create an object for Cart
    user_cart=current_session.create_cart()
    order_id=user_cart.order_id 


    # Create a frame for the header
    header_frame = tk.Frame(cart)
    header_frame.pack(side=tk.TOP, fill=tk.X)

    # Header label
    header_label = tk.Label(header_frame, text="Cart", font=("Arial", 16))
    header_label.pack(side=tk.LEFT, padx=10)

    #CHECKOUT LINK
    checkout_link = tk.Label(header_frame, text="Checkout", font=("Arial", 12), fg="blue", cursor="hand2")
    checkout_link.pack(side=tk.RIGHT, padx=10)
    checkout_link.bind("<Button-1>", lambda event: (user_cart.save_order(),cart.destroy(),Checkout.checkout(cart_item_quantity,order_id)))

    #cONTINUE sHOPPING lINK
    continue_shopping_link = tk.Label(header_frame, text="Continue Shopping", font=("Arial", 12), fg="blue", cursor="hand2")
    continue_shopping_link.pack(side=tk.RIGHT, padx=10)
    continue_shopping_link.bind("<Button-1>", lambda event: cart.destroy())

    
    # Create a frame to contain both the canvas and the label
    canvas_frame = tk.Frame(cart)
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

    #Creating Frame for each product
    for index, item_no in enumerate(cart_items):
        cart_item_quantity[item_no]=1 #initializa quantity with 1
        frame = tk.LabelFrame(frame_container, padx=20, pady=20)
        frame.grid(row=index, column=0, columnspan=3)
        
        # Load and resize the image
        image = Image.open(items[item_no][1])
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        
        # Create label for the image
        label = tk.Label(frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack(side=tk.LEFT)  # Pack the image label on the left
        
        # Create label for the item name
        item_name_label = tk.Label(frame, text=items[item_no][0],font=("Arial", 16))
        item_name_label.pack(side=tk.TOP)  # Pack the item name label on the top
        
        # Function to handle removal of item from cart
        def remove_item(frame,item):
            global cart_item_quantity
            cart_items.remove(item)
            del cart_item_quantity[item]
            user_cart.remove_item(item)
            # Update the UI to reflect the removal of the item from the cart
            frame.destroy()  # Destroy the frame containing the removed item
        
        # Create label for the "Remove Item" link
        remove_link = tk.Label(frame, text="Remove Item", fg="blue", cursor="hand2")
        remove_link.pack(side=tk.TOP)  # Pack the link label on the top
        # Bind the link label to the function that removes the item
        remove_link.bind("<Button-1>", lambda event,frame=frame, item=item_no: remove_item(frame,item))

        # Label for Quantity
        quantity_label = tk.Label(frame, text="Quantity:")
        quantity_label.pack(side=tk.TOP)

        def add_quantity(item_no, quantity_display):
            global items
            global cart_item_quantity
            cart_item_quantity[item_no]+=1
            items[item_no][2] += 1
            user_cart.add_quantity(item_no)
            quantity_display.config(text=items[item_no][2])


        def sub_quantity(item_no, quantity_display):
            global items
            if items[item_no][2] > 1:
                items[item_no][2] -= 1
                cart_item_quantity[item_no]-=1
                quantity_display.config(text=items[item_no][2])
                user_cart.sub_quantity(item_no)


     

        #Label for Qunatity Display
        quantity_display = tk.Label(frame, text=items[item_no][2])  # Initial quantity is 1
        quantity_display.pack(side=tk.LEFT)

        # Plus button
        plus_button = tk.Button(frame, text="+", command=lambda item_no=item_no, qd=quantity_display: add_quantity(item_no, qd))
        plus_button.pack(side=tk.LEFT)
        
        # Minus button
        minus_button = tk.Button(frame, text="-", command=lambda item_no=item_no, qd=quantity_display: sub_quantity(item_no, qd))
        minus_button.pack(side=tk.LEFT)
    

    cart.mainloop()


