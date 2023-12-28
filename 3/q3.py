from q1 import Disk
from q2 import Pole

class Hanoi(object):
    def __init__(self, n=3,start="A",workspace="B",destination="C"):
        self.start = Pole(start,0,0)
        self.workspace = Pole(workspace,150,0)
        self.destination = Pole(destination,300,0)
        self.start.showpole()
        self.workspace.showpole()
        self.destination.showpole()
        for i in range(n):
            self.start.pushdisk(Disk("d"+str(i),i*150,20,(n-i)*30))

    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)
        # disk.showdisk()
    
    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
            # self.showtowers()
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            # self.showtowers()
            self.move_tower(n-1,w,d,s)
    
    def solve(self):
        self.move_tower(self.start.size,self.start,self.destination,self.workspace)

h = Hanoi()
h.solve()

        