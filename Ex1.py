import datetime

print('''
    Create a program that asks the user to enter their name and their age. Print out
    a message addressed to them that tells them the year that they will turn 100 years old.
    ''')
y = datetime.datetime.now()
y = int((y.strftime('%Y')))

x = input('Please introduce your name: ')
z = int(input('Please introduce your age: '))
Formula = int(y + 100 - z)
print(f'Hello {x}, I\'m glad to inform you that you\'ll turn 100 years old in {Formula}.')

print('''
    source: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
    ''')
