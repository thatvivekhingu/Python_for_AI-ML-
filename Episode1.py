# practice que chapter 6

# Write a program to find the greatest of four numbers entered by the user.
'''
a=int(input("enter the number of a :"))
b=int(input("enter the number of b :"))
c=int(input("enter the number of c :"))
d=int(input("enter the number of d :"))

if(a>b and a>c and a>d):
    print("A is gretaest value between four")
elif(b>a and b>c and b>d):
    print("B is gretaest value between four")
if(c>b and c>a and c>d):
    print("C is gretaest value between four")
if(d>b and d>c and d>a):
    print("D is gretaest value between four")
    '''


# PRACTICE QUE NUMBER 2 :
#  Write a program to find out whether a student has passed or failed if it requires a total of 40% 
# and at least 33%  in each subject to pass. Assume 3 subjects and take marks as an input from the user.
'''
a=int(input("enter the marks of a :"))
b=int(input("enter the marks of b :"))
c=int(input("enter the marks of c :"))

total= a+b+c 
avg= (total*100)/300

if(avg > 40 and a>33 and b>33 and c>33):
    print("You are pass in exam",avg)
else:
    print("you are fail",avg)
'''
    
# Practice Que 3 :
#  A spam comment is defined as a text containing following keywords:
#"Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
 
'''
spam_msg1="Make a lot of money"
spam_msg2="buy now"
spam_msg3="subscribe this"
spam_msg4="click this"

comment =input("Enter the comment:")
if(comment == spam_msg1 or comment==spam_msg2 or comment==spam_msg3 or comment==spam_msg4):
    print("This is faraud message , Updates your security")

else:
    print(" comment is under safety ")
    '''

#Practice Que no 4 :
# Write a program to find whether a given username contains less than 10 characters or not.
'''
username=input("Enter the username :")

if(len(username)<10):

    print("Name having less than 10 character which is :",len(username))
elif(len(username)==10):

    print("Name having equal 10 character which is :",len(username))
else:
     print("Name having more than 10 character  which is : ",len(username))


'''

#Practice que 5 : 
# Write a program which finds out whether a given name is present in a list or not.
'''
list_name=["vivek","vaibhavi","sakshi","harsh"]
name=input("Enter the name :")

if(name in list_name):
    print("This name is conatins in this list")

else:
    print("This name is not  conatins in this list")
'''

#Practice que number :6 Write a program to find out whether a given post is talking about "Harry" or not.
'''
post ="harry is a famouse youtuber and harry also have a knowledge about content creator"
comment = input("enter the comment in post :")

if("harry".lower() in comment.lower()):
    print("This comment said about the harry")

else:
     print("This comment is not said about the harry")'''