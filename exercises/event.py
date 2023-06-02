class Event:
    id = 1
    def __init__(self, name, local=''):
        self.name = name
        self.local = local
        self.id = Event.id
        Event.id += 1

    def print_information(self):
        print('ID event', self.id)
        print('Event name:', self.name)
        print('Event local:',self.local)
        print('------------')
    
    @classmethod
    def create_online_event(cls,name):
        event = cls(name, local=f'https://marked.com/event?id={cls.id}')
        return event
    
    @staticmethod
    def calc_limit_of_person_area(area):
        if area >= 5 and area < 10: #5 <= area < 10
            return 5
        elif area >= 10 and area <20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0

