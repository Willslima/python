from event import Event
from online_event import OnlineEvent

ev = Event("Class of python")
ev2 = Event('Class of python', 'Rio de Janeiro')

ev3 = Event.create_online_event('Willian')
ev3.print_information()

print(ev3.calc_limit_of_person_area(35))


ev = OnlineEvent('Aula de Django','Rio de janeiro')
ev.print_information() 