from event import Event

class OnlineEvent(Event): #sintax to heritage
    def print_information(self):
        print(f'Event ID: {self.id}')
        print(f'Event name: {self.name}')
        print(f'Link to access event: {self.local}')
        print('-------------------')
