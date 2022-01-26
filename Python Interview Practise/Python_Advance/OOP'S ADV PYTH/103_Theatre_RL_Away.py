# from os import name
class movie:
    def __init__(self,name,actor,actress):
        self.name=name;
        self.actor=actor;
        self.actress=actress;
        # Dynamic Class Example
    def minfo(self):
        print("The name of movie is:",self.name)
        print("The name of movie is:",self.actor)
        print("The name of actress is:",self.actress)

List_of_Movies=[]
# m1=movie('spiderman','Tom holland',"cristiana oliver") STATIC APPROACH
while True:
 name=input("Enter the movie name:")
 actor=input("Enter Actor name:")
 actress=input("Enter Actress name:")
 m1=movie(name,actor,actress)
 List_of_Movies.append(m1)
 print("Movies added Sucessfully")
 option=input("Do you want to add more movies [Y||N]")
 if option.lower()=='n':
     break
print(List_of_Movies)
print("All movie INFORMATION")
# for(i=n:)
for movie in List_of_Movies: 
    movie.minfo()
    print("---------")
   



