import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(database='inventory_system', user='postgres', password='vivek9484', host='localhost',
                            port='5432')
        return conn
    except Exception as e:
        print(e)

def view_products():
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute('select * from products')
        rows = cur.fetchall()
        for row in rows:
            print(f'product_id = {row[0]}, Name = {row[1]}, quantity = {row[3]}, price = {row[4]}')
        cur.close()
        conn.close()

def add_new_product():
    conn = get_connection()
    if conn:
        name = input('Enter name of the Product: ')
        description = input('Enter product description: ')
        qty = int(input('Enter Quantity: '))
        price = float(input('Enter Price: '))
        cur = conn.cursor()
        cur.execute('insert into products (name, description, quantity, unit_price) values (%s, %s, %s, %s)', (name, description, qty, price))
        conn.commit()
        print(f'product {name} added successfully.')
        cur.close()
        conn.close()

def update_quantity():
    conn = get_connection()
    if conn:
        product_id = int(input("Enter the product id: "))
        sign = input('Want to (increase/decrease): ')
        cur = conn.cursor()
        if sign == 'increase':
            n_qty = int(input("Enter the Quantity to Increase: "))
            update_query = 'update products set quantity= quantity + %s where id= %s'
            cur.execute(update_query, (n_qty, product_id))
        elif sign == 'decrease':
            n_qty = int(input("Enter the Quantity to Decrease: "))
            update_query = 'update products set quantity= quantity - %s where id= %s'
            cur.execute(update_query, (n_qty, product_id))
        conn.commit()
        print(f'Product ID {product_id} quantity updated.')
        cur.close()
        conn.close()

def remove_product():
    conn = get_connection()
    if conn:
        product_id = int(input('Enter product id to remove product: '))
        cur = conn.cursor()
        delete_query = 'delete from products where id=%s'
        cur.execute(delete_query, [product_id])
        conn.commit()
        print(f'Product ID {product_id} deleted successfully.')
        cur.close()
        conn.close()

def start_app():
    print('Welcome to product inventory system.')
    print('Choose option from below :- ')
    option = input(' press 1 for View Products.\n press 2 for Add product.\n press 3 for Update quantity.\n press 4 for Remove product.\n press 5 for Exit.\n Choice: ')
    match option:
        case '1': return view_products()
        case '2': return add_new_product()
        case '3': return update_quantity()
        case '4': return remove_product()
        case '5': return None;
        case _:
            print( 'Invalid Choice')
            return None

start_app()