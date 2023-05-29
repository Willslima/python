users = {"Alice","Bob"}

users_2 = set({"Alice","Bob"})

print(type(users))
print(type(users_2))

#conjuntos/sets
#não permite conjuntos/dados repitidos

users.add("Adm")

print(users)

users_3 = {"Lena"}

users.union(users_3)

print(users_3)

#intersection
#difference