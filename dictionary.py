pessoa = {
    "name": "João",
    "surname": "Alexandrino",
    "age": 16,
    "city": "Novo Hamburgo"
}

print("name:", pessoa["name"])
print("surname:", pessoa["surname"])
print("age:", pessoa["age"])
print("city:", pessoa["city"])

pessoa["age"] = 18
print("age att:", pessoa["age"])

del pessoa["city"]

print(pessoa)

# Methods: Keys(), values(), itens()
keys = list(pessoa.keys())
print("Keys of dictionary:", keys)
print("First Key:", keys[0])

# Method values 
values_list = list(pessoa.values())
print("Values of dictionary:", values_list)
print("First Value of dictionary:", values_list[0])

# Method items
items_value = list(pessoa.items())
print("Key value to dictionary is:", items_value)
print("First value:", items_value[0][1])