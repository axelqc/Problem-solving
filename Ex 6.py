print('''
    Ask the user for a string and print out whether this string is a
    palindrome or not. (A palindrome is a string that reads the same
    forwards and backwards.)
    ''')

word = input("Introduce a word: ")
backwards = word[::-1]

if word == backwards:
    print('Word is palindrome.')

else:
    print('Word is not palindrome')

print('''
    source: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
    ''')