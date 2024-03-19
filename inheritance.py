class Elon:
    def __init__(self):
        print("profile Created...")
        
    def name(self):
        print("Elon musk")
    
    def age(self):
        print("40")
        
class SpaceX(Elon):
    def __init__(self):
        Elon.__init__(self)
        print("Company profile Created...")
    
    def name(self):
        print("SpaceX")
    
    def type(self):
        print("private space travel")    
        
        
a = SpaceX()
a.name()
a.age()
