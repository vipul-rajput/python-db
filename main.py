import psycopg2
from config import config
from insert import insert_category, insert_product

print("*********Jio Stores*********")

print("Select the Option")
ch = int(input("1. Insert Category\n2. Insert Product\n"))
if ch==1:
    temp_cat = input("Enter Category")
    insert_category(temp_cat)
if ch==2:
    temp_prod_cat = int(input("Enter Category Id in which you want to insert: "))
    temp_prod_name = input("Enter Product Name: ")
    temp_prod_price = int(input("Enter Product Price: "))
    insert_product(product_name= temp_prod_name, category_ID= temp_prod_cat, product_price= temp_prod_price)
    # insert_product(temp_prod_name, temp_prod_price, temp_prod_cat)
