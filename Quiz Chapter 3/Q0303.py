"""
Try creating a multi-dimensional list or nested list multi containing different numbers.

Example:
[
    [12, 52, 37],
    [46, 51, 16],
    [17, 82, 39]
]
Access the number 51 from the list.
Access the number 82 using the negative indices.
Find out the length of the list multi
Append another list [40, 61, 10] inside the list multi. The final list should be: [[12,52,37],[46,51,16],[17,82,39],[40, 61, 10]]
Use foreach in the list multi to print each list item to the console.
Bonus: Try using nested foreach to access each item inside of the inner list
Bonus: Try finding out the length of each inner list
Finally clear the list multi using the clear() method and verify if the list is empty or not.
"""
numbers = [[12, 52, 37], [46, 51, 16], [17, 82, 39]]
print(numbers[1][1])    # 51
print(numbers[-1][-2])  #82
print(len(numbers))     #3
numbers.append([40, 61, 10])
print(numbers)          # [[12, 52, 37], [46, 51, 16], [17, 82, 39], [40, 61, 10]]
for item in numbers:
    print(f'The item is {item}')
"""
The item is [12, 52, 37]
The item is [46, 51, 16]
The item is [17, 82, 39]
The item is [40, 61, 10]
"""

# todo: review the lines below [added by ghimiresdp]
# ------------------------------------------------------------------------------
# Bonus: Try using nested foreach to access each item inside of the inner list
for outer_item in numbers:
    for inner_item in outer_item:
        print("The item is:", inner_item)
"""
The item is: 12
The item is: 52
The item is: 37
The item is: 46
The item is: 51
The item is: 16
The item is: 17
The item is: 82
The item is: 39
The item is: 40
The item is: 61
The item is: 10
"""

# Bonus: Try finding out the length of each inner list
for outer_item in numbers:
    print("the length of the inner item is: ", len(outer_item))

# Finally clear the list multi using the clear() method and verify if the list is empty or not.

# ------------------------------------------------------------------------------

numbers.clear()
print(numbers)          # []
