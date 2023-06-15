"""
create two different tuples t1 and t2 with different elements inside it 
create the next tuple t3 to add all values of t1 and t2 by destructuring or unpacking.

suppose t1 has (1, 6, 9, 4, 3)
and t2 has (2, 7, 8, 3, 5)
t3 must have (1, 6, 9, 4, 3, 2, 7, 8, 3, 5)
"""
t1 = (1, 6, 9, 4, 3)
t2 = (2, 7, 8, 3, 5)
t3 = (*t1, *t2)
print(t3)       #(1, 6, 9, 4, 3, 2, 7, 8, 3, 5)
