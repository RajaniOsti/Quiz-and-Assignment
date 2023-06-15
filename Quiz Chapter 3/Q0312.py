"""
Suppose we have the variable assigned as follows:

PI = 3.1415
I want to print the value of PI to be 3. How should I convert the data to an integer? Please Explain with code.
"""
PI = 3.1415
print(int(PI))      #3

"""
Suppose we have variables assigned as follows:

str_1 = "20"
str_2 = "30"
print(str_1 + str_2)
above line gives us output of "2030" but I want the answer to be 50. How would you solve the problem using type conversion?
"""
str_1 = "20"
str_2 = "30"
print(int(str_1) + int(str_2))      # 50

"""
Suppose we have variables assigned as follows:

x = ['1', '2', '3', '4', '5']
sum = 0
I want the value of sum to be 15.
Hint:
Use for loop in the list
Change the type from str to int in each iteration
"""
x = ['1', '2', '3', '4', '5']
# print(int(x))


"""
Suppose we have variables assigned as follows:
odd = [1, 3, 5, 7, 9, 11, 13, 15]
prime = [2, 3, 5, 7, 11, 13, 17]
use type conversion to these lists to appropriate data type and find out
numbers that are odd but not prime
numbers that are either odd or prime
numbers that are prime but not odd.
Final values should be list and stored to respective variables.
"""
odd = [1, 3, 5, 7, 9, 11, 13, 15]
prime = [2, 3, 5, 7, 11, 13, 17]
# print(set(odd))           #{1, 3, 5, 7, 9, 11, 13, 15}
# print(set(prime))   #{2, 3, 5, 7, 11, 13, 17}
print(list((set(odd)) - (set(prime))))      #[1, 9, 15]
print(list((set(odd)) | (set(prime))))      #[1, 2, 3, 5, 7, 9, 11, 13, 15, 17]
print(list((set(prime)) - (set(odd))))      #[17, 2]

