from event import Event

class OnlineEvent(Event): #sintax to heritage
    def print_information(self):
        print(f'Event ID: {self.id}')
        print(f'Event name: {self.name}')
        print(f'Link to access event: {self.local}')
        print('-------------------')

@classmethod
def create_online_event(cls,name):
    event = cls(name, local=f'https://marked.com/event?id={cls.id}')
    return event

ev = OnlineEvent('ev')
ev.create_online_event('name')
print(ev.create_online_event('name').name)
print(ev.create_online_event('name').id)
print(ev.create_online_event('name').local)
