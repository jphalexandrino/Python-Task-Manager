# if, elif and else

#Exemple of "if"

age = 18
print("Exemple of if: ")
if age >= 18:
    print("You are of legal age ")
elif age >= 12:
    print("You are a teenager")
else:
    print("You are underage")

mensage = "You can get your driver's license" if age >= 18 else "You can't get a driver's license"
print(mensage)