import psycopg2
from config import config


def get_products():

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select products.product_id, categories.category_name, products.product_name, products.product_price from products left join categories on products.category_id=categories.category_id;"
)
        row = cur.fetchone()
        productList = []
        columnNames = ('Product ID', 'Product Category', 'Product Name', 'Price')
        productList.append(columnNames)
        while row is not None:
            productList.append(row)
            row = cur.fetchone()
        return productList
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_categories():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select * from categories")
        row = cur.fetchone()
        categoryList = []
 #       columnNames = ('Product ID', 'Product Category', 'Product Name', 'Price')
        columnNames = ('Category Id', 'Category Name')
        categoryList.append(columnNames)
        print(categoryList)
        while row is not None:
            categoryList.append(row)
            row = cur.fetchone()
        return categoryList
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_orders():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(" select orders.order_id, orders.order_date_time, orders.order_by_name, products.product_name, products.product_price, orders.order_quantity, orders.order_total_price from orders full outer join products on orders.order_product_id= products.product_id where orders.order_product_id= products.product_id")
        row = cur.fetchone()
        orderList = []
        while row is not None:
            orderList.append(row)
            row = cur.fetchone()
        return orderList
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    print(get_products())
  