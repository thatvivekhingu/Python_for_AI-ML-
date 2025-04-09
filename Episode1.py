# MUltiple Inheritance in python

class First:
    name="Vivek"
    skills="AI and ML"
    def job(self):
        print(f"Employee name is {self.name} and his skills in {self.skills}")

class Second:
    Language="Python"
    Hobby="Coding"
    def Expierence(self):
        print(f"Language is {self.Language} and his hobby is  {self.Hobby}")

class main(First,Second):
    def CV(self):
        print(f"Name of employee is {self.name} and its hobby is {self.Hobby}")


obj=main()
obj.CV()
obj.job()
obj.Expierence()