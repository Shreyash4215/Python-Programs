class Student:
    Total = 500
    
    def __init__(self,marks):
        self.marks = marks
        print("Initialized...")
        
    def findLoss(self):
        return self.Total - self.marks
      
    def findPercentage(self):
        return self.marks / self.Total*100
      
a = Student(marks=450)
#a = Student(450)

print("Total Marks: ",a.Total)
print("loss Marks: ",a.findLoss())
print("Percentage: ",a.findPercentage())