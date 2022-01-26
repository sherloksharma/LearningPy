class student: 
   '''This is documentation section'''
    
   def __init__(self):
    self.name='bishwash'
    self.rollno=27
    self.marks=83.5
   def talk(self):
    print("Hey there what's up",self.name)
    print("Your Roll no is:",self.rollno)

print(student.__doc__)
s=student()
print(s.name)
s.talk()