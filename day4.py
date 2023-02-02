# _____________________Comprehension Dictionaries______________________
# d = {n : n*n for n in range(1, 5)}
# print(d)
# # Calculating product price for 5
# old = {'rice': 60, 'dhaal': 120, 'oil': 150}
# new = {product: price*5 for (product, price) in old.items()}
# print(new.values())
# With condition
# real = {'sam': 24, 'angle': 18, 'kumar': 35}
# now = {name: age for (name, age) in real.items() if age >= 20}
# print(now)
# Create a list with 8 customers names display a dictionary which 
# has customers names along with discounts for them from a particular shop.
# import random
# customersList = ['sam', 'shyam', 'tarun', 'kumar', 'madhu', 'sagar', 'krishna']
# customersDict = {customer: random.randint(1, 100) for (customer) in (customersList)}
# print(customersDict)
# l1 = ['sam', 'tarun', 'kumar']
# l2 = [1, 2, 3]
# a = {b: c for (b, c) in zip(l1, l2)}
# print(a)
# Create 2 list first list have 5 students second list contains total marks(1, 500)
# create a dict where names as keys and percentage as values.
# l1 = ['sam', 'krishna', 'madhu', 'kumar', 'tarun']
# l2 = [450, 470, 466, 499, 412]
# percentages = []
# for i in range(len(l2)):
#     percentages.append(l2[i]/500*100)
# # print(percentages)
# studentsDict = {student: percentage for (student, percentage) in zip(l1, percentages)}
# print(studentsDict)
# _________________Strings___________________
# n = "hi i'am "manoj""
# n = "hi i'am manoj"
# print(n)
# m = 'hi i\'am manoj'
# print(m)
# print('a'>'b')
# print(max('a', 'b', 'c'))
# s = '   WeLcOMe sjdhj'
# print(s.upper())
# print(s.lower())
# print(s.casefold())
# print(s.capitalize())
# print(s.replace('O', 'u'))
# print(s.strip())
# print(s.center(50, 'e'))
# print(s.count('e'))
# print(s.count('e', 5, len(s)))
# print(s.endswith('h', 0, -1))
# print(s.find('e', 5, len(s)))
# print(s.index('e', 5, len(s)))
# print(s.islower())
# print(s.isupper())
# print('Uhcejc'.istitle())
# ___________________________________________
# x = 20
# print(id(x))
# x = 30
# print(id(x))
# l = [1, 2, 3]
# print(id(l))
# l.append(4)
# print(id(l))
'''mutable & immutable
mutable : can be changed after creation
eg: list, 
set, 
dictionary
immutable: can be changed after creation
eg: int, 
float '''
# ______________________Problems___________________________
# Get one string as input along with a character find out and
# display whether the particular character is in the string or not.
# s = list(map(str, input('Enter a string along with a character: ').split(', ')))
# print(s[0])
# print(s[1])
# givenStr = s[0]
# givenChar = s[1]
# if givenStr.find(givenChar, 0, len(givenStr)) != -1:
#     print('The string contains the character')
# else:
#     print('The string doesnt contains the character')

# Check whether the given string is palindrome or not.
# s1 = input('Enter a string: ')
# # print(len(s1)/2)
# count = 0
# if len(s1) % 2 == 0:
#     for i in range(len(s1)//2):
#         if s1[i] == s1[-(i + 1)]:
#             count += 1
#     if count == len(s1)//2:
#         print(s1, 'is a palindrome')
#     else:
#         print(s1, 'is not a palindrome')
# else:
#     for j in range((len(s1)- 1)//2):
#         if s1[j] == s1[-(j + 1)]:
#             count += 1
#     if count == (len(s1)- 1)//2:
#         print(s1, 'is a palindrome')
#     else:
#         print(s1, 'is not a palindrome')
    
    
# After entering one string as input check if the string contains space or not
# if yes count no of spaces in the string.
# s2 = input('Enter a string: ')
# spaceChar = ' '
# if spaceChar in s2:
#     print('There are', s2.count(' '), 'spaces')
# else:
#     print('There are no spaces')

# create a list with vowels get one string as input count no of vowels from the string
# display the result.
# l = ['a', 'e', 'i', 'o', 'u']
# s = input('Enter a string: ')
# count = 0
# for i in l:
#     count += s.count(i)
# print(count)

# _________________Math module___________________
import math
print(math.ceil(2.4))
print(math.floor(2.4))
print(math.sqrt(25))
print(math.factorial(6))
print(math.pow(2, 4))
print(math.fmod(10, 3))
a, b = divmod(10, 3)
print(a, b)




