"""
Create a dictionary of a person that contains key value pair of

name: str
age: int
profession: str
married: bool
Set values with valid data types to each keys of the dictionary

Print the value of 'name' from the dictionary
Add the age by 10 and print the dictionary items in formatted string Eg: {name} will be {new_age} after 10 years.
Try getting the value of 'employed' from the dictionary.
If exception occurs, note it and check what exception says and finally comment the line.
try using get() method instead of large brackets [] in the previous question.
try using get() method with second parameter as False and see what is printed. Example: person.get('employed', False)
"""
person = {
    "name": "ram",
    "age": 30,
    "profession": "teacher",
    "married": True,
}
    
print(person["name"])       # ram
person.update({"age": 40,})
print(person["age"])        #40
#print(person["employed"])       #KeyError: 'employed'
person["employed"] = False
print(person["employed"])
print(person.get("employed", False))
print(person)
# {'name': 'ram', 'age': 40, 'profession': 'teacher', 'married': True, 'employed': False}
print(f'{person["name"]} will be  {person["age"]} after 10 years')
# ram will be  40 after 10 years