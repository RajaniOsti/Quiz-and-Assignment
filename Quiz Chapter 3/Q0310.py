"""
Create a nested dictionary named yoda with following properties:
age: 910
species: Yodas
gender: male
affiliations: ['Jedi', 'Galactic Republic']
master:
name: Qui-Gon Jinn
age: 48
affiliations: ['Jedi', 'Galactic Republic', 'Heliost Clan']
master:
name: Dooku
age: 83
affiliations: ['House Serenno', 'Jedi']
Print the value of the first affiliation of Dooku from the dictionary
Add new affiliation 'Sith' to Dooku
pop the key 'master' from the dictionary"
"""
yoda = {
    "age": 910,
    "species": "Yodas",
    "gender": "male",
    "affiliations": ['Jedi', 'Galactic Republic'],
    "master":{
        "name": "Qui-Gon Jinn",
        "age": 48,
        "affiliations": ['Jedi', 'Galactic Republic', 'Heliost Clan'],
        "master":{
                "name": "Dooku",
                "age": 83,
                "affiliations": ['House Serenno', 'Jedi'],
            }
        }
    }

print(yoda["master"]["master"]["affiliations"][0])   
#House Serenno
yoda["master"]["master"]["affiliations"].append("Sith")
print(yoda)
"""
{'age': 910, 'species': 'Yodas', 'gender': 'male', 'affiliations': 
['Jedi', 'Galactic Republic'], 'master': {'name': 'Qui-Gon Jinn', 'age': 48, 
'affiliations': ['Jedi', 'Galactic Republic', 'Heliost Clan'], 
'master': {'name': 'Dooku', 'age': 83, 
'affiliations': ['House Serenno', 'Jedi', 'Sith']}}}
"""
yoda.pop("master")
print(yoda)
"""
{'age': 910, 'species': 'Yodas', 'gender': 'male', 'affiliations':
['Jedi', 'Galactic Republic']}
"""

