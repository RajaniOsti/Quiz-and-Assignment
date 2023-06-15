"""
Quiz Q0205
Use a function input() to input the the name and age from the command line and display the formatted
 text as instructed below:

1.use input() function to ask the name to the user. The console should show "What is your name?" to input the name
2.similarly ask the user to input the age and assign it to another variable.
3.Show a sentence describing the user name and age using different formatting methods.
hint: Output would be a sentence similar to Hello 20 years old John!!.
"""
# Question1
print("what is your {} ?".format("name"))
# what is your name ?

# Question2
print("what is your {} ?" .format("age"))
# what is your age ?

# Question4
name = "John"
age = 20
print("Hello %d years old %s !!" %(age, name))
# Hello 20 years old John !!
print("Hello {} years old {} !!". format(age, name))
# Hello 20 years old John !!
print(f"Hello {age} years old {name} !!")
# Hello 20 years old John !!