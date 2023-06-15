"""
Quiz Q0206
Perform the addition operations between the following data types and check whether the code runs successfully or not:

1.int and int (Example: 5 + 5)
2.int and float (Example: 5 + 5.5)
3.float and float (Example: 5.5 + 5.5)
4.str and str (Example: 'hello' + 'world')
5.int and str (Example: 5 + 'hello')
"""

int1 = 2
int2 = 2
float1 = 2.3
float2 = 2.2
str1 = "water"
str2 = "melon"
print(int1 + int2)
# 4
print(int1 + float1)
# 4.3
print(float1 + float2)
# 4.5
print(str1 + str2)
# watermelon
print(int1 + str1)
"""
Traceback (most recent call last):
  File "c:\Users\rajan\Desktop\Quiz\Q0206.py", line 26, in <module>
    print(int1 + str1)
          ~~~~~^~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""