print('''
Create a program that asks the user for a number and then prints out a list of all the
divisors of that number. (If you don’t know what a divisor is, it is a number that divides
evenly into another number. 
    For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
    ''')

x = int(input("Please intruduce a number: "))

print(f'The divisors of {x} are: ')
for elem in range(x):
    if elem != 0:
        y = x % elem

        if y == 0:
            print(elem)

print('''
    source: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
    ''')