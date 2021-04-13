#!/usr/bin/python

import psycopg2
from config import config


def insert_category(category_name):
    """ insert a new category into the categorys table """
    sql = """INSERT INTO categories(category_name)
             VALUES(%s) RETURNING category_ID;"""
    conn = None
    category_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (category_name,))
        # get the generated id back
        category_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return category_id

def insert_product(product_name, category_ID, product_price):
    """ insert a new product into the products table """
    sql = """INSERT INTO products(product_name, category_ID, product_price)
             VALUES(%s, %s, %s) RETURNING product_id;"""
    conn = None
    product_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (product_name,category_ID, product_price))
        # get the generated id back
        product_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return product_id
def insert_product_list(product_list):
    """ insert multiple products into the products table  """
    sql = "INSERT INTO products(product_name, category_ID, product_price) VALUES(%s, %s, %s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,product_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
def add_order( order_by_name, order_quantity, order_product_id, order_total_price):
    """ insert a new order into the orders table """
    sql = """INSERT INTO orders(  order_by_name, order_quantity, order_product_id, order_total_price)
             VALUES ( %s, %s, %s, %s) RETURNING order_ID;"""
    conn = None
    order_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, ( order_by_name, order_quantity, order_product_id, order_total_price))
        # get the generated id back
        product_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return order_id

if __name__ == '__main__':
    # insert one product
     
    add_order( order_by_name='kp', order_quantity=1, order_product_id=1, order_total_price=290)
 