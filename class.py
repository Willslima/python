class Person():
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
    def change_data(self, new_name, new_age, new_adress):
        self.name = new_name
        self.age = new_age
        self.adress = new_adress

me = Person('Will',29,'Domingos arevalo')
print(me.name)
print(me.adress)
print(me.age)

me.change_data('Willian',29,'Domingos')
print(me.name)
print(me.adress)
print(me.age)