print("For using list")
list = [1, 2, 3, 4, 5]
for element in list:
    print(element)

print("\nFor using tuple")
tuple = (1, 2, 3, 4, 5)
for element in tuple:
    print(element)

user = {
    "name": "João",
    "age": 16,
    "city": "Novo Hamburgo"
}
print("\nFor using dictionary - keys")
for keys in user.keys():
    print(keys)

print("\nFor using dictionary - Values")
for value in user.values():
    print(value)

print("\nFor using dictionary - Items")
for keys, value in user.items():
    print(f"{keys}: {value}")