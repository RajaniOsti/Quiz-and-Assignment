"""Write a program that accepts a number from the terminal and 
checks whether it is a multiple of both 3, 4, and 5 or not"""
num = int(input("enter a number"))
if (num % 3 == 0) and (num % 4 == 0):
    print(f'The number {num} is divisible by 3 and 4 both')
elif (num % 3 == 0) and (num % 5 == 0):
    print(f'The number {num} is divisible by 3 and 5 both')
elif (num % 4 == 0) and (num % 5 == 0):
    print(f'The number {num} is divisible by 4 and 5 both')
elif(num % 3 != 0 ):
    print(f'The number {num} is divisible by 3')
elif(num % 4 != 0 ):
    print(f'The number {num} is divisible by 4')
elif(num % 5 != 0 ):
    print(f'The number {num} is divisible by 5')
else:
    print(f'The number {num} is not divisible by 3, 4 and 5 both')
