#not
#and 
#or

age = 29
of_legal_age = age >= 18
minor_of_age = not of_legal_age

print('Age: ', age)
print('Of legal age: ',of_legal_age)
print('minor of age: ',minor_of_age)

movie = 18
accompanied_by_parents = True

allowed = of_legal_age or accompanied_by_parents
print(allowed)