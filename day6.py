'''Exception Handling: 
When there is exception the devloper doesnt want intruption or disturbance 
in the program flow to achieve this we are using exception handling.'''
a = 100
# b = 10
# try:
#     print(a // b)
# except Exception as e:
#     print('Number cant be divisible by zero, ', e)
# print('over')
# try:
#     print('resource opened')
#     print(a//b)
# except Exception as e:
#     print('Number cant be divisible by zero, ', e)
# finally:
#     print('resource closed')
# try:
#     b = int(input('Enter a number: '))
#     print('resource opened')
#     print(a//b)
# except ZeroDivisionError as e:
#     print('Cant be divided by zero, ', e)
# except ValueError as e:
#     print('Invalid input, ', e)
# except Exception as e:
#     print('Other error, ', e)
# finally:
#     print('resource closed')
# x = int(input('Enter an even number: '))
# if x%2 != 0:
#     raise Exception('x should be even number')
# else:
#     print('x is even number')
'''OOPs:
It is an efficient concept used in all object oriented languages like
java and python. For multiple reasons we use oops concepts.
eg: Code reusability, Hiding data
Class:
Its a blue print.
eg: birds
Objects:
Its a thig created based on class.
note: One class can have multiple objects.
eg: parrot, peagion, peacock
'''
# class computer:
#     def config(self):
#         print('yes')
# lenova = computer()
# lenova.config()
# dell = computer()
# dell.config()
# ___________________Constructor_____________________
# class employee:
#     def __init__(self, name, id):
#         self.id = id
#         self.name = name
#     def display(self):
#         print('Id: %d \nName: %s' % (self.id, self.name))  
# emp1 = employee('John', 21)     
# emp2 = employee('sins', 21) 
# emp1.display()
# emp2.display()
# class computer:
#     a = 10
#     b = 20
#     print('Class variable inside class, ', a)
#     def config(self):
#         c = 100
#         print(c)
#         print('Instance access, ', self.b)
# lenova = computer()
# print(lenova.a)
# print(lenova.a + lenova.b)
# dell = computer()
# print('dell', dell.a)
# dell.config()





