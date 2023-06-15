"""
Write a program to add 5 different wild animals to a list named wild.

Example: tiger, lion, deer, bear, zebra

sort them in ascending using the sort() method.
reverse the list using the reverse() method.
now add 3 more animals to the list wild. Example: leopard, elephant, rhino
find the position of leopard using the index() method and remove it using the pop() method.
pop should have the index value returned using the index() method.
do not hard-code the position of leopard by manually counting it from the list.
check whether the leopard is removed from the list or not by index() method again. if the value error occurs, you have successfully removed it from the list. otherwise, try to do it again.
you can then comment the line that gives exception to continue to the next question.
Now add leopard again in the index 2 using insert() method.
Again, remove rhino from the list using remove() method.
Note: you can check output after each successive operations.
"""
wild = ["tiger", "lion", "deer", "bear", "zebra"]
wild.sort()
print(wild)     # ['bear', 'deer', 'lion', 'tiger', 'zebra']
wild.reverse()
print(wild)     # ['zebra', 'tiger', 'lion', 'deer', 'bear']
wild.sort(reverse = True)       
print(wild)     # ['zebra', 'tiger', 'lion', 'deer', 'bear']
wild.extend(["leopard", "elephant", "rhino"])
print(wild)     #['zebra', 'tiger', 'lion', 'deer', 'bear', 'leopard', 'elephant', 'rhino']
print(wild.index("leopard"))        # 5
print(wild)     #   ['zebra', 'tiger', 'lion', 'deer', 'bear', 'leopard', 'elephant', 'rhino']
wild.pop(5)
print(wild)     #   ['zebra', 'tiger', 'lion', 'deer', 'bear', 'elephant', 'rhino']
# print(wild.index("leopard"))    #   ValueError: 'leopard' is not in list
wild.insert(2, "leopard")
print(wild)     #   ['zebra', 'tiger', 'leopard', 'lion', 'deer', 'bear', 'elephant', 'rhino']
wild.remove("rhino")
print(wild)     #   ['zebra', 'tiger', 'leopard', 'lion', 'deer', 'bear', 'elephant']


