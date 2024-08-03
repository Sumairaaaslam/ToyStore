import pandas as pd

class Product:
    def __init__(self):
        self.product_df = pd.read_csv('files/Products.csv')

    def add_item(self,id,name,img,price):
        new_product={'Item_id':id,'Item Name':name,'Item Image':img,'Item Price':price}
        self.product_df=self.product_df._append(new_product,ignore_index=True)
        self.product_df.to_csv('files/Products.csv', index=False)

    
        












#Add item Code