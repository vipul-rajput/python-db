#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
         CREATE TABLE categories (
          category_ID int GENERATED ALWAYS AS IDENTITY,
          category_name VARCHAR(255) not null,
          primary key(category_ID));
        """
       ,
         """
        CREATE TABLE products (
            product_ID int GENERATED ALWAYS AS IDENTITY,
            product_name VARCHAR(255) NOT NULL,
            category_ID int not null,
            product_price INT ,
            primary key (product_id),
            foreign key (category_ID) references categories(category_ID) on delete cascade);
        """,
     """  CREATE TABLE orders(
           order_ID int GENERATED ALWAYS AS IDENTITY,
           order_date_time timestamp default current_timestamp,
           order_by_name VARCHAR(255) not null,
           order_quantity int not null,
           order_product_id int not null,
           order_total_price int not null,
           foreign key(order_product_id) references products(product_ID) on delete cascade,
           primary key(order_ID));

       """
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()