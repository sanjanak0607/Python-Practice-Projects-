# number guessing game using generator function
def Game1_Gen():
    yield 'Now MULTIPLY that number with 2'
    yield 'Now ADD 10 to your result.'
    yield 'Now DIVIDE the result by 2'
    yield 'Now SUBTRACT your original number from your result.'

def Game2_Gen():
    yield 'Now MULTIPLY that number with 2'
    yield 'Now ADD 8 to your result.'
    yield 'Now DIVIDE the result by 2'

def Game1():
    print('Welcome to the Result Guessing Magic Trick!!!!')
    print('Lets Begin!')
    print('Think of ANY Number')
    input('Please press enter once you are done')

    for step in Game1_Gen():
        print(step)
        input('Please press enter once you are done')

    print('So Are you ready to see the magic?')
    print('So the final result is: ..............')
    print('.')
    print('.')
    print('.')
    print('.')
    print('5')

def Game2():
    print('Welcome to the Original Number Guessing Magic Trick!!!!')
    print('Lets Begin!')
    print('Think of ANY Number')
    input('Please press enter once you are done')

    for steps in Game2_Gen():
        print(steps)
        input('Please press enter once you are done')

    final = int(input('Enter the result you got: '))
    print('Now I am gonna guess your original number.')
    print('So Are you excited for the magic to happen?')
    result = final - 4
    print('The final result is: ..............')
    print('.')
    print('.')
    print('.')
    print('.')
    print('.')
    print('.')
    print('.')
    print('.')
    print('.')
    print(result)

while True:
    print('Welcome to the game arena.....')
    print('Lets Begin!')
    print('Before starting just make a choice which game you wanna play first? Your options are: ')
    print('1. Result Guessing Magic Trick')
    print('2. Original Number Guessing Magic Trick')
    print('3. I dont wanna play now so I am leaving.')
    ch=int(input('Enter your choice: '))
    if ch==1:
        Game1()
    elif ch==2:
        Game2()
    elif ch==3:
        print('Okayyyy Byeeeeeeeeeeee!!!!!!!!')
        break
    else:
        print('Wrong choice!')