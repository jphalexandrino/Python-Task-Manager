
# Creating a tupla for exemple
my_tupla = (1,2,3,4)

print("My tupla", my_tupla)

# 1º iten contains
print("My tupla[0] contains:", my_tupla[0])

# 2º iten contains
print("My tupla[1] contains:", my_tupla[1])

# Last iten contains
print("My tupla[1] contains:", my_tupla[-1])

# The Tupla is Immutable

# Method count
count = my_tupla.count(2)
print("The element 2 appear for", count, "times")

# Method Index
index = my_tupla.index(3)
print("my index on third element is:", index)