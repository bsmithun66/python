# object
# class person:
#      def __init__(self,name,age):
#           self.name = name
#           self.age = age
#      def greet(self):
#           print(f"Hello {self.name} of age {self.age}")      
          
# a = person("alice",29) #object
# print(a.name)
# a.greet()

# class car:
#      def __init__(self,Brand,Model,Year):
#           self.Brand = Brand
#           self.Model = Model
#           self.Year = Year
#      def drive(self):
#           print(f"car is of Brand {self.Brand} and published in the year of {self.Year}  ")
# b = car("BMW",0000,2016)               
# b.drive() 
        
#inheritance
# class Father:
#      def  fatherWealth(self):
#           print("papa ka paisa")
# class Mother:
#      def Hobbies(self):
#           print("Mulitiple inheritance")          
# class Ram(Father,Mother):
#      def salary(self):
#           print("earned by ram")
# f = Father()
# b = Ram()
# b.Hobbies()                                               
# b.salary()
# b.fatherWealth()     
# f.fatherWealth()
               
# class vehicle:
#      def __init__(self,brand):
#           self.brand=brand
# class car(vehicle):
#      def __init__(self, brand,model):
#           super().__init__(brand)          
#           self.model = model
# c = car("Toyato","camry")
# print(c.brand,c.model)          


# #polymorphism

# class bird:
#      def sound(self):
#           print("chirp")

# class Cat:
#      def sound(self):
#           print("Meow")

# sparrow = bird()
# sparrow.sound()
# kitten=Cat()
# kitten.sound()

# #method overloading
# class Parents:
#      def show(self):
#           print("parents method")
# class child(Parents):
#      def show(self):
#           print("Childs method")

# obj = child()
# obj.show()

# #operator overloading
# class Point:
#      def __init__(self,x,y):
#           self.x=x
#           self.y=y

#      def __add__(self,other):
#           return Point(self.x+other.x,self.y+other.y)
# p1 = Point(2,3)
# p2 = Point(3,4)
# p3 = p1+p2
# print(p3.x,p3.y)     
          
# class student:
#      def __init__(self,name,roll):
#           self.name=name
#           self.roll=roll

#      def __eq__(self, other):
#           return self.roll == other.roll
     
# s1 = student("Alice",101)
# s2 = student("Bob",101)
# s3 = student("Charlie",102)
# print(s1==s2)
# print(s1==s3)

# class book:
#      def __init__(self,title,page):
#           self.title=title
#           self.page=page

#      def __add__(self,other):
#           return (self.page+other.page)
     
# p1 = book("",123)     
# p2 = book("",321)
# print(p1+p2) 

# class Protected:
#      def __init__(self):
#           self._age = 30 #protected attribute _age

# class Sub(Protected):
#      def display_age(self):
#           print(self._age) #protected members accessible in subclass

# obj = Sub()
# obj.display_age()          

     
# class Bankacc():
#      def __init__(self,balance):
#           self.__balance=balance
#      def deposit(self,amount):
#           self.__balance += amount
#      def get_balance(self):
#           return self.__balance     
     
# acc = Bankacc(1000)
# acc.deposit(50)
# print(acc.get_balance())

# #Abstraction
# from abc import ABC,abstractmethod

# class Vehicle(ABC):
#      @abstractmethod
#      def start_engine(self):
#        pass
# class Car(Vehicle):
#           def start_engine(self):
#             print("Car engine started")


# class Bike(Vehicle):
#           def start_engine(self):
#             print("Bike engine started")
          
# c = Car()
# c.start_engine()
# b = Bike()
# b.start_engine()


#Exception Handling
# try:
#     num  = int(input("enter a number: "))
#     x=10/num
#     print(x)
# except ZeroDivisionError:
#      print("Cannot divide by 0")
# except ValueError:
#      print("please enter a valid number")     
# else:
#      print("sucess")

# age = int(input("Enter a num:"))
# if age<18:
#      raise ValueError("Voter age must be above 18")
# else:
#      print("cast ur vote")

# try:
#      name = input("enter ur name: ")
#      if name=="":
#       raise ValueError("name cant be empty")
#      #else:
#       #print("your name is ",name)
# except ValueError:
#    print("Error Handled")      


#Q1.write a program to find if the given string is a palindrome or not
# str = input("Enter a string")
# if str==str[::-1]:
#     print("is palindrome")
# else:
#     print("is not palindrome")    


#Q2.program to find 2nd largest number without using sort fun

#Q3. create a function that counts the numbers of vowels in a given string
# str = input("enter ur name")
# def c_vowels(s):
#     vowels="aeiouAEIOU"
#     return sum(1 for char in s if char in vowels)
# print(c_vowels(str))    

v = ["a", "e", "i", "o", "u"]

text = input("enter a string")
vowelCount = 0

for i in text:
    if i in v:
        vowelCount+=1

print(vowelCount)

# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno

# class marks(student):
#     def __init__(self, name, rollno,c1,c2,c3):
#         self().__init__(name,rollno)
#         self.marks(c1,c2,c3)


            
    


    
        



    