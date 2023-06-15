"""
Quiz Q0210
Use Identity and Membership operations to solve the following problems

check whether the number 12 is an integer or not

divide 100 by 12 and check whether the number is float or not

suppose we have following lists:

x = [1,2,3,4,5]
y = [1,2,3,4,5]
z = x
Is x identical to y?
Is x identical to z?
Solve problems programmatically and write the reasons why they are or are not identical with each other.

Suppose there are following animals in the zoo:

elephant, tiger, zebra, lion, wolf

Check programmatically whether lion is in the zoo or not.
Check programmatically whether horse is in the zoo or not.
Create a list of first 7 prime numbers and check whether 9 is a prime number or not using membership operation.
"""
x1 = 12
print(type(x1))
# <class 'int'>
print(type(x1) is int)
# True
print(100/12)
# 8.333333333333334
print(type(8.333333333333334))
print(type(8.333333333333334) is float)
# <class 'float'>
# True

x = [1,2,3,4,5]
y = [1,2,3,4,5]
z = x
print(x == y)
# True. So, X and Y are identical
print(x == z)
# True. X and z are also identical


zoo = "elephant", "tiger", "zebra", "lion", "wolf"
print("lion" in zoo)
# True
print("lion" not in zoo)
# False
print("horse" in zoo)
# False
print("horse" not in zoo)
# True

prime_number = (1, 2, 3, 5, 7, 11, 13)
print(9 is prime_number)
# False