"""
Quiz Q0301
Write a program to create an empty list named my_list and

1. Add numbers 5 and 9 to the list using append() method
2. Ask the user to input any number in the console and add the number to the list.
3. You can use int() to typecast string to integer if you want.
4. Create another list more_items with 3 items on it and extend the list my_list using extend method.
5. Now find the length of the list and print the length of list describing it in a sentence.
6. you can use string formatting for better outputs.
7. Now remove the second item using pop() method and see if the item exists in the list
you can print the list before and after using the pop() method.
"""
my_list = []
my_list.append(5)
print(my_list)
my_list.append(9)
print(my_list)
number = int(input("enter a number"))
print(number)
my_list.append(int(number))
print(my_list)
more_items = [2, 3, 4]
more_items.extend(my_list)
print(more_items)  # [2,3,4,5,9,8]     
print(len(more_items))
print(f"The length of the list 'more_items' is {len(more_items)}")
more_items.pop(1)
print(more_items)   #[2, 4, 5, 9, 8]
"""
[5, 9]
enter a number8
8
[5, 9, 8]
[2, 3, 4, 5, 9, 8]
6
The length of the list 'more_items' is 6
[2, 4, 5, 9, 8]
"""

