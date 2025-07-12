#string
s1 = "python"
s2 = 'programming'
s3 = """
This is multi line 
string.
"""
print(s1)
print(s2)
print(s3)
print(s1[3])
print(s1[-3])
print(s1[1:4])
#coomon string methods
str1 = "Alice, in, wonderland"
#lower()-converts string to lower case
print(str1.lower())
#upper()-converts string to upper case
print(str1.upper())
#title()-caplitalizes each word
print(str1.title())
#strip()- removes spaces from the start and end of the str
print(str1.strip())
#replace("a","b")-a will be replaced by b
print(str1.replace("Alice","Mithun"))
#find("sub") - finds the substring
print(str1.find("in"))
#count("sub")
print(str1.count("Mithun"))
#startswith("str")
print(str1.startswith("M"))
#endswith()
print(str1.endswith("d"))
#split()- method returns a list where the text btwn specified separator
print(str1.strip(","))

name = "Mithun"
roll = 19
branch = "AIML"
print("My Name Is",name,"roll no is",roll,"and branch is",branch)
print("My Name Is "+name+" roll no is "+str(roll)+" and branch is "+branch)

#string formatting (f string)
print(f"My Name Is {name} roll no is {roll} and branch is {branch}" )
#.format
print("My Name Is {} roll no is {} and branch is {}".format(name,roll,branch))

print("Good"+"Morning")#concatination
print("GM "*3)#reptition
print("py" in "python")#membership op

#condition statements
if 20>30:
    print("if block executd ")
else:
    print("else block executed") 


marks=int(input("enter marks :"))
#marks=int(mark)
if marks>=90:
    print("A grade")
elif marks>=80:
    print("B grade")
elif marks>=70:
    print("C grade")
elif marks>=60:
    print("D grade")
else:
    print("E grade")           
        
age = int(input("enter ur age:"))
if age>=18:
    print("You can vote")
else:
    print("You Cant vote")     

#while loop
i=0
while i<5:
    print(i)
    i+=1   
#for loop
for j in range(1,5):
    print("for loop no",j)

for j in range(1,10,2):#start,end-1,increment
    print("for loop no",j)    

for j in range(10,1,-2):
    print(j)

for j in range(1,11):
    if j==5:
        break
    print(j)

for j in range(1,11):
    if j==7:
        continue
    print(j)

for letter in "words":
    print(letter) 


psd = "asdf"
for i in range(3):
    password = input("Enter Password:")
    if(password==psd):
     print("!Welcome")
     break
    else:
     print("Access Denied")           

#functions
def greet():
    print("Hello,Good Morning")

greet() #calling the function 

def greet1(user):
    print("Hello,Good Morning",user)

greet1("charan")  

def greet2(user="ram"):
    print("Hello,Good Morning",user)

greet2()

#variable length arguments
#*args - passes tuples as arguments ,
#**kwargs - dictionary will be passed as arguments

def greettuple(*args):
    for name in args:
        print(f"Hello,{name}!")

greettuple("Alice","Bob","Charlie")

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

display_info(name="David",college="PU",branch="AIML")

def demo(*args,**kwargs):
    print("Args tuple elements",args)
    print("Kwargs Dictionary elemnts",kwargs)

demo (1,2,"apple",name="David",college="PU",profession="Sales")

def squareFunc(x):
    return x**2

print(squareFunc(4))

num1 = int(input("enter num 1:"))
num2 = int(input("enter num 2:"))
operation = input("enter operation(+,-,*,/,**):")
if operation == "+":
   print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
elif operation == "**":
    print(num1**num2)
else:
    print("Invalid choice")    

x = lambda a: a+10
print(x(5))

y=lambda a,b,c : a+b+c
print(y(2,3,4))

#Modules
import math
print(math.sqrt(4))
print(math.pi)
      
import random
print(random.randint(1,10))
    
from math import sqrt
print(sqrt(16))   

import datetime as dt#alias
print(dt.datetime.now())

import mymodule
mymodule.mymodulefunction() 

x = 1#global
def showNum():
    global x
    x=5#local
    print("value of x as a local variable",x)
showNum()
print("value as global variable",x)

f = open("file1.txt",'r')
content = f.readline()
print(content)
content1 = f.readlines()
for l in content1:
    print(l)

text = f.read()
print(text) 

f=open("file1.txt",'w')
f.write("Hello,\n")
f.write("Good Morning\n")   
lines = ["Line1\n","Line2\n","line3\n"]
f.writelines(lines)
f.close()

f=open("file1.txt",'a')
f.write("6.new line")
f.close()

import os
print(os.path.exists("file1.txt"))
print(os.path.exists("file2.txt"))
#os.rename("file1.txt","NewFile.txt")
os.remove("NewFile.txt")