class student: 
   '''This is documentation section'''
    
   def __init__(self,name,rollno,marks):
    self.name=name
    self.rollno=rollno
    self.marks=marks
   def talk(self):
    print("Hey there what's up",self.name)
    print("Your Roll no is:",self.rollno)
    print("Your marks is:",self.marks)

# print(student.__doc__)
s=student('bishwash sharma','KATO75BCT027',83.5)
print(s.name)
print(s.rollno)
print(s.marks)
s.talk()