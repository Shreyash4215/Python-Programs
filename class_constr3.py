class Student:
    Total = 500
    
    def __init__(self,name,marks,gender):
        self.name = name
        self.marks = marks
        self.gender = gender
        print("Initialized...")
        
    def __len__(self):
        return self.marks
      
    def __str__(self):
        return "Name: %s | Marks: %s | Gender: %s"%(self.name,self.marks,self.gender)
        
    def __del__(self):
        print("Student Object Deleted")
        
a = Student('champ',450,'male')

print(a)
print('Marks: ',len(a))
del a        
      
