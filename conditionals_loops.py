age_data = input('How old are you\n')
age = int(age_data)

if age <= 11:
    print("I'm a Child")
elif age >= 12 and age <= 17:
    print("I'm a Young")
else:
    print("I'm an Adult")