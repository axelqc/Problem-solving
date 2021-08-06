print('''
    Ask the user for a number. Depending on whether the number is even or odd,
     print out an appropriate message to the user. 
    ''')

print('This algorithm will determine if your number is even or odd.')
x = int(input('Please introduce  a number: '))
if x % 2 == 0:
    print(f'{x} is an even number')

else:
    print(f'{x} is an odd number')

print('''
    source: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html 
    ''')