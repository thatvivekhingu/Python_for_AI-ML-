class employee:
    langauage ="Python"
    Salary=45,000
  
    def __init__(self): # In python said this method as Dunder Method
        print("This method atomatically functions are called")

    def nitin(self): # create the functions 
        print(f"Nitin skill langaugae is {self.langauage} . salary is {self.Salary}")
    

Harry=employee()
Harry.nitin() #call the function




