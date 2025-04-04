# file input/output in python

# first create  one file name is myfixe. txt then this file write content : hello genix what are you doing now??( not derived ,simply write )
# reading mode
f=open("myfile.txt")
data =f.read()
print(data)
f.close()



# when file not create first anfter code run then create automaticaly in file in vs code
# this is contain write mode
line="hello genix what are you doing now??"
f=open("myfile","w")
f.write(line)
f.close()


# if you don't write f.close()so you try:
# with statement 

with open("myfile.txt") as f:
    print(f.read())