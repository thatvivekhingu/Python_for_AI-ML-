# @class method decorator

class body():
    def show(self):
        print(f"The upadates value is print in self : {self.a}")
    a=45
  
    
obj=body()
obj.a=69
obj.show()

#o/p 
# The upadates value is print in self :69

    

    # this portion self is also contains the instance value but you want to take only class value so you define
    # @classmethod

class deco():
    

    @classmethod
    def show(cls):
        print(f"The decorator value is print in class is : {cls.a}")
    a=45
    
obj2=deco()
obj2.a=99
obj2.show()

#o/p:
#The decorator value is print in class is :45

