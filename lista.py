# Declaration 
#List:
my_lisy = [1, 2, 3, 4, 5, "Avocato", True, False]
print("My list contains:", my_lisy)

#List Exemples
my_lisy[0] = "Python"

# 1º iten contains
print("My list[0] contains:", my_lisy[0])

# 2º iten contains
print("My list[1] contains:", my_lisy[1])

# 3º iten contains
print("My list[2] contains:", my_lisy[2])

# 4º iten contains
print("My list[3] contains:", my_lisy[3])

# 5º iten contains
print("My list[4] contains:", my_lisy[4])

# 6º iten contains
print("My list[5] contains:", my_lisy[5])

# 7º iten contains
print("My list[6] contains:", my_lisy[6])

# 8º iten contains
print("My list[7] contains:", my_lisy[7])

# Slice
print("Slice [1:7]:", my_lisy[1:7])

# Slice to
print("Slice to element 6:", my_lisy[:6])

# Slice afther
print("Slice to element 6:", my_lisy[2:])

#Append()
my_lisy.append(6)
print("Afther append(6):", my_lisy)

# Method: index
indice = my_lisy.index(6)
print("my indice in the element 6 is:", indice)

# Method Insert
my_lisy.insert(2, 10)
print("Afther the insert(2,10):", my_lisy)

# Method Pop
element_removed = my_lisy.pop(3)
print("Element removed:", element_removed)
print("Afther Pop(3):", my_lisy)

# Method remove 
my_lisy.remove(True)
print("Afther remove(true):", my_lisy)

# Method Sort
# my_lisy.sort() // does not work because it has different types of items (texts, numbers and booleans).
# print("Afther sort():", my_lisy)

