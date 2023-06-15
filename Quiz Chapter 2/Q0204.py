"""
Quiz Q0204
Assign a variable pi and assign value 3.14159265

1.use formatting strings to show pi with 3 digits after the decimal
2.use formatting strings to show pi with 2 digits after the decimal but allocate 10 spaces for the variable.
3.use f-string to show the result in the following format: "The value of PIE is 3.14" ( hint: "%<a>.<b>f" )
"""

pi = 3.14159265
print(f"{pi:8.3f}")
# 3.142
print(f"{pi:10.2f}")
"""
PS C:\Users\rajan> & C:/Users/rajan/AppData/Local/Programs/Python/Python311/python.exe c:/Users/rajan/Desktop/Quiz/Q0204.py
   3.142
      3.14
PS C:\Users\rajan>
"""

