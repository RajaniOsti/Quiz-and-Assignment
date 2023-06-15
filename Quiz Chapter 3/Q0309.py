"""
create a dictionary car with 3 keys brand, model, and price.

Set a random value to a new key engine in the dictionary.
Add 3 more keys (color, no_of_seats, transmission) using update method.
Remove the key color from the dictionary.
Try using popitem() method in the dictionary and see what changes in dictionary
Use for loop to iterate through all keys from a dictionary.
Use for loop to iterate through all keys from a dictionary using keys() method.
Use for loop to iterate through all values from a dictionary using values() method.
Use for loop to iterate through all keys, values from a dictionary using items() method.
"""
car = {
    "brand":"Honda",
    "model": "CRV",
    "price": 35000,
}
car.update({
    "colour": "white",
    "no_of_seat": 5,
    "transmission": True
})
print(car)
# {'brand': 'Honda', 'model': 'CRV', 'price': 35000, 'colour': 'white', 'no_of_seat': 5, 'transmission': True}
car.pop("colour")
print(car)
# {'brand': 'Honda', 'model': 'CRV', 'price': 35000, 'no_of_seat': 5, 'transmission': True}
for key, value in car.items():
    print(f'the {key} is {value}')
# the brand is Honda
# the model is CRV
# the price is 35000
# the no_of_seat is 5
# the transmission is True
for x in car:
    print(x)
# brand
# model
# price
# no_of_seat
# transmission
for x in car:
    print(car[x])
# Honda
# CRV
# 35000
# 5
# True
for x in car.keys():
    print(x)
for x in car.values():
    print(x)
for x, y in car.items():
    print(x, y)