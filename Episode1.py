# Object oreinted programming in python 

'''
class vivek:          # create a class
    langauage="python"
    job="Bnaglore"
    salary="30,000"


It=vivek()  # create object "It"
It.skills ="Ai and ml"
print(It.langauage,It.salary,It.job,It.skills)
'''

# Same parameter 
class employee:
    langauage ="Python"
    Salary=45,000
    trip="Goa"
    Game="BGMI"

    def nitin(self): # create the functions 
        print(f"Nitin skill langaugae is {self.langauage} . salary is {self.Salary}")
    def kamal(self): # create the functions 
        print(f"Kamal going to trip in  {self.trip} . salary is {self.Game}")

    @staticmethod  # this method not contains any other object only staticly run    
    def sakshi():
        print("My life, My rules")

Harry=employee()
Harry.nitin() #call the function
Harry.kamal()
Harry.sakshi()



