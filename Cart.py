import pandas as pd
from datetime import date

class Cart:
    orders_df = pd.read_csv('files/Orders.csv',header=0)
    try:
        last_order_id=orders_df.iloc[-1]['Orderid']
    except:
        last_order_id=0
    
    order_id=int(last_order_id)+1 
    
    def __init__(self,username):
        self.username=username
        self.items=[]
        self.order_id=Cart.order_id 


    def add_item(self,items):
        for i in range(len(items)):
            self.items.append([items[i],1])


    def add_quantity(self,item_no):
        for i in range(len(self.items)):
            if self.items[i][0]==item_no:
                self.items[i][1]+=1
                break

    def sub_quantity(self,item_no):
        for i in range(len(self.items)):
            if self.items[i][0]==item_no:
                self.items[i][1]-=1
                break

    def remove_item(self,item_no):
        for i in range(len(self.items)):
            if self.items[i][0]==item_no:
                self.items.remove(self.items[i])
                break


    def save_order(self):
        for i in range(len(self.items)):
            order_item={'Orderid':self.order_id,'Username':self.username,'Item_id':self.items[i][0],'Quantity':self.items[i][1],'Date':date.today().strftime("%B %d, %Y")}
            Cart.orders_df=Cart.orders_df._append(order_item, ignore_index=True)
            Cart.orders_df.to_csv('files/Orders.csv',index=False)


    
