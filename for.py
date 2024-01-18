"""
print("For using list")
list = [1, 2, 3, 4, 5]
for element in list:
    print(element)
"""

print("\n For using tuple")
tuple = (1, 2, 3, 4, 5)
for element in tuple:
    print(element)

user = {
    "name": "João",
    "age": 16,
    "city": "Novo Hamburgo"
}
print("\n For using dictionary - keys")
for keys in user.keys():
    print(keys)

print("\n For using dictionary - Values")
for value in user.values():
    print(value)

print("\n For using dictionary - Items")
for keys, value in user.items():
    print(f"{keys}: {value}")

# range():
    print("\n Using Range() function")
for number in range(5):
    print("Number:", number)

# Len()
print("\n Using Range() function with len()")
list2 = [1, 2, 3, 4, 5]
for index in range(0, len(list2)):
    print("Index:", index)
    print("Element:", list2[index])