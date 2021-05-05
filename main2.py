import psycopg2
from display import *
from config import config
from insert import *
from tkinter import *
from delete import *

  
def Main():
    class Table:
        def __init__(self,root):
            
            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    
                    self.e = Entry(root, width=20, fg='black',
                                font=('Arial',16,'bold'))
                    
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst2[i][j])
    while True:
        print("\n\nSelect the Option")
        ch = int(input("1. Categories\n2. Products\n3. Orders \n4. Exit\n\n"))
        if ch==1:
            print("***Category***")
            ch1 = int(input(("1. Add Category\n2. Show Category \n3. Delete Category\n4. Exit\n\n")))
            if(ch1==1):
                print("Add Categories")
                temp_cat = input("Enter Category Name :")
                insert_category(temp_cat)
            if(ch1==2):
                lst2 = get_categories()
                print(lst2)  
                total_rows = len(lst2)
                total_columns = len(lst2[0])
                root = Tk()
                t = Table(root)
                root.mainloop()
            if(ch1==3):
                print('Delete Category')
                print(get_categories())
                delete_category(int(input("Enter Category ID to delete: ")))

            if(ch1==4):
                Main()
        if ch==2:
            print("\n\n***Products***")
            ch1 = int(input(("1. Add Product\n2. Show Products\n3. Delete Product\n4. Exit\n\n")))
            if(ch1==1):
                print("Add Product")
                print(get_categories())
                temp_prod_cat = int(input("Enter Category Id in which you want to insert: "))
                temp_prod_name = input("Enter Product Name: ")
                temp_prod_price = int(input("Enter Product Price: "))
                insert_product(product_name= temp_prod_name, category_ID= temp_prod_cat, product_price= temp_prod_price)

            if(ch1==2):
                lst2 = get_products()
                print(lst2)  
                total_rows = len(lst2)
                total_columns = len(lst2[0])
                root = Tk()
                t = Table(root)
                root.mainloop()
            if(ch1==3):
                print('Delete Product')
                print(get_products())
                delete_products(int(input("Enter Product ID to delete: ")))
            if(ch1==4):
                Main()
        if(ch==3):
            print("\n\n***Orders***")
            ch1 = int(input(("1. Add Order\n2. Show Orders\n3. Exit\n\n")))
            if(ch1==1):
                add_order(input('Customer Name : '), int(input('Order quantity : ')), int(input('Order Product Id : ')), int(input('Total Price :')))
            if(ch1==2):
                lst2 = get_orders()
                print(lst2)  
                total_rows = len(lst2)
                total_columns = len(lst2[0])
                root = Tk()
                t = Table(root)
                root.mainloop()

            if(ch1==4):
                Main()
        if(ch==4):
            print("Thank You!")
            break

print("*********Jio Stores*********")
Main()
