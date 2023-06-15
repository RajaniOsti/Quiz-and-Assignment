"""
Write a program to create two different set of countries

Rich: USA, China, Japan, Germany, France, Australia, Italy
Europe: Germany, France, England, Switzerland, Italy, Portugal, Sweden
Use Set methods to find out:

countries that are rich but not in Europe
countries that are in Europe but not rich
countries that are both rich and are in Europe
countries that are either rich or in Europe, but not both
all the countries in either of the sets. (Names must be unique)
see if two sets are disjoint or not
now remove the common countries from the rich set and check if two sets are disjoint or not.
hint: use difference_update() method. for more, please refer to python documentation
Create 2 more sets:
asian_rich: China, Japan
american_rich: USA, Canada
Check whether asian_rich is a subset of rich or not.
Check whether rich is a superset of asian_rich or not.
Check whether american_rich is a subset of rich or not. Note: you can use different operators to perform above operations
"""
rich = {"USA", "China", "Japan", "Germany", "France", "Australia", "Italy"}
europe = {"Germany", "France", "England", "Switzerland", "Italy", "Portugal", "Sweden"}
print(rich-europe)      #{'Japan', 'Australia', 'China', 'USA'}
print(europe - rich)        #{'Sweden', 'England', 'Switzerland', 'Portugal'}
print(rich & europe)        #{'Germany', 'Italy', 'France'}
print(rich.symmetric_difference(europe))   
#{'Australia', 'USA', 'Sweden', 'Switzerland', 'England', 'Japan', 'Portugal', 'China'}
print(rich.intersection(europe))        #{'France', 'Germany', 'Italy'}
print(rich.isdisjoint(europe))                      # False
print((rich-europe).isdisjoint(europe-rich))        #True
asian_rich = {"China","Japan"}
american_rich = {"USA", "Canada"} 
print(asian_rich.issubset(rich))        #True
print(rich.issuperset(asian_rich))      #True
print(american_rich.issubset(rich))     #False
