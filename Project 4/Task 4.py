# bitwise operator calculator

def login(func):
    def wrapper(a,b):
        print('Operation Starts Here!!!!!')
        c = func(a,b)
        print('Results are: ', c)
        return c
    return wrapper


def main(a,b):
    operations = {
        1: login(lambda a,b: a & b),
        2: login(lambda a,b: a | b),
        3: login(lambda a,b: a ^ b),
        4: login(lambda a,b: ~ (a & b)),
        5: login(lambda a,b: ~ (a | b)),
        6: login(lambda a,b: ~ (a ^ b))
    }



    print('You have following options to perform Please make a choice from the options given below: ')
    print('1. Bitwise AND')
    print('2. Bitwise OR')
    print('3. Bitwise XOR')
    print('4. Bitwise NAND')
    print('5. Bitwise NOR')
    print('6. Bitwise XNOR')
    try:
        choice = int(input('Enter your choice: '))
        if choice in operations:
            operations[choice](a, b)
        else:
            print("You Chose Invalid Choice.")

    except ValueError:
        print('Please enter a number only')


exit_loop = False
while not exit_loop:
    while True:
        try:
            a = int(input('Enter first number: '))
            if a < 0:
                print('Please enter a positive number')
                continue
            break

        except ValueError:
            print('Please enter a number only')
            continue

    while True:
        try:
            b = int(input('Enter second number: '))
            if b < 0:
                print('Please enter a positive number')
                continue
            break
        except ValueError:
            print('Please enter a number only')
            continue
    print("1. Perform Operations")
    print("2. Change value of the numbers")
    print("3. Exit")

    while True:
        try:
            ch = int(input("Enter your choice: "))
            if ch == 1:
                main(a,b)
                continue
            elif ch == 2:
                break
            elif ch == 3:
                print("Okay Byeeeeeeeeee")
                exit_loop = True
                break
            else:
                print("invalid choice. Please enter a valid choice")
        except ValueError:
            print('Please enter a number only')