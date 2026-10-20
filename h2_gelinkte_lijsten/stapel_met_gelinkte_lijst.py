class StackList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende


    def __init__(self): #contructor van de klasse stacklist
        self.t = None   # lege stapel maken - als je dit niet schrijft dan heeft de klasse geen eigenschappen. Nu heeft die de eigenschap t (top)

    def is_empty(self): # altijd self meegeven als argument
        return self.t is None

    def push(self, data):
        hulp = StackList.Knoop(data, self.t) # self.t dat is de volgende
        self.t = hulp

    def peek(self):
        if self.is_empty():
            return None
        return self.t.data

    def pop(self):
        if self.is_empty():
            return None
        x = self.t.data
        self.t = self.t.volgende
        return x
        



    