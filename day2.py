# get any 2 numbers both the numbers should be less than
# or equal to 15 perform bitwise and, or, xor
# num1, num2 = input('Enter 2 numbers <= 15: ').split( )
# num1, num2 = int(num1), int(num2)
# print('Bitwise OR:', num1 | num2)
# print('Bitwise AND:', num1 & num2)
# print('Bitwise XOR:', num1 ^ num2)
# n = int(input('size: '))
# a = list(map(int, input('Numbers: ').strip().split()))[:n]
# print(a)
# Find the product of 10 int numbers.
# n = list(map(int, input("Enter 10 numbers: ").split()))
# print(n[0]*n[1]*n[2]*n[3]*n[4]*n[5]*n[6]*n[7]*n[8]*n[9])
# print('Its', 'a', 'good', 'day', end = ' ')
# print('all', 'is', 'good', sep = '#', end = ' ')
# print('joy')
# triangle

# print('*', '*', '*', '*', '*', sep='   ')
# print('  *', '*', sep='           ')
# print('    *', '*', sep='       ')
# print('      *', '*', sep='   ')
# print('        *')

# # hollow heart
# print('________________')
# print('________________')
# print('', '**', ' ', '**', '', sep='   ')
# print('*', ' ', '*', ' ', '*', sep='   ')
# print('  *', '*', sep='           ')
# print('    *', '*', sep='       ')
# print('      *', '*', sep='   ')
# print('        *')

# # frog
# print('________________')
# print('________________')
# print(' ', '*', ' ', '*', ' ', sep='   ')
# print(' *', '', '*', '', '*', sep='   ')
# print('*', '*', '*', '*', '*', sep='   ')
# print(' *', '', '*', '', '*', sep='   ')
# print('    *', ' ', '', '*', sep='  ')
# print('     *', ' ', ' ', '*', sep=' ')
# print('        *')
# conditional statement
# if, ifelse, else-if, else-if ladder, nested if
# temp > 45 ==> hottest
# 40 < temp <= 45 ==> hot
# 25 < temp <= 40 ==> moderate
# 10 < temp <= 25 ==> cold
# temp <= 10 ==> chill
'''
num = int(input("Enter a number: "))
# 1st
if num == 500:
    print(num, ' is 500')
else:
    print(num, ' is not 500')
#2nd
if num > 0:
    if num % 2 == 0:
        print(num, ' is even positive')
    else:
        print(num, ' is odd positive')
else:
    if num % 2 == 0:
        print(num, ' is even negative')
    else:
        print(num, ' is odd negative')
# 3rd
n= list(map(int, input('Enter two nummbers: ').split( )))
if n[0] > n[1]:
    print(n[0], 'is greater than', n[1])
else:
    print(n[1], 'is greater than', n[0])

# 5th
nums = list(map(int, input('Enter three numbers: ').split( )))
if nums[0] > nums[1] and nums[0] > nums[2]:
    print(nums[0], 'is greater than', nums[1], 'and', nums[2])
elif nums[1] > nums[0] and nums[1] > nums[2]:
    print(nums[1], 'is greater than', nums[0], 'and', nums[2])
else:
    print(nums[2], 'is greater than', nums[0], 'and', nums[1])
# 6th
if num == 11:
    print(num, ' is 11')
else:
    print(num, ' is not 11')
# 7th
if num % 2 == 0:
    print(num, 'is divisible by 2')
elif num % 5 == 0:
    print(num, 'is divisible by 5')
else:
    print(num, 'is not divisible by either 2 or 5')
    
    '''
# 4th
# a = 3
# if type(a) == float:
#     print(a, 'is float type')
# elif type(a) == int:
#     print(a, 'is integer type')
    
# n = float(input("Enter an integer or float: "))
# res = n - int(n)
# if res != 0:
#     print('float')
# else:
#     print('integer')
# i = 0
# while i < 10:
#     print(i + 1)
#     i += 2
# j = 1
# for j in range(10):
#     print(j)
# print all even nos btw 2 to 20
# i = 2
# print('Even numbers between 2 and 20: ')
# while i >= 2 and i <= 20:
#     print(i)
#     i += 2
# for i in range(2, 21, 2):
#     print(i)
# print all odd nos btw 1 to 30
# j = 0
# print('Odd numbers between 1 and 30: ')
# while j >= 0 and j < 30:
#     print(j + 1)
#     j += 2
# for i in range(0, 31, 2):
#     print(i+1)
# _____________Guess the number game_____________________
import random
num = random.randrange(1, 30)
print(num)
guess = int(input("Enter any number: "))
while guess != num:
    
    if guess > num:
        print('Too High!')
        guess = int(input('Enter number again: '))
    elif guess < num:
        print('Too Low!')
        guess = int(input('Enter number again: '))
    else:
        break
print('You guessed it right!')
