
# NOTE the Python Standard Libary  is based on the consept of class and object 

# Defining Clases 

# class Class_name:
#     statement1
#     statement2
#     statement3
#     . 
#     . 
#     . 
#     statementN
    

# tip A class can be defined in a function or whith an if statement

# NOTE Python does not require the new operator to create an object. 





# #program to access class variable using class object 
# class abc:
#     var= 10

# a= abc()
# # a= a.var    #this method is only for more clear understanding perpose
# print(a.var)





# NOTE : self in Python workd in the same way as the "this" pointer in c++


# # Program to access class members using the class object . 
# class abc:
#     ver = 10
#     def display(self):             # NOTE you can give any name for the self parameter, but you should not do so 

#         print("in a class method")

# obj= abc()
# print(obj.ver)
# obj.display()






# # Program illusttrating the use of __init__() method 

# class abc():
#     def __init__(self,val):
#         print("in class method....")
#         self.val= val
#         print("the value is :",val)
#         print("the value is :",self.val)

# obj= abc(10)









# # Program to differentiate between class and object variables 
# class abc():
#     class_var = 0
#     def __init__(self,var):
#         abc.class_var+=1
#         self.var = var
#         print("the object value is :",var)
#         print("The value of class variable is :", abc.class_var )

# obj1= abc(10)
# obj2= abc(20)
# obj3= abc(30)














# # Program to illustrating the modification of an instance variable 
# class number():
#     even= 0
#     def check(self,num):
#         if num%2==0:
#             self.even = 1
        
#     def even_odd(self,num):
#         self.check(num)
#         if self.even==1:
#             print("number is even")
#         else:
#             print("number is odd")
        

# n= number()
# n.even_odd(15)








# # Program to modifying a mutable type attribute 
# class number():
#     even =[]
#     odd=[]

#     def __init__(self,val):
#         # self.num= val
#         if val%2==0:     # you are also use self.num of val variable 
#             number.even.append(val)
#         else:
#             number.odd.append(val)
            

# n1= number(21)
# n2= number(33)
# n3= number(42)
# n4 = number(48)
# n5 = number(54)
# n6 = number(90)

# print("even numbers:",number.even)
# print("odd number",number.odd)










# # Program to  illustrate the use of __del__() method 
# class abc():
#     a_var = 0      # class variable 
#     def __init__(self,var):
#         abc.a_var+=1
#         self.var1=var    # object variable 
#         print("the object val is",self.var1)
#         print("the value of class variable is :",abc.a_var)
    
#     def __del__(num):   # you can also use  num in place of the self
#         abc.a_var-=1
#         print("object with value %d is gowing out of scope " %num.var1)


# obj1 = abc(10)
# obj2= abc(20)
# obj3= abc(30)
# obj4= abc(40)

# del obj1
# del obj2
# del obj3
# del obj4






# # Program to illustrate the use of special methods in python  class 
# class abc():
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age
    
#     def __repr__(self):
#         return repr(self.age)
    
#     def __len__(self):
#         return len(self.name)
    
#     def __cmp__(self,obj):
#         return self.age - obj.age


# obj = abc("vaibhav",21)
# print("The value stored in object is :", repr(obj))
# print("the length of name is:",len(obj))
# obj1 = abc("snehal", 20)
# val = obj.__cmp__(obj1)
# if val==0:
#     print("both are equl")
# elif val== -1:
#     print("first value is less than second ")
# else:
#     print("second value is less than first")












# # Program to demonstrate the use of __getitem__() and __setitem__() methodas 


# class number():
#     def __init__(self,mylist):
#         self.mylist1=mylist

#     def __getitem__(self,index):
#         return self.mylist1[index]
        
#     def __setitem__(self,index,val):
#         self.mylist1[index]=val
# num = number([1,2,3,4,5,6,7,8,9,])
# print(num[4])
# num[4]= 10
# print(num.mylist1)












# # Program to illustrate the difference between public and private variable 
# class class1():
#     def __init__(self,var1,var2):
#         self.var1= var1
#         self.__var2= var2

#     def display(self):
#         print("from class method, var1 ",self.var1)
#         print("from class method, __var2 ",self.__var2)

# obj = class1(10,20)
# obj.display()

# print("from the main module var1",obj.var1)
# print("from the main module var2",obj.__var2)




# # Program to illustrate the use of a private method 
# class abc():
#     def __init__(self,var):
#         self.__var= var
#     def display(se):
#         print("form class method, var = ",se.__var)



# obj = abc(10)
# obj.display()







# # Program to call a class method from another method of the same class. 
# class abc():
#     def __init__(self,var):
#         self.var= var
#     def display(self):
#         print("var is : ",self.var)
#     def add_2(self):
#         self.var +=2
#         self.display()
# obj = abc(10)
# obj.display()
# obj.add_2()










# # program to show how a class method calls a functoon defined in the golbal Namespace
# def scale_10(var):
#     return var*10
# class abc():
#     def __init__(self,var1):
#         self.var= var1
#     def display(self):
#         print("the value is ",self.var)
#     def modify(self):
#         self.var=scale_10(self.var)
    


# a = int(input("enter the number:"))
# obj = abc(a)
# obj.display()
# obj.modify()
# obj.display()










# # Program to add variables to a class at run- time 

# class abc():
#     def __init__(self,var):
#         self.var= var
    
#     def display(self):
#         print("variable is ",self.var)


# a = abc(10)
# a.display()
# a.new_var= 20
# print("new variable  is ",a.new_var)
# a.new_var = 30
# print("new variable after modifying  ",a.new_var)
# del a.new_var
# print("new variable after deletion = ",a.new_var)









# # Program to demonstrate the use of getattr(), seatr(), and delattr(). functions 

# class abc():
#     def __init__(self,var):
#         self.var1=var
    
#     def display(self):
#         print("the value is :",self.var1)
    


# obj = abc(10)
# obj.display()

# print("check if object has attribute var ..... ",hasattr(obj,'val'))
# getattr(obj,'var1')

# setattr(obj,"var1",50)
# print("after setting value, var is : ",obj.var1)

# setattr(obj,'count',11)
# print("new variable count is created and its value is :",obj.count)

# delattr(obj,'var1')
# print("after deleting the attribute, var is :", obj.var1)










# Program to demonstrate the use of built-in- class attributes 

# class abc():
#     """this is a semple abc class for practicess"""
#     def __init__(delf, val1,val2):   # i know i using 😁delf😁 on self place! but you can also use diffrence name on place self .😂😅
#         delf.varl= val1
#         delf.var2=val2
    
#     def display(delf):
#         print("frist value is :",delf.varl)
#         print("second value is :",delf.var2)
    



# a = 10
# b= 20
# obj = abc(a,b)
# obj.display()

# print("object.__dict__ - ",obj.__dict__)
# print("object.__doc__ - ",obj.__doc__)
# print("class.__name__ - ",abc.__name__)
# print("object.__module__ -",obj.__module__)
# print("class.__bases__",abc.__bases__)






# ex - when an objext's reference count reaches zero python recollects the memory used by it. 
# consider the following examples which  illustrate the way in which reference count changes for a given object. 







# var1= 10
# var2=var1
# var3=[var2]
# # var2= 50
# # var3[0]= -1
# # del var1
# print(type(var3))
# print(type(var2))
# print(id(var1))
# print(id(var2))
# print(id(var3))







# # write a Program that uses class to store the name and marks of students. Use list to store the marks in three subjects. 

# class student():
#     def __init__(self,name):
#         self.name1=name
#         self.marks=[]
    
#     def entermarks(self):
#         for i in range(3):
#             m= int(input(f"enter the  of {self.name1} in subject {i+1} : "))    # using 😁f string😎 method  
#             self.marks.append(m)

#     def display(self):
#         print(f"{self.name1} got {self.marks}")


# s1 = student('vaibhav')
# s1.entermarks()

# s2 = student("mauli")
# s2.entermarks()
# s1.display()
# s2.display()










# # write a program with class employee that keeps a track of the number of employess in an organization and also store their name. designation, and salary detail. 
# class empl:
#     emp= 0 
#     def __init__(self,name,desig,salary):
#         self.name1=name
#         self.desig=desig
#         self.salary=salary
#         empl.emp+=1

#     def display_count(self):
#         print(f"there are {empl.emp} employees ")


#     def display_detail(self):
#         print("name",self.name1,"disignation",self.desig,"salary",self.salary)



# e1 = empl("gajanan","farma",50000)
# e2 = empl("sanket","engineer",35000)
# e3= empl("vaibhav","devloper",45000)
# e3.display_count()
# print("detail of second employee - \n")
# e2.display_detail()








# # write a program that has a class person storing name and date of birth (DOB) of a person. The program should subtract the DOB from today's date to find you whether a person is eligible to vaote or not 

# import datetime
# class person:
#     def __init__(self,name,dob):
#         self.name=name
#         self.dob= dob
    
#     def check(self):
#         today=datetime.date.today()
#         age=today.year-self.dob.year

#         if today<datetime.date(today.year,self.dob.month,self.dob.day):
#             age-=1
#         if age>=18:
#             print(self.name,"congratulation you are eligible to vote.")
        
#         else:
#             print(self.name,"sorry you should be at least 18 years of age to cast your vote")


# p= person("vaibhav",datetime.date(2005,4,17))
# p.check()











# # write a program that has a class circle. Use a class variable to define the value of constant PI Use this class variable to calculate area and circumference of a circle with specified radius .
# class circle:
#     pi = 3.14159
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return circle.pi*self.radius*self.radius
    
#     def circumference(self):
#         return 2*circle.pi*self.radius 
        
# c= circle(7.5)
# print("area =",c.area())
# print("circumference",c.circumference())
















# # write a program that has a class student that stores roll number, name and marks (in three subject) of the students. Display the information (roll number, name and total marks ) stored about the student. 

# class student():
#     __marks= []
#     def set_data(self,r,n,m1,m2,m3):
#         student.__roll=r
#         student.__name=n
#         student.__marks.append(m1)
#         student.__marks.append(m2)
#         student.__marks.append(m3)
    
#     def display(self):
#         print("student details->")
#         print("roll number is ",student.__roll)
#         print("name is : ",student.__name)
#         print("mark is 3 subject ",self.total())

#     def total(self):
#         m= student.__marks
#         return m[0]+m[1]+m[2]


# roll= int (input("enter the roll number :"))
# name = input("enter the name :")
# m1=int(input("enter the marks in first subject:"))
# m2 =int(input("enter the marks in second subject:"))
# m3=int(input("enter the marks in third subject:"))

# s1=student()
# s1.set_data(roll,name,m1,m2,m3)
# s1.display()














# # write a class rectangle that has attributes length and breadth and  a method area which returns the area of the ractagle 

# class ractangle():
#     def get_data(self):
#         ractangle.len=float(input("enter the length of ractangle:"))
#         ractangle.breadth= float(input("enter the breadth of ractangle:"))
#     def show_data(self):
#         print("length is :",ractangle.len)
#         print("breadth is :",ractangle.breadth)

#     def area(self):
#         print("area of ractangle is :",ractangle.len*ractangle.breadth)


# r1 = ractangle()
# r1.get_data()
# r1.show_data()
# r1.area()














# # write a program that has a class fraction with attributes numarator and denominator. Enter the value of attributes and print the fraction in simplified from . 
# class fraction:
#     def get_data(self):
#         self.__num= int(input("enter the numerator :"))    
#         self.__deno= int(input("enter the denominator:"))
#         if self.__deno==0:
#             print("fraction not possible ")
#             exit()
    
#     def display(self):
#         self.__simplify()
#         print(self.__num,"/",self.__deno)


#     def __simplify(self):
#         print("the simplified fraction is :")
#         commen_deviser  = self.__GCD(self.__num,self.__deno)
#         self.__num = self.__num/commen_deviser
#         self.__deno = self.__deno/commen_deviser


#     def __GCD(self,a,b):
#         if b==0:
#             return a
#         else:
#             return self.__GCD(b,a%b)

# f= fraction()
# f.get_data()
# f.display()

















# # write a program that has a class store which keeps a record of code and price of each product. Display a menu of all products to the user and promots him to enter the quantity of each item required. generated a bill and display the total amount

# class store:
#         __item_code=[]
#         __price= []

#         def get_data(self):
#             for i in range(5):
#                 self.__item_code.append(int(input("enter the code of item :")))
#                 self.__price.append(int(input("enter the price of item:")))

#         def display(self):
#             print("Item code \t Price")
#             for i in range(5):
#                 print(self.__item_code[i],"\t\t",self.__price[i])
        

#         def calculate(self,quant):
#             total_amount= 0
#             for i in range(5):
#                 total_amount= total_amount+self.__price[i]*quant[i]
            
#             print("******************* Bill ************************")
#             print("item \t price \t quantity \t subtotal")
#             for i in range(5):
#                 print(self.__item_code[i],'\t',self.__price[i],"\t",quant[i],'\t',quant[i]*self.__price[i])

#             print("****************************************************")
#             print("Total = ",total_amount)


# s= store()
# s.get_data()
# s.display()
# q=[]
# print("enter the quantity of each item : ")
# for i in range(5):
#     q.append(int(input()))

# s.calculate(q)












# # Write a program that has a class numbers with values stored in a list. write class method to find the largest value 
# """Program to use a cinstructor to create an array and find the largest element from that array """

# class numbers:
#     def __init__(self):
#         self.values=[]
    
#     def find_max(self):
#         max=''
#         for i in self.values:
#             if i>max:
#                 max=i
        
#         print("maximum element : %r"%max)

#     def insert_element(self):
#         value= input("enter a value: ")
#         self.values.append(value)

# x= numbers()
# ch='y'
# while( ch=='y'):
#     x.insert_element()
#     ch=input("do you wish to enter more elements?")

# x.find_max()











# # write a class that stores a string and its status details such as number of uppercase character, vowels, consonants, spaces, etc . 

# class string:
#     def __init__(self):
#         self.vowels= 0
#         self.spaces=0
#         self.consonants=0
#         self.uppercase=0
#         self.lowercase=0
#         self.string=str(input("inter string: "))

#     def count_uppercase(self):
#         for letter in self.string:
#             if letter.isupper():
#                 self.uppercase+=1

#     def count_lowercase(self):
#         for letter in self.string:
#             if letter.islower():
#                 self.lowercase+=1
            
#     def count_vowel(self):
#         for letter in self.string:
#             if letter in ('a','e','i','o','u') or letter in ('A','E','I','O','U'):
#                 self.vowels+=1

#     def count_space(self):
#         for letter in self.string:
#             if letter==' ':
#                 self.spaces+=1

#     def count_consonants(self):
#         for letter in self.string:
#             if letter not in ('a','e','i','o','u','A','E','I','O','U',' '):
#                 self.consonants+=1
            
#     def compute_state(self):
#         self.count_uppercase()
#         self.count_lowercase()
#         self.count_vowel()
#         self.count_space()
#         self.count_consonants()

#     def show_state(self):
#         print('vovels is ',self.vowels)
#         print('consonants is :', self.consonants)
#         print('spases is :',self.spaces)
#         print('upppercase is : ',self.uppercase)
#         print('Lowercase is ',self.lowercase)


# s= string()
# s.compute_state()
# s.show_state()







# # write a program that uses datetime module within a class. Enter manufacturing date nad expiry date of the product. The program must display the years, months, and days that are left for expriry. 

# import datetime
# class product:
#     def __init__(self):
#         self.manufacture = datetime.datetime.strptime(input("enter manufacturing date (mm/dd/yyyy):"),'%m/%d/%Y')
#         self.expiry= datetime.datetime.strptime(input("enter expiry date (mm/dd/yyyy"),'%m/%d/%Y')

#     def time_expire(self):
#         today= datetime.datetime.now()
#         if (today>self.expiry):
#             print("Product has already expired.")
#         else:
#             time_left=self.expiry.date() - datetime.datetime.now().date()
#             print("Time left :",time_left)
#     def show(self):
#         print("expiry :",self.expiry)
#         print("manufacturing:",self.manufacture)


# x=product()
# x.time_expire()
# x.show()












# # write a program to deposite or withdraw money in a bank account .

# class accounts:
#     def __init__(self):
#         self.__balance=0
#         print("new account created...")

#     def deposit(self):
#         amount= float(input("enter amount to deposite: "))
#         self.__balance+=amount
#         print("new balance : %f" %self.__balance)

#     def withdraw(self):
#         amount=float(input("Enter amount to withdrowl : "))
#         if amount>self.__balance:
#             print("Insufficient balance")
#             pass
#         else:
#             self.__balance -= amount
#             print("total amount: %f:"%self.__balance)

#     def enquiry(self):
#         print("Amount:",self.__balance)

# account= accounts()
# account.deposit()
# account.withdraw()
# account.enquiry()



















# # write a menu driven program that keeps record of books and journats available in a library.

# from random import choice


# class Book:
#     def __init__(self):
#         self.tital=''
#         self.author=''
#         self.price=0

#     def read(self):
#         self.tital=input("Enter book Tital : ")
#         self.author=input("Enter Book Author :")
#         self.price=int(input("Enter Book Price :"))
    
#     def display(self):
#         print("tital :",self.tital)
#         print("Author :",self.author)
#         print("Price :",self.price)
#         print("\n")


# my_book=[]
# ch='y'
# while (ch=='y'):
#     print('''
#     1.Add New Book 
#     2. Display Books
#     ''')
#     choice=int(input("inter choice :"))
#     if choice==1:
#         book=Book()
#         book.read()
#         my_book.append(book)
    
#     elif choice==2:
#         for i in my_book:
#             i.display()
#     else:
#         print('Invalid Choice ')
    
#     ch=input("do you want to continue...")

# print("thank You ............")














# # NOTE class methods are marked with a class decoratror           # confused  :(

# # program to demonstrate the use of classmethod 

# class ractangle:
#     def __init__(self,length,breadth):
#         self.len=length
#         self.brea=breadth
    
#     def area(self):
#         return self.len*self.brea

#     @classmethod
#     def square(cls,side):
#         return cls(side,side)




# a= ractangle.square(10)
# print("area = ",a.area())
















 
#code with harry code //////////////////////////////////////////////////////              totally solid  consept  and proude to me this next level approch  

# class emp:
#     increment=1.5
#     no_of_emp=0
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
#         emp.no_of_emp+=1

#     def increase(self):
#         self.salary= self.salary*self.increment

#     @classmethod                             # for  classe variable change value  
#     def change_increment(cls,amount):    # you not use @classmethod decoretor so you can only chane variable value 
#         cls.increment=amount


# vaibhav= emp('vaibhav','nagargoje',50000)
# maggi= emp('maggi','yeppi',20000)
# print(f'first name is {vaibhav.fname} and last name is {vaibhav.lname} and his salary is {vaibhav.salary}')
# # vaibhav.increase()
# print(f'first name is {maggi.fname} and last name is {maggi.lname} and his salary is {maggi.salary}')
# emp.change_increment(2)   #for class variable change value 
# vaibhav.increase()
# print(f'first name is {vaibhav.fname} and last name is {vaibhav.lname} and his salary is {vaibhav.salary}')


# maggi.increase()
# print(f'first name is {maggi.fname} and last name is {maggi.lname} and his salary is {maggi.salary}')





























# # program to illustrate static methid .           #confused



# class choice:
#     def __init__(self,sub):
#         self.subject=sub

#     @staticmethod
#     def validate(sub):
#         if 'os' in sub:
#             print("this option is no longer available.")
#         else:
#             return True

# subject= ['dsa','csa','hos','math','electronic']
# if all(choice.validate(i) for i in subject):
#     ch=choice(subject)
#     print("you ave been alloteed the subjects:",subject)











# //////////////////////////////////////////////////////////////////////// Getters, Setters, @property, and @ deleter .//////////////////////////////////////////////////////////////////////////////////////////////////////



# # program that uses get and set function to retrieve and set a value .


# class sample:
#     def __init__(self,val):
#         self.val=val
    
#     def get_val(self):
#         return self.val

#     def set_val(self,val):
#         self.val=val


# s=sample(0)
# s.set_val(10)
# print(s.get_val())











# # program to demonstrate @property and @setter 

# class sample:
#     def __init__(self,val):
#         self.val2=val
#     @property
#     def val(self):
#         return self.__val
#     @val.setter
#     def val2(self,val2):
#         self.__val=val2


# s=sample(20)
# s.val=100
# print(s.val)








# setter and deleter and getter and progerty decoretor  code with harry////////////////////////////////////////////////////


# class emp:
#     increment = 2
#     no_of_emp=0
    
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
#         # self.email=fname+lname+'@email.com'
#         emp.no_of_emp+=1

#     def increase(self):
#         self.salary=int(self.salary*self.increment)

#     @property
#     def email(self):
#         if self.fname==None:
#             print("email not set ")
        
#         else:
#             return self.lname+'.'+self.fname+'@gmail.com'

#     @email.setter
#     def email(self,given_mail):
       
#         name_list=given_mail.split('@')[0].split('.')
#         print(name_list)
#         self.fname=name_list[0]
#         self.lname=name_list[1]
#     @classmethod
#     def change_increment(cls,amount):
#         emp.increment= amount

#     @classmethod
#     def form_str(cls,empstring):
#         fname,lname,salary=empstring.split("-")
#         return cls(fname,lname,salary)

#     @email.deleter
#     def email(self):
#         self.fname=None
#         self.lname=None

    


# vaibhav= emp('vaibhav','nagargoje',2000)
# print(vaibhav.lname)
# emp.change_increment(5)
# vaibhav.increase()
# print(vaibhav.salary)
# print(vaibhav.email)
# vaibhav.lname='khan'
# print(vaibhav.email )
# vaibhav.email='vaibhv.sing@email.com'
# print(vaibhav.email)
# del vaibhav.email
# print(vaibhav.email)















# # write a program that has a class point. Define another class location which has two objects (location and destinations ) of class point. also define a function in location that print the reflecation on the x axis 

# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def get(self):
#         return (self.x,self.y)
    
# class location:
#     def __init__(self,x1,y1,x2,y2):
#         self.sourc=point(x1,y1)
#         self.destination=point(x2,y2)

#     def show(self):
#         print("source = " ,self.sourc.get())
#         print('Distination = ', self.destination.get())
#     def reflaction(self):
#         self.destination.x= -self.destination.x
#         print("reflacton point on x acis is :",self.destination.x ,self.destination.y)

# l=location(1,2, 3,4)
# l.show()
# l.reflaction()





















# # write a program that has classes such as Student, courses, and department enroll a student is a courses of a particular department.


# from unicodedata import name


# class student:
#     def __init__(self,name,rollno,course, year):
#         self.name=name
#         self.rollno=rollno
#         self.course=Course(course,year)
#     def show(self):
#         print(self.name,self.rollno)
#         print(self.course.get())

# class Course:
#     def __init__(self,name,year):
#         self.name=name
#         self.year=year
#     def get(self):
#         return(self.name,self.year)
    
# class departement:
#     def __init__(self,name):
#         self.name=name
#         self.courses=[]
#     def get(self):
#         return(name,self.courses)
#     def add_courses(self,name):
#         self.courses.append(name)
#     def show_courses(self):
#         print("courses offred in this department are :",self.courses)

# d1=departement("computer science")
# d2=departement("math")
# d1.add_courses('bca')
# d1.add_courses("bsc")
# d2.add_courses("math")
# d2.add_courses("math2")
    

# print("*** their student, the list of courses offered in their respective department is given below.. kindly choose any one courses *******")

# d1.show_courses()
# # print(d1 .get())
# d2.show_courses()
# s=student("vaibhav",15,"computer science",2020)
# s.show()

















# # write a program that has an abstract class Polygon. Drive two classes Rectangle and Triangle from Polygon and write methods to get the details of their dimensions and hence calculate the area.

# class polygon:
#     def get_data(self):
#         raise NotImplementedError
#     def area(self):
#         raise NotImplementedError

# class Ractangle(polygon):
#     def get_data(self):
#         self.length=float(input("Enter the length of the  rectangle :"))
#         self.breadth = float(input("Enter the breadth of the reactangle "))
#     def area(self):
#         return float( (self.length*self.breadth))

# class triangle(polygon):
#     def get_data(se):  #you can take any keyword ad a parameter like (self,le,etc)
#         se.base=float(input("Enter the base of the Triangle :"))
#         se.height=float(input("Enter the height of the Triangle :"))
#     def area(self):
#         return .5*self.base*self.height


# r= Ractangle()
# r.get_data()
# print(r.area())

# t=triangle()
# t.get_data()
# print(t.area())










