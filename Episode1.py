# practice que 1 :  Write a program to create a dictionary
#  of Hindi words with values as their English translation.
#  Provide user with an option to look it up
'''d ={
    "apple":"safarjan",
    "mango":"Aam",
    "light":"prakash",
    "mouce":"chuha"
}
d1=input("enter words of you want to translate in hindi :")
print(d[d1]) # you enter mango o/p is Aam '''


#practice que 2 : Write a program to input eight numbers from the user and display all the unique numbers (once).
'''
s=set() #empty set
n=input("enter the number: ")
s.add(int(n))
n=input("enter the number: ")
s.add(int(n))
n=input("enter the number: ")
s.add(int(n))
n=input("enter the number: ")
s.add(int(n))
n=input("enter the number: ")
s.add(int(n))
n=input("enter the number: ")
s.add(int(n))
n=input("enter the number: ")
s.add(int(n))
n=input("enter the number: ")
s.add(int(n))
n=input("enter the number: ")
s.add(int(n))
print(s)
'''

# practice que 3 : Can we have a set with 18 (int) and '18' (str) as a value in it?
'''
s=set()
s.add("18")
s.add(18)
print(s)
# yes both values are excixt in set {'18',18}'''

# practice que 4 : What will be the length of following 
# set s:
# s= set()
#s.add(20)
#s.add(20.0)
#s.add('20')  length of s after these operations?

'''
s= {20,20.0,'20'}
print(len(s)) #o/p is 2  because 20==20.0 (agar value same hai toh bhale type matter nahi karta ) dono same hai toh ak hi baar o/p milega
print(s) #o/p {20,'20'}
'''


#   practice que 5 :
# s={}
#What is the type of 's'?
'''
      s={}                  # Disctionary
print(type(s)) ''' #o/p disctionary


# practice que 6 :
# Create an empty dictionary.
#  Allow 4 friends to enter their favorite language as value 
# and use key as their names. Assume that the names are unique.

d={}
name=input("enter the name :")
lang=input("enter the language :")
d.update({name:lang})

name=input("enter the name :")
lang=input("enter the language :")
d.update({name:lang})

name=input("enter the name :")
lang=input("enter the language :")
d.update({name:lang})

name=input("enter the name :")
lang=input("enter the language :")
d.update({name:lang})

print(d)

# Practice que 7 :  the names of 2 friends are same; what will happen to the program in problem 6?
'''
 name of two frd is same so first name vivek hase c lang,second vivek have c++ lang this 
method used in que 6 update value so updated value is contains like {'viviek:"c++"}
'''

# Practice que 8 : If languages of two friends are same; what will happen to the program in problem 6?

'''in this method two language are same so two times print the langaugae'''

# Practice que 9 : Can you change the values inside a list which is contained in set S?
#s = (8, 7, 12, "Harry", [1,2])
'''No, you cannot change the values inside the list [1,2] because the given set definition is invalid.
A set in Python can only contain immutable (unchangeable) elements.'''
