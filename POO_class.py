#Class
class Event:
    def __init__(self, name):
        self.name = name
        self.local = 'Brasil'
    def change_event_name(self, new_name): #First arg is named with self
        self.name = new_name
        print(self.name)

eu = Event('Willian')
lena = Event('Lena')

print(eu.name)
print(eu.local)
print(lena)
