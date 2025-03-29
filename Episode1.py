#short the name 
Name="abcdefghijklmnopqrstuvwxyz"
nameshort=Name[0:3] #start with 0 and ends with 2 (excluding 3)
name=Name[1]
print(nameshort) #o/p abc
print(name) #o/p b
print(len(Name)) #o/p 26

b =Name[1:9:2] # contain 1 to 9 then first letter contain and take jump of 2 and conatins char
print(b) # bdfh