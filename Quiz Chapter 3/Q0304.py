"""
Write a program to create a tuple to add 5 different numbers.

find out the length of the tuple
find out the 3rd element of the tuple by accessing it through the index
use enumerate() function to map each element with its index and print it using for loop.
"""
x = []
num = int(input("enter a number"))      # 5
x.append(int(num))
print(x)        #[5]
x.extend([6, 7, 8, 9])
print(x)        #[5, 6, 7, 8, 9]
x = tuple(x)
print(x)        # (5, 6, 7, 8, 9)
print(len(x))       #5
print(x[2])         #7
for item in x:
    print(f'The item is {item}')
"""
The item is 5
The item is 6
The item is 7
The item is 8
The item is 9
"""

# use enumerate() function to map each element with its index and print it using for loop.
for index, item in enumerate(x):
    print(index, item)
# 0 5
# 1 6
# 2 7
# 3 8
# 4 9
