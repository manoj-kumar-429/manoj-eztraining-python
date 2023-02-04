# import random as r
# x = 'i love sweets'
# print(r.sample('xjhs', 4))
# print(r.sample(x, 4))
# a = [1, 2, 3, 4, 5, 6]
# r.shuffle(a)
# print(a)
# a = [1, 2, 3, 4, 5, 6]
# print(r.choice(a))
# print(r.choices(a, k = 3))
# b = 'welcome back'
# print(r.choice(b))
# print(r.choices(b, k = 15))
# a = r.random()
# print(a)
# print(r.randint(20, 30))
# print(r.uniform(5, 10))
# z = dir(r)
# print(r.choice(z))
# _____________________Calendar module_____________________
# import calendar
# print('Full year calendar: ')
# print(calendar.calendar(2023))
# print('Month calendar: ')
# print(calendar.month(2023, 9))
# print('Set first day of the week: ')
# calendar.setfirstweekday(calendar.THURSDAY)
# print(calendar.month(2023, 12))
# _____________________Datetime module______________________
# import datetime
# a = datetime.datetime.now()
# print(a)
# sv = a.strftime('%y')
# fv = a.strftime('%Y')
# print('year short version: ', sv)
# print('year full version: ', fv)

# ______________________Functions___________________________
'''
Classifications:
1. pre defined functions
2. user defined functions
>>for code reusability we use functions, 
>>if we want to use a particular concept multiple times in our program instead of writting
the same code multiple times we can write it once include that inside a function and 
can call the function where ever we need it.
Types: 
1. functions without argument without return value
2. without argument with return value
3. with argument with return value
4. with argument without return value
'''
# def sample():
#     print('Great day')
#     print('Happy time')
# sample()
# print('today')
# sample()
# def multi():
#     n = list(map(int, input('Enter 3 numbers: ').split( )))
#     prod = n[0]*n[1]*n[2]
#     return prod
# res = multi()
# print(res)
# def multi(n1, n2, n3):
#     prod = n1*n2*n3
#     print(prod)
# n = list(map(int, input('Enter 3 numbers: ').split( )))
# multi(n[0], n[1], n[2])
# def multi(n1, n2, n3):
#     prod = n1*n2*n3
#     return prod
# # n = list(map(int, input('Enter 3 numbers: ').split( )))
# res = multi(n[0], n[1], n[2])
# print(res)
# _________Lemons program using func type 1___________
# def lemons():
#     noOfLemons = int(input('Enter no of lemons: '))
#     if noOfLemons > 21:
#         print('There are', noOfLemons - 21, 'excess lemons')
#     elif noOfLemons < 21:
#         print('Need', 21 - noOfLemons, 'more lemons')
#     else:
#         print('Got 21 lemons')
# lemons()
        
# # Find factors of the given number using functions type 2
# def factorsOfNum():
#     factors = []
#     num = int(input('Enter a number: '))
#     for i in range(1, (num//2) + 1):
#         if num % i == 0:
#             factors.append(i)
#     factors.append(num)   
#     return factors
# print(factorsOfNum())
        
# # Print multiplication table of the given number using functions type 3
# def multiplicationTable(n):
#     for i in range(1, 11):
#         print(n, 'x', i, '=', i*n)
# multiplicationTable(int(input('Enter a number: ')))

# # Find out sum of digits of given number using functions type 4
# def sumOfDigits(n):
#     sum = 0
#     for i in range(len(n)):
#         sum += int(n[i])
#     print(sum)
# sumOfDigits(input('Enter a number: '))
'''
Recursive function: 
A function which calls itself is called as recursive function.
'''
# def display():
#     n = int(input('Enter a number: '))
#     if n == 1:
#         display()
#     else:
#         print('over')
# display()
# def fact(n):
#     if n == 1:
#         return 1
#     n *= fact(n-1)
#     return n
# print(fact(5))
# def facto(n):
#     prod = 1
#     for i in range(1, n+1):
#         prod *= i
#     print(prod)
# facto(int(input('Enter a number: ')))
n = int(input('Enter a number: '))
a = 0
b = 1
sum = 0
count = 1
while(count <= n):
    print(sum, end = '')
    count += 1
    a = b
    b = sum
    sum = a + b

        




