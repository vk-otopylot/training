product_details = {
    101: {"name": "Pen", "price": 10},
    102: {"name": "Notebook", "price": 50},
    103: {"name": "Eraser", "price": 5},
}

cart = []

def billing_console_app():
    choice = int(input('Choose Option from Below:-\n1. show product\n2. Add to cart\n3. Print bill\n4. Save bill\nYour Choice:- '))

    def show_products():
        print('Available Products:- ')
        for data in product_details.values():
            print(f'{data['name']}: Rs.{data['price']}')
        print()
        billing_console_app()

    def add_to_cart():
        name = input('Enter the name of the product: ')
        qty = int(input('Enter the Quantity: '))
        n_name = name.capitalize()
        for key,value in product_details.items():
            if value['name'] == n_name:
                k = key
                n_name = value['name']
                price = value['price']
                cart.append({
                    "id": k,
                    "name": n_name,
                    "price": price,
                    "qty": qty,
                    "total": (price*qty)
                })
        billing_console_app()

    def print_bill():
        print('=======BILL=======')
        print(f'{'Item':<10} \t Price \t Qyt \t Total')
        print('------------------')
        for data in cart:
            print(f'{data['name']:<10} \t {data['price']} \t {data['qty']} \t {data['total']}')
        print('------------------')
        total = 0
        for val in cart:
            total = total + val['total']
        print(f'Grand Total: {total}')
        billing_console_app()

    def save_bill():
        with open('bill.txt', 'w') as file:
            file.write(f'Bill No: 1' + '\n')
            file.write('------------' + '\n')
            total = 0
            for data in cart:
                file.write(f'{data['name']:<10}\t{data['qty']} X {data['price']} = {data['price']*data['qty']}' + '\n')
                total = total + data['total']
            file.write('------------' + '\n')
            file.write(f'Total Amount: {total}')
        print('Thank You For Shopping with us. Have a Nice Day!!!')

    match choice:
            case 1: return show_products()
            case 2: return add_to_cart()
            case 3: return print_bill()
            case 4: return save_bill()
            case _: return 'Invalid Choice'

billing_console_app()