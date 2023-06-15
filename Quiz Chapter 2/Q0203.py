"""
Quiz Q0203
Create two variables first_name, and last_name and print the sentence in the format below:

"My name is John Doe"

1.use + operator to concatenate strings
2.use format() method to achieve the same result
3.use f-strings to achieve the same result
4.use %s formatting method to achieve the same result
"""
# Answer1
first_name = "John"
last_name = "Doe"
print("My name is", first_name, last_name)
# My name is John Doe

# Answer2 format() method:
print("My name is {} {}".format(first_name, last_name))
# My name is John Doe

# Answer3 fstring method:
print(f"My name is {first_name} {last_name}")
# My name is John Doe

# Answer4 %s formatting method:
print("My name is %s %s" %(first_name, last_name))

"""
PS C:\Users\rajan> & C:/Users/rajan/AppData/Local/Programs/Python/Python311/python.exe c:/Users/rajan/Desktop/Quiz/Q0203.py
My name is John Doe
My name is John Doe
My name is John Doe
My name is John Doe
PS C:\Users\rajan>
"""