class QueueList:

    class Knoop:

        def __init__(self,data=None,volgende=None) -> None:
            self.data = data
            self.volgende = volgende


    def __init__(self) -> None: # contstructor van de klasse QueueList
        self.k = None
        self.s = None

    def is_empty(self):
        return self.k == None

    def enqueue(self,data):
        hulp = QueueList.Knoop(data) # toevoegen van achteren
        if self.is_empty():
            self.k = hulp
        else:
            self.s.volgende = hulp
        self.s = hulp

    def front(self):
        return self.k.data

    def dequeue(self):
        if self.is_empty():         # eerst controleren
            return None
        x = self.k.data             # data van de kop bewaren
        if self.k == self.s:        # maar één element?
            self.k = None           # dan wordt de wachtrij leeg
            self.s = None
        else:
            self.k = self.k.volgende    # kop schuift één plaats op
        return x
         
    def invert(self):
        vorige = None
        huidige = self.k
        while huidige is not None:
            volgende = huidige.volgende     # bewaar de rest van de lijst
            huidige.volgende = vorige       # draai de pijl om
            vorige = huidige                # vorige schuift door
            huidige = volgende              # huidige schuift door
        self.k, self.s = self.s, self.k     # kop en staart wisselen