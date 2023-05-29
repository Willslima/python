names = []

option = input('You are sure to insert the name on list ? s/n')
while option != 'n':
    name = input('Type the name to insert on list\n')
    option = input('You are sure to insert the name on list ? s/n\n')
    names.append(name)
    print(names)
    