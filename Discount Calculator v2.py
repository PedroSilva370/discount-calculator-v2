# Discount Calculator
def get_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('\033[31mInvalid input\033[m')

def result():
    price = get_float("Enter the product price: ")

    while True:
        choose = input('''\nDiscount or Interest
\033[32m1) Discount\033[m
\033[31m2) Interest\033[m
: ''').lower()
        # Ask the discount
        if choose in ['1', 'discount', 'd']:
            discount = get_float("Enter the discount percentage: ")
            new_price = price - (price * discount/100)
            break

        elif choose in ['2', 'interest', 'i']:
            interest = get_float("Enter the interest percentage: ")
            new_price = price + (price * interest/100)
            break


        else:
            print('\033[31mInvalid input\033[m')

    print(f"\033[32mThe new price is, {new_price:.2f}\033[m\n")

def again1():
    again = input('''Do you want again? 
\033[32m1) Yes\033[m
\033[31m2) No\033[m
: ''').lower()
    if again in ['1', 'yes', 'y']:
       return True
    elif again in ['2', 'no', 'n']:
        print(('\033[31m-=' * 16) + 'FINISHED' + ('=-' * 16 + '\033[m'))
        return False
    else:
        print("Invalid input")
        return again1()


# Start the programm
def start():
    while True:
        start1 = input('''Do you want start the programm? 
\033[32m1) Yes\033[m
\033[31m2) No\033[m
: ''').lower()
        if start1 in ["1", "yes", "y"]:
            print(('-=' * 16) + 'DISCOUNT CALCULATOR' + ('=-' * 16))

            while True:
                result()
                if not again1():
                    return
        elif start1 in ["2", "no", "n"]:
            print('\033[31m_____________________________________________________________\033[m')
            break
        else:
            print('Invalid input')

start()
