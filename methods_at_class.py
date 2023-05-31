class Event:
    def instance_method(self):
        return('instance method call', self)
    
    @classmethod
    def class_method(cls):
        return ('method of class call', cls) #cls == class

    @staticmethod #@staticmethod is required
    def static_method():
        return 'static method'
    
ev = Event()
a = ev.instance_method() #Event.instance_method(ev)
print(a)

b = Event.class_method() #Event.class_method(Event)
print(b)

c = Event.static_method() #Event.static_method()
print(c)