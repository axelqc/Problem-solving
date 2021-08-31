print('''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  
and write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). Make sure your program works on two lists of
different sizes.
    ''')


list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_c = []

list_a = list(set(list_a)) #converted into set to remove duplicates
list_b = list(set(list_b)) 

for a in list_a:
    for b in list_b:
        if a == b:
            list_c.append(a)
print(list_c)        

print('''
    source: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
    ''')




