
# # def update(a):
# #     print(a)
# #     print(id(a))
# #     a[3]=50 
# #     print(a)






# # lst=[5,4,54,32,5,8]
# # print(id(lst))
# # print(lst)
# # update(lst)
# # print(lst)






# ## keyword variabal lenght argument  **kwargs

# # def info(name,age):

# #     print(name)
# #     print(age)

# # info(name='vaibhav',age=21)






# ##fibonachi series 

# # def fibo(x):
# #     a=0
# #     b=1
# #     if x==1:
# #         print(x)
# #     else:
# #         print(a)
# #         print(b)
# #         for i in range(2,x):
# #             c=a+b
# #             a=b
# #             b=c
# #             print(c)

# # if __name__=='__main__':
# #     print("enter a number for fibo")
# #     fibo(15)





# ##object orianted progaming langauge
# #Class 

# # class student():
# #     def info(self):

# #         print("name vaibhav and age is 21")



# # s1=student()
# # student.info(s1)



# ##__init__ method

# # class student:

    
# #     def __init__(self,name,age,fev,other):
# #         self.a=name
# #         self.b=age
# #         self.c=fev
# #         self.d=other


# #     def execute(self):
# #         print("hi i am {0} i am {1} year old & my passion is  {2}  and {3}".format(self.a,self.b,self.c,self.d))

# #     def camepare(self,other):
# #         if self.a==other.a:
# #             print("they are same age")

# #         else:
# #             print("they are different age")
# # s1=student( )

# # s1=student('vaibhav',21,'coder','and something')
# # s2= student('mauli',19,'coding lover','sweet')
# # s1.a='mauli'
# # s1.execute()
# # s2.execute()

# # s1.camepare(s2)





# # class student:
# #     def __init__(self,name,std,Roll):
# #         self.name=name 
# #         self.std=std 
# #         self.roll=Roll
# #         self.lapinfo=self.laptop()


# #     def showinfo(self):
# #         print("name is ",self.name,"&std is ", self.std,"and roll number is ",self.roll,)
# #         self.lapinfo.lap()

    
# #     class laptop:
# #         def __init__(self):
# #             self.brand='acer'
# #             self.prosser='i3'
# #             self.Ram= '8gb'
# #         def lap(self):
# #             print(self.brand,self.Ram,self.prosser  )



# # S1=student('vaibhav','sybcs',18)
# # S2= student('kailas','sybcom',5)

# # S1.showinfo()

# # S2.showinfo()


# # a= int(input("enter the 1st number"))
# # b= int(input("enter the 2nd number"))

# # if a>b:
# #     print(a,"larger than ",b)
# # else:
# #     print(b,"larger than ",a)




# # tprime=0
# # tcomposite=0

# # num= int(input("enter the number:"))
# # # if (num==-1):

# # # composite=0
# # for i in range(2,num):
# #     if (num%i==0):
# #         tcomposite+=1
            
# #     else:
# #         tprime+=1
# # print("total primr",tprime)
# # print("total prime",tcomposite)







# from playsound import playsound
# from gtts import gTTS
# def playaudio(audio):
#     playsound(audio)
# def audio(text):
#     audio=gTTS(text)
#     audio.save("textaudio.mp3")
#     playsound("textaudio.mp3")
# audio("jab tak todenge nahi, tab tak .")







# # # warite a program to determine whether a person is eligibal to vote

# # age = int(input("enter your age:"))

# # if age>=18:
# #     print("you are eligibal to vote")
# # else:
# #     print("you are not eligibal to vote")





# # write a program to determine the charecter entered by user .

# # char= input("press any key :")
# # if (char.isalpha()):
# #     print("you interd charector ")
# # elif (char.isdigit()):
# #     print("you press digit ")
# # elif (char.isspace()):
# #     print("you press space")
# # if (char.isascii()):
# #     print("ascii")






# #write a program to determine whether  a person is eligibal to vote or not. if he is not eligibal, display how many years  are left to be eligibal 


# # age=int (input("enter your age :"))

# # if age>=18:
# #     print("congraculation, you are a eligibal to vote")
# # elif (age<=18):
# #     year=18-age
# #     print("you are not eligibal to vote please waite next {0} year for vote".format(year))






# # #write a program to find larger of two numbers.
# # a=int(input("enter a number:"))
# # b=int(input("enter a number"))
# # if a>b:
# #     c=a
# # else:
# #     c=b
# # print("large number is :",c)





# # #write a program to find a whether the given number is even or odd.

# # num=int(input("enter a number:"))
# # if num%2==0:
# #     print("the given number is even")
# # else:
# #     print("the given number is odd")




# #write a program to enter any charecter. if the enteres character is an lowercase then convert it into uppercase and if it is ippercase charecter,then convert into lowercase.
# # ch=input("enter any charecter")
# # if (ch>='A'and ch<='z'):
# #     ch=ch.lower()
# #     print("converting lovercase:",ch)
# # elif (ch>='a' and ch<='z'):
# #     ch=ch.upper()
# #     print("converting uppercase:",ch)



# # a company  decided to give bounus to all employees on Diwali. A 5% bonus on salery is given to the male workers and 10% bounus on salery to the female 
# # workers. Write a program to enter the salery of the employee and sex of the employee . if of the employee is less than Rs 10000 get an 2%  extra bonus 
# # on salery. Calculate the bonus that has  to be given to the employee and display the selery thet the employee will get.


# # sex= input("Press M for male and press F for female:")
# # salery=int(input("enter your selery amount"))

# # if sex=='m'and  salery<=10000:
# #     bo=0.07*salery
# # elif (sex=='m'):
# #     bo=0.05*salery
# # elif(sex=='f') :
# #     bo=0.10*salery

# # total=bo+salery
# # print("salery:",salery)
# # print("bonus",bo)
# # print("total paid",salery+bo)






# ## Programe to test a number enterd by the user is negative or positive 
# # num=int(input("enter the number : "))
# # if (num>0):
# #     print("this number is positive")
# # elif(num<0):
# #     print("this number is negetive")





# # write  a programe to determine whether the charecter enterd is a vowel or not 

# # ch = input("enter a chareacter ")
# # if (ch=='a'or ch=='e' or ch=='i'or ch =='o' or ch=='u' ):
# #     print("this is vowel")
# # else:
# #     print("this is not Vowel")


# # vai= "vaibhav"
# # vai2= "vaibhav nagargoje"
# # vai2+=vai 
# # print(vai2)



# # programe to demonstrate oprations on a tuple
# # tup1=('a','bc',78,1.23)
# # tup2=('d', 45)

# # print(tup1)
# # print(tup1[1])
# # print(tup1[1:3])
# # print(tup1[2:])
# # print(tup1+tup2)



# #programe to demonstrate opration on lists
# # list1=['a','bc',54,2.33]
# # list2=['e',90]
# # print(list1)  #printing list
# # print(list1[2])
# # print(list1[1:2])
# # print(list1*3)
# # print(list1+list2)



# #Programe to demonstrate the use of dictionary
# # Dict1={"name":"vaibhav","GF":"S_someone"}
# # print(Dict1)
# # print(Dict1["name"])
# # print(Dict1["GF"])



# # ##write a programe to enter  a number and display its hex and octal equivalant and its square root.
# # num= int(input("enter a number:"))
# # print("hexadecimal of "+ str(num)+"-"+str(hex(num)))
# # print("octal of "+str(num)+":"+str(oct(num)))
# # print("square root of is",num**0.5)





# ##write a programe to calculate area of a triangle using Heron's formula.
# # a=float(input("inter a"))
# # b=float(input("enter b"))
# # c=float(input("enter c"))
# # print(a,b,c)
# # s=(a+b+c)/2
# # ans=(s*(s-a)*(s-b)*(s-c))**0.5
# # print("area of triangle is :",ans)



# # #let learn about list comprehensions! you are given three integer x,y,z
# # #representing the dimension of a cuboid along with an integer n.
# # #Print a list of all possibal coordinates given by (i,j,k) on a 3d gird where the sum  of o+j+k is not equal to n.
# # #here, 0<+i<=x;0<=j<=y;0<=k<=z. Please use list comprehensions rather than multipal loots
# # #as learning exercise.

# # x= int(input("enter"))
# # y= int(input("enter"))
# # z= int(input("enter"))
# # n= int(input("enter"))
# # ans=[[i,j,k]
# # for i in range(x+1)
# #     for j in range(y+1)
# #         for k in range(z+1)
# #             if i+j+k!=n]
# # print(ans)







# # #given the names and grades for each student for each student  in class od N students, store tham 
# # # in a nested list and print and print the name(s) of any student(s) having the second lowest grade

# # result=[]
# # scorelist=[]
# # std=int(input("enter a total student "))

# # for i in range(std):
# #     name=input("enter a name:")
# #     mark=float(input("enter a mark score: "))
# #     result+=[[name,mark]]
# #     scorelist+=[mark]
# # b=sorted(list(set(scorelist)))[1]
# # for a,c in scorelist(result):
# #     if c==b:
# #         print(a)






# # #python pattern
# # name=input("enter a name ")
# # a=0
# # for i in name:
# #     a=a+1
# #     print(name[0:a])
# # for i in name:
# #     a=a-1
# #     print(name[0:a])
    






# # for i in range(5):
# #     for j in range(5):
# #         if i+j==2 or i-j==2 or i+j==6 or j-i==2:
# #             print("*",end="")
# #         else:
# #             print(end="")
# #             print()






# # def pattern(n):
# #     k=2*n-2
# #     for i in range(0,n):
# #         for j in range(0,k):
# #             print(end=" ")
# #         k=k-1
# #         for i in range(0,i+1):
# #             print('10',end="")
# #         print("\n")
# # pattern(5)










# import pyfiglet
# a= pyfiglet.figlet_format("happay birthday    ")
# print(a)

# x=0
# while x<20:
#     x=x+3
#     print(x)
# print(x)





# # Consider a list (list=[]). you can perform the following commands:
# # insert i e: Insert integer  at position .
# # print: Print the list.
# # remove e: Delete the first occurrence of integer .
# # append e: Insert integer  at the end of the list.
# # sort: Sort the list.
# # pop: Pop the last element from the list.
# # reverse: Reverse the list.




# # N=(int(input("enter:")))
# # list=[];
# # for i in range(0,N):
# #     l=input().split()
# #     if l[0]=="insert":
# #         list.insert(int(l[1]),int(l[2]))
# #     elif l[0]=="append":
# #         list.append(int(l[1]))
# #     elif l[0]=="pop":
# #         list.pop()
# #     elif l[0]=="print":
# #         print(list)
# #     elif l[0]=="remove":
# #         list.remove(int(l[1]))
# #     elif l[0]=="sort":
# #         list.sort()
# #     else:
# #         list.reverse()



# # from numpy import*
# # arr= array([])








# ### wrrite a programe to find a wheater a given year is leap or not

# year = int(input("enter a year:"))

# if (year%4==0 and year%100 != 0 or year %400 == 0 ):
#     print("this is a leap year")
# else :
#     print("this is not a leap year")






# #write a programe to test a whether a number enterd by the user in negative, positive,or equal to zero

# num = int(input("inter a number :"))

# if(num==0):
#     print("the value is zero")
# elif(num>0):
#     print("the value is positive")
# else:
#     print("the value is negative")










# # write a programe to calculate the tax

# min1 = 150001
# max1 = 300000

# rate1 = 0.10

# min2 = 300001
# max2= 500000
# rate2 = 0.20

# min3 = 500001
# rate3 = 0.30 

# income= int(input("enter yout incomr"))

# taxebal_inc= income - 150000
# tax=0
# if(taxebal_inc<= 0):
#     print("no tax")
# elif(taxebal_inc> min1 and taxebal_inc < max1):
#     tax= (taxebal_inc - min1)* rate1
# elif(taxebal_inc>min2 and taxebal_inc<max2):
#     tax = (taxebal_inc- min2)*rate2
# else:
#     tax= (taxebal_inc-min3)*rate3

# print("total tax is :",tax)





# # add a two integer using functins
# def total( x,y):
#     sum= x+y
#     print("sum of",a, "+",b,"=",sum)

# a = (int(input('enter a first number :')))
# b= int(input("inter second number :"))

# total(a,b)








# num1= 10
# print("Global veriable num1 = ",num1)
# def func(num2):
#     print("num2 is a local veriable = ",num2)
#     num3 = 30 # num 3 is a local veriable 
#     print ("in function  - local veriable num3 =", num3)
#     global num1
#     num1 = 200


# func(20)

# print("num1",num1)
# print(num3)











# #programe to demonstrate the use of global statement
# var= "good"

# def show ():
#     global var1
    
#     var1 = "morning"
#     print("in fuction var is ",var)

# show()
# print("outside fuction , var1 is ", var1)

# print("var is ", var)






# # programe to demostrate name clash of local and global variable
# var ="Good"
# def show():
#     var = "morning "
#     print("inFunction var is -", var)

# show()
# print("Outside fuction var is - var is ", var)






# # Programe to demonstrate modifing a Global variable

# var = "good"

# def func ():

#     # print("var is ", var)
#     global var
#     var = "ggg"
#     print(var)

# func()
# print("var",var)

    






# # Programe to demonstrate access of variable of varius in inner and outer function
# def outer_func():
#     pass
#     outer_variable= 10
#     def inner_variable():
#         # global inner_var # try to avoid  the use of global variable and glogal statement
#         inner_var= 20
#         print("outer_variableis",outer_variable)
#         print("inner_variableis",inner_var)
#     inner_variable()
#     print("outer_variableis",outer_variable)
#     print("inner_variableis",inner_var)




# outer_func()









# # programe to demonstrate name clash variable in case of nested fuctions
# def outer_func():
#     var= 10
#     def inner_func():
#         var = 20
#         print("inner variable is ",var)
#     inner_func()
#     print("Outer variable is =", var)

# outer_func()







# # programe to write a function without a return astatement and try to ptint its  return value As mentioned earlier, such a function should reuturn none

# def display (str1): #taking paraperter as a string  
#     a=print(str1)
#     return a
# a= display("hello world")
# # print (a)









# # programe to write another function which return an integer to the caller

# def cube (x):
#     return(x*x*x)
# num= 10
# result= cube(num)
# print(f"cube of {num} is {result} ")







# progrme to demonstrate flow of control after  dthe return statement

# def display():
    
#     print("in fuction")
#     return
#     print("after retun")
# display()









##### Keywoed Arguement 

#programe to demonstrate keywoed arguments

# def display(str,int_c,float_y):
#     print(str)
#     print(float_y)
#     print(int_c)
    # display(float_y= 344.3,str= "vaibhav",int_c= 12)







# consider anothe programe for keywoed arhuments in which during functuin call we use assignment operator to assign values to functoin parameters using other variables 














# #from typing import AsyncGenerator
#    # this code wirtten by kailas khade the blogger chutita 

# def display('name' 'age' 'salary')
# n = kailas 
# a= 20
# s= 3000
# display( name=n age=a salary=s)
# print(name)








# programe to add a two number  using the syntax of lamda function 

# sum = lambda a , b , c: a + b + c 
# print("=", sum( 3,4,5))









# progrme to find samaller of two numbers using lambda functoin

# def small( a,b):
#     if (a<b):
#         return a
#     else:
#         return b
# sum = lambda a,b : a+b 
# diff= lambda a,b : a-b

# # passing the value 
# a= small(sum( 30,5),diff(  45, 22))
# print(a)









# # programe to  use a lambda function with an ordinary function

# def incerment(y):
#     return (lambda x:x+1)(y)
    
# a = 100
# print ( "a", a )
# print("after increment a +")
# b = incerment(a)
# print(b)








# progrme to passes lambda function as an argument to a function

# def func( a,b):
#     print(a(b))
# squre = lambda x : x*x

# cube = lambda x: x* x*x
# func (squre, 4)
# func( cube, 3)







# programe that uses a lambda fucntion to find the sum of first 10 natural numbers

# x = lambda  :sum(range( 1, 11))

# print(x())














# #  ************** Documentation strings ***************


# # programe to show a multi - line docstring

# def func ():
#     """this fucntion is not important and only print Hello Vaibhav   """
#     print("hello vaibhav")

# a=(func.__doc__)
# print (a)






#  EXAMPAL 
# #  write a programe to swap two numbers


# a= input("enter a value of  A : ")
# b= input("enter a value of  B : ")
# def swap(a,b):
#     temp = a
#     a= b
#     b= temp
#     return a, b

# print(f"before swap a value A =  {a} and B = {b} ")

# a,b=swap( a,b)
# print(f"after swap  A= {a}, and B= {b}")








# # #  write a programe to return the full name of a person.

# a = input("enter your frist name :")
# b = input("enter your last  name :")

# def name (a,b):
#     space =" "
#     n=    a+space+ b

#     return n
# x= name(a,b)
# print(x)








# # wrrite a programe to retuen the average of its arguments.

# def average(a,b):
#     return int((a+b)/2)  #typecasting in int
# n1= int(input("inter a 1st number:"))
# n2= int(input("inter a 2nd number:"))
# print("average is:",average(n1,n2))







# # write a program to convert time into minutes

# def convert_time(h,m):
#     min = h*60+m
#     return min
# hour = int(input("Enter a hour:"))
# min = int(input("Enter a min:"))
# a=convert_time(hour,min)
# print(a)





# # write a programe to calculate simpal interest.
# def intrest( p,y,s):
#     if s=='y':
#         si= float(p*y*12)
#     else:
#         si= float(p*y*10)
#     return si

# p= float(input("Enter the principal amount:"))
# y= float(input("Enter the number of years:"))

# senior= input("is customer senior citizer (Y/N):")
# intress = intrest(p,y,senior)

# print(intress)











# # write a program to calculate the valume of a cuboid using default argumentds.

# def valume( l=8,w=9,h=10):
#     print(f"length is {l} ,\twidth is {w} \t height{h}")


# print("value is :",valume(4,5,6))
# print("value is :",valume(4,6,))
# print("value is :",valume(3))
# print("value is :",valume())










# # write a programe that computes p(n,r)
# def func(num):
#     f=1
#     if (num==0 or num==1):
#         return 1
#     else:
#         for i in range(1,int(num+1)):
#             f=f*i
#         return f

# n= int(input("enter a value of n:"))
# r= int(input("enter a value of r:"))
# result = func(n)/func(r)
# print(result)







# # write a sum of the series  1/1! + 4/2! + 27/3+ .....
# def fact(num):
#     f=1
#     if num==0 or n==1:
#         return 1
#     else:
#         for i in range(1,num+1):
#             f=f*i
#         return f







# n= int(input("enter the value of n :"))

# s= 0.0 
# for i in range (1,n+1):
#     s=s+((i**i)/fact(i))
# print("result =",s)








# # # write a program that uses docstings and variable length arguments to add the values passed to the function
# def addfunc(*args):
#     """function returns the sum of  values  passed to it """

#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
# print(addfunc.__doc__)
# add= addfunc(10,20,30,40,50)
# print("sum of total:",add)







# # write a programe that greets a person.
# def greet(name,message):
#     """this is a function 
#     hello the person passed whose name is passed as a parameter"""
#     # print(greet.__doc__) this is for only for try the function is calling itself 
#     print(f"hello {name}, {message} ")


# message = "happay birthday "
# name=input("enter yoour name :")

# print(greet.__doc__)

# greet(name, message)









# # write a programe to print the following Pattern using default arguments.
# def pattern(c='*',n= 4,m=4):
#     for i in range(1,m):       #range will go upto column
#         print()                #for new line 
#         for j in range(n):      #range will go up to rows
#             print(c,end=" ")


# c=input("Enter the character to be displayed: ")

# n= int(input("enter the number of rows:"))
# m= int (input("enter the number of columns: "))

# # pattern(c)
# pattern(c,n,m)

# ***********************************************************     today_date_is 28/12/2021        **********************************************************




# # recursive functions

# # programe to calculate the factorial of a number recursively

# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     else:
#         a= n*factorial(n-1)
#         return a
# num= int(input("Enter a number :"))

# print("factorial is:",factorial(num))





# #### GCD  Greatest common divisor ***********************

# # write a programe to calculate GCD using recursive fuction 
# def gcd( a, b):
#     reminder= a%b
#     if reminder==0:
#         return b
#     else:
#         return gcd(b,reminder)


# a= int(input("enter a number: "))
# b= int(input("enter a number:"))
# c= gcd(a,b)
# print(f"gcd of {a}, {b} is {c}")





# ##   finding exponents 

# #write a programe to calculate exp(x,y) using recursive recursive functions.
# def exp(n,m):
#     if m==0:
#         return 1
#     else:
#         return (n*(exp(n,m-1)))


# n= int (input("Enter number:"))
# m= int (input("Enter number:"))

# print("exponents is ",exp(n,m))





# ## write a program to print the fibonacci series using recursion
# def fibo(a):
#     if a<2:
#         return 1
#     else:
#         return fibo(a-1)+fibo(a-2)
    

# n= int (input("number:"))
# for i in range(n):

#     print(f"fibo {i} is :",fibo(i))








# #********************************** iteration **********************************



# def func (n,count= 0):
#     if n==0:
#         return count
#     else:
#         return func(n-1, count+1)
# print("total times recursive fuction=",func(555))




# #************************** module***********************************

# #write a programe to print the  sys.path

# import sys
# print ("\n python path = \n", sys.path)







# # program to show the use of  from import statement

# from math import pi 

# print(pi)








# #programe to  print the name of the module in which yoyr statemants is weitten

# print("hello vaibhav")

# print("name of this module is : ",__name__)








# import mymodule
# print("MyModule str=",mymodule.str)
# mymodule.display()
# print("name of calling module is :",__name__)








# programe that defines a function large in a module which will be used to find larger of two values and called from  code  in another module 

"""importing logic from mumodule in this folder"""
# import mymodule
# print("large(50,100",mymodule.large(50,100))

# a= mymodule.large('b','z')
# print(a)




# # programe to demonatrate the use of dir() function

# def print_var(x):
#     print(x)

# x=10
# print_var (x)
# print(dir())





# # programe to print identifiers in the dir() function
# import builtins
# print(dir(__builtins__))







# # write a programe that print absulate value , squre root, and cube of a number

# import math

# def cube(a):
#     return a**3

# a=int(input("inter a number:"))


# # print("abs(a)",abs())

# print(f"squre root of {a}", math.sqrt(a))
# print(f"qube is {a}", cube(a))



        








# # write a programe to genrate 10 random nummbers between 1 to 100:

# import random
# for i in range(10):
#     Value= random.randint(1,1000)

#     print(Value)













# *******fuction as Object *******************************************************

# # program to demonstrate that function is object 

# def fuct1():
#     """this function DONE  by vaibhav WITH  doing python prctice"""

# a=  isinstance(fuct1, object)

# print("func1  is an instance of Object :",a )
# id = id(fuct1)
# print(id)

# print("docstring ", fuct1.__doc__)
# print("fuction name", fuct1.__name__)










# # Program to demonstrate thet fuctions can be used as an argument to a fucntion and canbe stored in a collections

# def func1():
#     pass

# def func2():
#     pass
# def func3():
#     pass 
# def func4(func):
#     print("id(func)=",id(func))


# functions= (func1,func2,func3,func4)
# for i in functions:
#     print(i)
#     func4(i)













# *********************************************python string**********************************************************************

# programe to demonstrate string traversal using indexing

# name = "vaibhav"

# index= 0

# for a in name:
#     print("name[",index,"] = ", a)
#     index+=1




# str1 = "my name is "
# str2 = input("inter your name ")

# print((str1+str2)*3)





# program to  print a raw string

# print("hello")
# print("\nhello")
# print(r"\nvaibahv")




# programe to demonstrate string regerance using the id () fuction

# ####( string are immutable means onece created thy cannot be changed)

# str1 = "hello"
# print("str1 is :",str1)
# print ("id of str1 is ", id(str1))
# str1 = "hello"
# print("str1 is :",str1)
# print ("id of str1 is ", id(str1))
# str1 = "hello"
# print("str1 is :",str1)
# print ("id of str1 is ", id(str1))

# str2 = "vaibhav"
# print("str2 is :",str2)
# print ("id of str2 is ", id(str2))
# str1+=str2

# print("str1 after concatination is  :",str1)
# print ("id of str1 is ", id(str1))






# # string is immutable you cannot be change specific index
# str= "vaibhav"
# print(str[3])
# str[3]= "h"









# #  program to use format sequance while printing a string
# name= " vaibhav"
# age = 57

# print( " name is %s and  age is %d"%(name, age))






# # program to display powers of a number without using formatting characters
# i=1
# print("i\ti**2\ti**3\ti**4\ti**5\ti**6\ti**7\ti**8\ti**9\ti**10")

# while i<=10:
#     print(i,  '\t',i**2,  '\t',i**3,  '\t',i**4,  '\t',i**5,  '\t',i**6,  '\t',i**7,  '\t',i**8,  '\t',i**9,  '\t',i**10)
#     i+=1






#******************************************************  BUILT-IN STRING METHODS AND FUNCTIONS*********************************************************************************************


# str = "hello Vaibhav Nagargoje"
# print(str.capitalize())  # only frist letter  this fuction is used to capitalize frist letter of the string

# str = "hello"
# print(str.center(9, '*'))

# str= "she is my girlfrind and she is very cute"
# print(str.find("very"))            # finding the position of given argument 




# str= "Hello"
# print(str.lower())


# str1= "name is my vaibhav"
# print(str1.replace("vaibhav","don"))



# str1 = " Vaibhav_nagargoje"
# print(str1.upper())



# str1= "Vaibav is very tired "
# a = str1.title()
# print(a)



# str= "the  VAibhav NAGARGOje "
# print(str.swapcase())
# str="hello, my, name,is vaibhv"
# a= str.split(",")
# print(a)








# # print('-'.join( [ "vaibhav","is ","bad" ,"boy"]))

# str1= "what is a coinsident"
# print(list(enumerate(str1)))









# programe to  demonstrate splice operation with just last (negative) argument


# str1=" welcome to the world of python"
# print(str1[::-1])




# char= 'A'
# print(ord(char))

# print(chr(118))






# str1= "welcome to the my life "

# str2 ="my"

# if str2 in str1 :
#     print("found")
# else:
#     print("not found")









# # program to iterate a given string using for loop
# str1= "this is vaibhav pro "
# for i in str1:
#     print(i,end=' ')

# index=0 
# while index<len(str1):
#     leter=str1[index]
#     print(leter,end=" ")
#     index+=1







# # write a program to pront the following pattern.
# # A
# # AB
# # ABC 
# # ABCD 
# # ABCDE 
# # ABCDEF 

# for i in range(1,10):
#     ch='A'
#     print()
#     for j in range (1,i+1):
#         print (ch,end=" ")
#         ch= chr(ord(ch)+1)












# # write a program that takes user's name and PAN card number as input validate the information using isX fuction and print the details.

# while(True):
#     name = input(" Enter your name:")

#     if name.isalpha()==False:
#         print("Invalid Name, Sorry you cannot proceed.")
#         break
#     else:
#         pan_card_no = input("Enter your PAN card number:")

#         if pan_card_no.isalnum()== False:
#             print("Invalid PAN card number, sorry you cannot proceed,")
#             break
#     print("Please check, "+name+", your pan card number is : "+ pan_card_no)
#     break











# # write a program that encrypts a massage by adding a key value to every character. (Caesar Cipher)

# massage=input("enter your massage:")
# index=0
# while index<len(massage):
#     letter= massage[index]
#     print(chr(ord(letter)+7),end="")
#     index+=1
# print("\n")






# # decrypter 
# massage=input("Enter your massage for decrypt")
# index=0
# while index<len(massage):
#     letter= massage[index]
#     print(chr(ord(letter)-7),end="")
#     index+=1







# # write a programe that uses split () to split a multipal string.

# letter = """ Dear students, 
# i am pleased to inforn you that, 
# there is a workshop on python in college tomorrow.
# Wveryone shoukd come and there will also be  a quiz in python whosoever wins
# will win a Gold Medel."""

# print(letter.split("\n"))










# # write a programe  to generate an abecendarian series.

# str1= 'ABCDEFGHI'
# STR2= "ate"

# for letter in str1:
#     print(letter+STR2,end="  ")







# # write a program that accepts a string fron user and redisplays the same string after removing vowels from it.
# def R_vewels(string):
#     string1=""
#     for i in string:
#         if i in "AEIOUaeiou":
#             pass
#         else:
#             string1+=i
#     return string1

# str1 = input("Enter a string:")
# a=R_vewels(str1)
# print("new string after removing Vowels: ",a)









# # Write a program that find whether a given character is present in a string or not. In case it is present is prints the index at which it is present. So not use built_in find
# # function to search the character.

# def ch_search(s,c):
#     index=0
#     for i in s:

#         if i==c:
#             print(f"{c} charactrer found in {index} index no")
#             return
#         else:
#             pass
#         index+=1
#     print("this character is not found in given string")
    

# str1= input("Enter a string:")
# ch= input("enter a character for search:")
# ch_search(str1,ch)











# # write a program that emulates the rfind function.
# def refind(str,ch):
#     index= len(str)-1
#     while index >=0:
#         if str[index]==ch:
#             return index
#         index-=1
#     return -1





# str1= input("Enter a string:")
# ch=input("Enter a character:")
# a=refind(str1,ch)
# if a!= -1:
#     print(ch,"found at location ",a)
# else:
#     print(ch,"is not present in the string")












# # Write a program that counts the occurrences of a character in a string .Do not use built in function 
# def count_ch(str,ch):
#     count=0
#     for i in str:
#         if i ==ch:
#             count+=1
#         else:
#             pass
#     return count


# str=input( "enter a string")
# ch= input("enter a character")
# count=count_ch(str, ch)
# print(ch ," is total ",count,"times in string")






















# # Write a program to reverse a string*******************************************************

# def reversed_string(string):
#     new_str=""
#     print(len(string))
#     i = len(string)-1
#     while i>=0:
#         new_str+=string[i]
#         i-=1
#     return new_str
    
# str= input("Enter a string ")
# print(reversed_string(str))
# # print(str[::-1])








# # Write a programe to parse an emal id to print from which email server it was sent and when.
# info ='from vaibhavnagargoje381@gmail.com sun oct 16 20:29:40 2021'
# st









# *****************************************************************The strubg module**********************************************************************************

# # program to print the dectsring of an item in string module
# import string

# print(string.__builtins__.__doc__)




# # program using help()
# str= 'Hello'
# print(help(str.isalpha))











# # program to demonstrae the use of match() function
# import re
# string ="She sells sea shelles on the sea shore"
# pattern1= "sea"
# if re.match(pattern1,string):
#     print("Match found")
# else :
#     print(pattern1,"is not present in the string")
# pattern2= "shore"
# if (re.match(pattern2,string)):
#     print("match found")
# else:
#     print(pattern2,"is not present in string ")









# # programe to demonstrate the use of search() function
# import re
# string= ' she sells sea shells on the sea shore'
# pattern1= 'sells'
# pattern2= 'shore'
# if re.search(pattern1,string):
#     print("match found")
# else:
#     print(pattern1," is not not present in string")









# ** the sub() function
# # program to demonstrate the use of sub () function

# import re
# string="she sells sea shells on the sea shore"
# pattern1="sea"
# replace='ocean'
# new_str=re.sub(pattern1,replace,string)
# print(new_str)











# # Program to demonstrate the use of findall() function 


# import re
# pattern=r"[a-zA-z]+ \d+"
# match= re.findall(pattern,"LXI 2013 ,vxi 2015, vdi 20104, maruti suzuki cars i india")
# for i in match:
#     print (i ,end=" ")



# # hackerrank practice****************************
# def cou_sub(s1,s2):
#     count= 0
#     for i in range(len(s1)-len(s2)+1):
#         if (s1[i:i+len(s2)]==s2):
#             count+=1
#     return count
# str1= input("enter a string:")
# sub_str=input("enter a string:")


# count=cou_sub(str1,sub_str)
# print(count)








# ********************************************************** File Handling ******************************************************************************************************************************************************************************************************************

# # Program to open a file and print its attribute value.

# file= open("file.txt","wb")
# print("name of the file:",file.name)
# print("file is closed.", file.close)
# print("file has been upened in",file.mode,"mode")







# # Profram to access a file after it is closed.

# file= open("file1.txt","wb")
# print("name of the file:",file.name)
# print("file is closed.",file.closed)
# print("file is now being closed.. You canot use the File Objext")
# file.close()
# print("file is closed.",file.closed)
# print(file.read())







# # Program  that weites a mwssage in the file,file1.txt 

# file=open("file1.txt","w")
# file.write("hello all, hope you are enjoying learning Python")

# file.close()
# print("data written into the file. . .......")


















# # Program to write to a file using the writelines() method

# file = open("file1.txt","w")
# lines= ["hello workd", "welcome to the world of python", "enjoy Learning Python"]

# file.writelines(lines)
# file.close()
# print("file written to file........")




# # Program  to append data to an already existing file

# file= open("file1.txt",'a')
# file.write("\nPython is avery simple yet powerful language")
# file.close()
# print("Data appended to file............")











#  the tead() and readline () Methods///////////////////////////////////////////////////////////////


# #  program to print the first 10 characters of the file file1.txt
# file= open("file1.txt","r")
# print(file.read(15))
# file.close()











# # NOTE Note that if you tru to open a file for reading that does not wxost,then you will get an wrror, as shown below.

# file= open("file2.txt","r")
# print(file2.read())









# cinsider adding a few more lines in the file file1.txt and read its contensts using the readline() method . The following are the contents of the
# file which will be also used inExamples 

# file1.txt 
    # hello all , 
    #  hope you are enjoying learning Python
    #  We have ried to cover every point in detail to avoid confusion
    #  Happy Reading

# file= open("file1.txt","r")
# print("first line:",file.readline())    
# print("second line:",file.readline())
# print("third line:",file.readline())

# file.close()












# # Program to demonstrate readlines() fuction 
# file= open("file1.txt","r")
# print(file.readlines())
# file.close()







# # Program to display the contenst of the file file1.txt using the list() method.
# file=open("file1.txt","r")
# print(list(file))
# file.close()









# # Program to display the contents of a file
# file= open("file1.txt","r")
# for line in file:
#     print(line)
# file.close()








# # opening file using with keyword/////////////////////////////

# with open ("file1.txt","rb") as file:
#     for line in file:
#         print(line)
    
# print("Let's check if the file is closed:",file.close())



# # file = open("file1.txt","rb")
# # for i in file:
# #     print (i)
# # print("Let's check if the file is closed:",file.close())








# #  SPLITTING WOEDS ///////////////////////////////////////////////////////

# # Program to split the line into a series of woeds and use space to perform the split operation
# with open("file1.txt","r") as file:
#     line= file.readline()
#     word=line.split()
#     print(word)







# # Program to perform split operationwhenever a coma is encounterd

# with open("file1.txt","r") as file:
#     line= file.readline()
#     words= line.split(',')
#     print(words)









# # return the file number of the file  
# file= open("file.txt","w")
# print(file.fileno())










# # program that tells and sets the position of the pointer

# file= open("file1.txt","rb")
# print("Position of file pointer before reading is :",file.tell())
# print(file.read(10))
# print("Position of file pointer after reading is :",file.tell())
# print("ssetting 3 byte from the current position of file pointer")
# file.seek(1,2)
# print(file.read())
# file.close()







# # Write a program that copies first 10 byte of a binary file into another.
# with open ("file1.txt","rb") as file1:
#     with open("file2","wb") as file2:
#         buf= file1.read(10)
#         file2.write(buf)
# print("file copied")








# # Write a program that copies one Pthon script into another in such a way the all comment lines are skipped and not copied in the destination file.
# with open ("01.py","rb")as file1:
#     with open("02.py","wb") as file2:
#         while True:
#             buf= file1.readline()
#             if len(buf)!=0:
#                 if buf[0] =='#':
#                     continue
#                 else:
#                     file2.write(buf)
#             else:
#                 break
# print("file copied!!")










# # write a program that accepts filename as an input from the user.Open the file and count the unmber of time a character appears in the file

# filename= input("Enter the filename")
# with open (filename) as file:
#     text= file.read()
#     letter= input ("Enter the character to be searched:")
#     count=0
#     for character in text:
#         if character==letter:
#             count+=1
# print(letter,"appers",count,"times in file")












# # Write  a program the reads data from a file and calculus the percentage of vowels and consonats in the file

# filename=input("Enter the file name")
# with open (filename)as file:
#     text = file.read()
#     count_vovel = 0
#     count_consonants=0
#     for  ch in text:
#         if ch in "aeiou":
#             count_vovel+=1
#         else:
#             count_consonants+=1
# print("number of vewels =",count_vovel)
# print("number of consonants = ",count_consonants)
# print("total length of file= ",len(text))
# print("percentage of vowels in the file = ",(count_vovel*100)/len(text),"%")
# print("percentage of consonants in the file = ",(count_consonants*100)/len(text),"%")
















# #   RENAMING AND DELETING FILES 

# # Program to rename file"file1.txt" the "student.txt"
# import os
# os.rename("file1.txt","New_file.txt")
# print("file Renamed")

#  the remove method 

# # Program to delet a file named "New_file.txt"
# import os 
# os.remove("New_file.txt")
# print("file deleted")








# DIRECTORY METHOD//////////////////////////////

#the mkdir () Method : 


# #  Program to create a new directory New Dir in the current directory.continue
# import os 
# os.mkdir("New directory")
# print("directory created")






# Program that  change the current directory to our newly created direactory  - New Dir .

# import os 
# print("Current working directory is: ", os.getcwd())
# os.chdir("New Dir")
# print("After chdir, the current Dirchtory is now.............",end=' ')
# print(os.getcwd())













# # Program to demonstrate the use of rmdir() functon 

# import os 
# os.rmdir("New directory")
# print("directory deleted")











# # Program that uses os.path.jion() method to form a valid file path 

# import os 
# print( os.path.jion("C:","student", " vaibhav.txt"))




# # write a program that counts the number of tabs, spaces, and new line characters in a file.

# filename= input("Enter the file name:")
# with open (filename) as file:
#     text = file.read()
#     count_tab= 0
#     count_space=0
#     count_newline=0
#     for character in text:
#         if character=='\t':
#             coutnt_tab+=1
#         if character == ' ':
#             count_space+=1
#         if character =='\n':
#             count_newline+=1
# print("Total tab",count_tab)
# print("Total space  ",count_space)
# print("Total new line character :",count_newline)








# # Write  a program that computes the total size of all the files in F:\python folder 
# import os 
# Total_size = 0
# for file in os.listdir("F:\python",):
#     Total_size+=os.path.getsize(os.path.join("F:\python",file))
# print("total soze of all the files in F:\python=",Total_size)








# # Write a program to  check if flash drive is connexted to your compter .
# import os
# connect= os.path.exists("g:\\")
# print("G drive is connected on your pc:",connect)












# # Write a program that reads a file line by line. Each line read from the file is copied to another file woth line numbers specified at the beginning of the line

# file1=open("file.txt","r")
# file2=open("file1.txt","w")
# num=1
# for line in file1:
#     file2.write(str(num)+":"+line)
#     num=num+1
# file1.close()
# file2.close()










# # Write a program that fatches data from a specified url and prints it on screen.
# import urllib.request
# a= urllib.request.urlopen('https://www.google.com/')
# print(a.read())











# # write a program that fatches data from a specified url and writes it in file.

# # Hint- Use the urllib2 module that handles the url

# import urllib3.request

# url='https://www.google.com.search?q=python'
# headers={}
# headers['User-Agent'] = "Mozilla/5.0 (X11; Linix i686) AppleWorkit/537.17 (KHTML,like Gecko) Chrome/24.0.1312.27 Sfari/537.17"
# Request=urllib3.request.Request(url,headers = headers)
# Response=urllib3.request.urlopen(Request)
# Data= response.read()
# file=open("URL_file.txt",'w')
# file.write(str(data))
# file.close()
# print("sucessful")









# #  Mail merge Program *************************************************************************************************************************************************************

# with open("names.txt","r") as names:
#     with open("Mail_body.txt","r") as body:
#         text= body.read()
#         for name in names:
#             mes="Hello"+name+text
#             with open(name.strip()+".txt","w",)as file:
#                 file.write(mes)











# # Finding Resolutionn of and Image************************************************************************************************************************************************************8

# # "Jpeg (Joint Photographic Experts Graph ) is one of the most widdely used comoression techniques for image compression. Most of the Image file
# # formats have headers stored in the inital few bytes few bytes to retain some usefil information about the file.
# #    in the following program, we will find out the resolution of JPEG image by reading the information stored in the header."


# # Program to find the resolution of an image

# def find_reso(filename):
#     with open(filename,"rb") as Img_file:  #Open Image in binary mode
#         Img_file.seek(163)
#         a=Img_file.read(2)
#         height= (a[0]<<8)+a[1]
#         a= Img_file.read(2)
#         width= (a[0]<< 8)+a[1]
#         print("Image Resolution is :",width,"X",height)

# find_reso("G:\DSC_0030-Copy.JPG")





















# ************************************************************DATA STRUCTURES*****************************************************************************************************************



# NOTE List is versatile data type available in Python.

# The syntax of defining a  list can be given as list_variable = [ val1, val2,val3,val4,......,valn]


# some type of list

# 1)
# list_a= [ 1,2,3,4,5]
# print(list_a)



# # 2)
# list_b = [ 'A','B','C','D']
# print(list_b)


# 3)
# list_c = ['Good Morning', 'Hello'," vaibhav"]
# print(list_c)



# 3)
# list_d= [1,'A', "vaibhav","""sorry"""]
# print(list_d)

# NOTE -> LIST IS MUTABLE WHICH MEANS THAT VALUE OF ITS ELEMENTS CAN BE CHANGED.





# ///////////////  Access Vales in Lists/////////////////
# Similar to strings, lists can also be sliced and concatenated.

# seq = List[start:stop: step]








# #  Program to demonstrate the slice operations used to access the elements of the list 

# num_list = [ 1,2,3,4,5,6,7,8,9,10]
# print("num list is  :", num_list)
# print("First element in the list is ", num_list[0])
# print("num_list[2:5]:",num_list[2:5])
# print("num_list [::2",num_list[::2])
# print("num_list [1::3]",num_list[1::3])







# #  Updating value in Lists///////////////////////////

# # Program to illustrate updating values in a list
# num_list = [ 1,2,3,4,5,6,7,8,9,10]
# print("list is :",num_list)
# num_list[5]= 100
# print("after updating list:",num_list)
# num_list.append(200)
# print("lis after appending a value:",num_list)
# del num_list[3]
# print("list after deleting a value :", num_list)









# # Program toillustrate delation of numbers from a list using del statements
# num_list =[1,2,3,4,5,6,7,8,9,10] # a list is defined
# del num_list[2:4]
# print(num_list)
# del num_list[:]
# print(num_list)









# # Program to illustrate deletion of a list
# num_list = [1,2,3,4,5,6,7,8,9,10]
# del num_list
# print(num_list)






# # Program to insert a list in another list using the slice operation 
# num_list =[1,9,13,15,20]
# print("original list",num_list)
# num_list[2]= [4,45,23]
# num_list[4]= [33,44]
# print("after inserting another list ,the update list is :", num_list)









# Nested list/////////////////////

# # Program to illustrate nested list

# list1= [ 1,'a',"abc",[2,3,4,],8.9]
# i=0
# while i< len(list1):
#     print("list1[",i,"] = ",list1[i])
#     i+=1



# # Cloning lists ////////////////////

# Program to create a copy as well as the clone of the original list

# list1= [1,2,3,4,5,6,7,8,9,10]
# list2= list1
# print("list1=",list1)
# print("list2=",list2)
# list3 = [list1[2:7]]
# print("list3= ", list3)






# list method //////////////////////////////////////////////////

# # append  
# num_list = [6,3,7,0,1,2,4,9]
# num_list.append(10)
# print(num_list)




# count()
# num_list = [6,3,7,0,1,2,4,9,2]
# a=num_list.count(2)
# print(a)


# index()
# num_list = [6,3,7,0,1,2,4,9]
# print(num_list.index(1))



# # insert()
# num_list = [6,3,7,0,1,2,4,9]
# num_list.insert(3,100)
# print(num_list)



# # pop()
# num_list = [6,3,7,0,1,2,4,9]
# num_list.pop()
# num_list.pop(0)
# print(num_list)



# # remove()
# num_list = [6,3,7,0,1,2,4,9]
# print(num_list)
# num_list.remove(6)
# print(num_list)









# # reverse()
# num_list = [6,3,7,0,1,2,4,9]
# a=(num_list.reverse)
# print (a)





# sort()
# num_list = [6,3,7,0,1,2,4,9]
# num_list.sort()
# print(num_list)





# # extend()
# num_list1=[1,2,3,4,5]
# num_list2=[6,7,8,9,10]
# num_list1.extend(num_list2)
# print(num_list1)







# #  to print the return values 
# num_list = [6,3,7,0,1,2,4,9]
# print(num_list.insert(2,250))







# # Program that uses the assignment operator to assing one list to another list variable
# num_list1 = [ 1,2,3,4,5]
# num_list2 = num_list1
# print(num_list2)





# # Program to show the sort() mentioned
# list1= ['1','a',"abc",'2','B','Def']
# list1.sort()
# print(list1)






# # Program to delete item using empty list
# list = ['p','r','o','g','r','a', 'm']
# list[2:5] = []
# print(list)






# # Stack  ///////////////////////////////////

# # Program to illustrate operation on a stack 
# stack = [1,2,3,4,5,6,7]
# print("Original stak is :" , stack)
# stack.append(8)
# print("after push operation:",stack)
# stack.pop()
# print("after pop operation:",stack)
# last_element_index= len(stack)-1
# print("Value obtained after peep operation is : ",stack[last_element_index])





# # Program to make a list of cubes
# cubes =[]
# for i in range(11):
#     cubes.append(i**3)
# print("Cubes of numbers from 1-10 :",cubes)



# # Program to combien three lines of code into one
# cube = [i**3 for i in range (11)]
# print(cube)





# # Program to combile and print elements of two list using list comprehension
# print([(x,y) for x in [10,20,30] for y in [30,40,50] if x !=y])












#  Looping in Lists /////////////////////

# # Program to find the sum and mean of elements in a list
# num_list = [1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in num_list:
#     sum+=i
# print("total sum of element is :",sum)
# print("Average of a element: ",sum/len(num_list))






# # Program to illustrate the use of enumerate() to print an individual item and its index in the list 

# num_list=[10,20,30,40]
# for index , i in enumerate(num_list):
#     print(i,"is at ",index)











# # Program to print the index of values in alist
# num_list= [ 1,2,3,4,5]
# for i in range(len(num_list)):
#     print("index:",i)





# # Program to print the elements i the list using an irerator
# num_list = [1,2,3,4,5]
# it = iter(num_list)
# for i in range(len(num_list)):
#     print("Lelement at index ", i , "is ", next(it))





# # Program to create a list of numbers devisible by 2 or 4 using list comprehension 
# def check (x):
#     if (x % 2 ==0 or x%4==0):
#         return 1
    
# evens=  list(filter(check,range(10,55)))
# print(evens)




# # Program that adds 2 to every value i the list 
# def add(a):
#     a+=2
#     return a

# num_list=[1,2,3,4,5]
# new_list = list(map(add,num_list))  # map function the return the modified list 
# print(new_list)









# # Program to pass more than one sequence to the map() function

# def add(a,b):
#     return a+b

# num_list= [1,2,3,4,5]
# num_list1 = [1,2,3,4,5]
# num_list3 = list(map(add,num_list1,num_list))
# print(num_list, num_list1,"+",num_list3)







# # Program to calculate the sum of values in a list using the reduce() function .

# import functools # functools is a module that contains the function reduce()

# def add(a,b):
#     return a+b

# num_list=[ 1,2,3,4,5,6,7,8,9,10]
# print("sum of total values in list=",)
# print(functools.reduce(add,num_list))







# # Write a program that creates a list of numbers from 1-20 that are ither dividible by 2 or dibisible by 4 without using the filter function.
# div=[]
# for i in range(1,21):
#     if (i%2==0 or i%4==0):
#         div.append(i)

# print(div)






# # Write a program using filter function to alist of squares of numbers from 1-10 . Than use the for .... in construct to sum the elements in the list argument
 

# # from numpy import square
# def square(x):
#     return(x**2)


# squres=[]
# squres= list(filter(square,range(1, 11)))
# print("list of squared in the range 1-10 = ",squres)
# sum =0
# for i in squres:
#     sum+=i 

# print("total sum of:",sum)








# # Write a program the defines a list of countries that are a members of Bires.
# # check whether a county is a menber of BRICS or not.


# county=[ "Brazil","india","china", "Rissia","sri lanka"]
# is_member =input(" country")
# if is_member in county:
#     print(is_member,"in a BRICS")
# else:
#     print(is_member,"is not in  a BRICS")
    







# # Write a program to create a list of numbers in the range 1 to 10 . Than delete all he even numbers from the list and print thelfinal list.
# num_list =[]
# for i in range(1,11):
#     num_list.append(i)
# print("original list:",num_list)
# for index, i in enumerate(num_list):
#     if(i%2==0):
#         del num_list[index]
# print("after delete even numbe:",num_list)











# # Write  a program to print index at which a particular value wxists. If the value exists at multiple locations in the list, than print all the indices. 
# # Also ,count the number of times that value is repeated in the list.
# num_list=[1,2,3,4,5,6,5,7,4,3,2,1,]
# num = int(input("inter a value to be searched:",))
# i =0
# count=0
# while (i<len(num_list)):
#     if (num== num_list[i]):
#         print(num,"found at location",i)

#         count+=1
#     i+=1
# print(num,"total appers ",count,"times")















# # write a program that creates a list of words by combining the woeds in two individual lists

# list = []
# list1= ["hello ", " word"]
# list2= ["python "," progrmming"]
# for i in list1:
#     for j in list2:
#         word= i+j
#         list.append(word)
# print("list combining the woeds in two indivisul list is:", list)









# # Write a Program that forms a list of first character of every woed in another list.

# list1= ["hello","welcome","my","name","is ","Vaibhav"]
# letter=[]
# for i in list1:
#     letter.append(i[0])
# print(letter)






# # Write a program to remove all duplicates from a list.

# num_list= [ 1,3,4,5,3,4,5,6,3,2,7,89,8,7,8,9,]
# print("original list:",num_list)
# for i in range(len(num_list)):
#     val= num_list[i]
#     for j in range(len(num_list)):
#         if val== num_list[j]:
#             del num_list[j]

# print("after removing duplicated:", num_list)







 
# # write a program to create a list of numbers in the specified range in particular steps. Reverse the list and print its values.

# num_list=[]
# m= int(input("Enter the starting of the range:"))
# n= int(input("enter the ending of the range:"))
# o= int(input("enter the steps in the range:"))

# for i in range(m,n,o):
#     num_list.append(i)
# print("original list:", num_list)
# num_list.reverse()
# print("Reversed list",num_list)





# # Write a program to create a list of first 10 random integers. Then create two list - odd and Even List that has all odd and even values in the list respectively

# import random 
# num_list =[]

# for i in range(10):
#     val= random.randint(1,100)
#     num_list.append(val)
# print("list after gereate a random numbers",num_list)
# even_list=[]
# odd_list=[]
# for index in range(len(num_list)):
#     if (num_list[index]%2==0):
#         even_list.append(num_list[index])
#     else:
#         odd_list.append(num_list[index])
# print("even numbers list:",even_list)
# print("odd numbers list:",odd_list)









# # Write a program to create a list of first 20 odd numbers using the shortcut 
# odd = [2*i +1  for i in range(20)]
# print(odd)







# # Write a program that passes a list to a function that scales each element in the list by a factor of 10. Print the list values at differents stages to show
# #  that changes made to one list is automatically reflected in the other lis.

# def change(list1):
#     for i in range(len(list1)):
#         list1[i] = list1[i] * 10
    

# num_list= [1,2,3,4,5,6]
# print("original list:",num_list)
# change(num_list)

# print("after change num_list",num_list)








# #   write a program that has a list of both positive and negative numbers. Create another list using filter() that has only positive values.
# def is_positive(a): 
#     if a >= 0:
#         return a
# num_list = [ 1,-3,4,-4,-2,10,-45,-43,-3, 5,6,3,-5]
# List= []
# List = list(filter(is_positive,num_list))
# print("only positive numbers:", List)








# # Write a program that converts strings of all uppercase characters into strings of all lowercase character using the map() function 

# def to_lower(x):
#     return x.lower()

# list1= ["hello","WELLCOME", "friend","phyTHON"]
# list2 = list(map(to_lower,list1))
# print (list2)



# # Write a  program that conversts string of all uppercase character into  steing of all lowercase character using map() function.
# def to_lower(list1):
#     return list1.lower()

# def to_upper(list1):
#     return list1.upper()
# #  for upper
# list1 = ['hello ', 'Vaiibhav']
# list2 = list(map(to_lower,list1))
# print(list2)
# #  for upper
# list3= list(map(to_upper,list1))
# print(list3)






# # write a program using map() function to create a list of squre of number in the range 1-10
# def square(x):
#     return x*x
# squ_list = list(map(square, range(1,20)))
# print(squ_list)





# # write a program to combine values in two in two lists using list comprehension. combine only those values of a list that are multiples of values in the firsy list

# print([(x,y) for x in [ 10,20,30,40,50] for y in [ 60,70,80,90,100] if y%x == 0 or x%y ==0 ])









# # write a program that converrt a list of temperature in clcius into Farenheit.
# def convert_to_f(str1):
#     return ((float (9/5)*str1) + 32)
# temp_in_c =[ 34.4 , 33, 22, 35.5, 22, 4.3]

# temp_in_f = list(map(convert_to_f,temp_in_c))
# print(temp_in_c)
# print(temp_in_f)










# # Write a program to find the largest value in  a list using reduce() function.
# import functools as ft

# # def max_ele(x,y):
# #     return x>y
# num_list =[ 22,43,54,66,44,2,3,5,56,77,34,56,98,4,44]
# print("Largest value in the list is :",ft.reduce(max, num_list))








# # write a program program  that has a list of functions that scales a number by a factor of 2,3,and,4. Call each function in the list on a given number

# l= [lambda x:x *2, lambda x:x*3 , lambda x: x*4]
# for i in l:
#     print(i(3))

# print("\n Multipying the value of 50 by we get :", (l[0](50)))











# # write a program to generate in the Fibonacci sequence and store it in a lis. Then find the sum of the even-valued.

# n= int (input ("Enter a number of terms:"))
# a= 0
# b= 1
# i = 2
# list1= [a,b]
# while i<=n :
#     s= a+b
#     list1.append(s)
#     a=b
#     b=s 
#     i+=1
# print(list1)
    






# # write a program to add two matrics (using nested lists).

# from re import L


# x= [[2,5,6],
#     [3,5,6],
#     [4,3,1]]

# y= [[4,4,6],
#     [3,4,6],
#     [4,2,1]]
# result= [[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] + y [i][j]
# for printarr in result:
#     print(printarr)






# # write a program to find the median of a list of numbers
# list1= []
# n = int(input("inter the number of elements to be :"))
# for i in range(n):
#     print("enter number ", i +1," : ")
#     num = int(input())
#     list1.append(num)
# print("sorted list is:")
# list1= sorted(list1)
# print(list1)
# i = len(list1) -1
# if n%2!=0:
#     print("median = ", list1[i//2])
# else:
#     print("median is : ",(list1[i//2] + list1[i+1//2])/2)















# # write a program to calculate distance between two points.  // confuse

# import math 
# p1 =[]
# p2 =[]
# x1 = int(input("Enter the X co-ordinate of starting point:"))
# y1 = int(input("enter the y co-ordinate of starting point:"))
# x2 = int(input("Enter the x co-ordinate form ending point:"))
# y2 = int(input("enter the y co-ordinate of ending point:"))

# p1.append(x1)
# p1.append(x2)
# p2.append(y1)
# p2.append(y2)

# distance = math.sqrt(((p1[0]-p2[0])**2)+ ((p1[1]-p2[1])**2))
# print("distance = %f" %distance)

















# ///////////////////////////////////// Tuple /////////////////////////////////////////////////////////////////////////////////////////////////////


# #  program to  show how to create the  differents types of tuples
# tup1 = ()
# print(tup1)


# tup2 = (5)
# print(tup2)



# tup1 = (1,2,3,4,5)
# tup2= ('a','b','c','d')
# tup3 = ("abc","gg", "ghi")
# tup4= ("as",44," 3.3",4.4,4,"""ASDFE"s""")
# print(tup1)
# print(tup2)
# print(tup3)
# print(tup4)








# # NOTE default tuple without parentheses

# a= 3,34,55,33
# print(type(a))
# print(a)

# # Program to demonstrate the necessory of having a comma in the tuple 
# tup = (33,)
# print(tup)
# print(type(tup))

# tup = (33)
# print(tup)   /// #without comma class is int
# print(type(tup))






# #  program to illustrate the use of divmod() function

# qoutient,remainder = divmod(100,3)
# print(qoutient)
# print(remainder)





# # program to illustrate the use of slice operation to retrieve value(s) stored in tuple 


# tup1=(1,2,3,4,5,6,7,8,9,10)
# print("Tup1[3:6]",tup1[3:6])
# print("tup1[:8]",tup1[:8])
# print("tup1[4:]",tup1[4:])
# print("tup1[:]",tup1[:])
# print('tup1[1::2]',tup1[0::2])
# print('tup1[1::2]',tup1[::2])






# tup1=(1,3,2)
# tup2= (5,6,7)
# print(tup1+tup2)




# # deleting elements in Tuple
# # Program to illustrate that tuples are immutable 
# tup1= (1,3,4,6)
# del tup1[3]   # doesn't support item delation
# print(tup1)


# # program to delet a tuple 
# tup1=(3,5,6,6)
# del tup1
# print(tup1)







# # Program to dhow the different ways of tuple assignment
# (val1, val2, val3) = (1,2,4)
# print(type(val2))

# tup2=val1,val2,val2
# print(tup2)
# print(type(tup2))

# tup2 = (100,200,300)
# val1,val2,val3 = tup2
# print(tup2)
# print(val2)









# # Progem to return the highest as well as the lowest values in the list 

# def max_min(val):
#     x= max(val)
#     y=min(val)
#     return (y,x)
# val = (1,3,55,66,3,55,64,67,87,94,33)
# maxi, mini= max_min(val)
# print("max in val is",maxi)
# print("main in val is",mini)








# # Nested Tuples
# # Program to demonstrate the use of nested tuples
# stud= (("vaibhav","BCS","80"),("banti","BCS","95"))
# print(type(stud))
# for i in (stud):
#     print(i)





# # Program to print the name of the topper and her marks in 4 subject wherein the marks are specified as a list in the tuple topper
# topper = ("vaibhav",[94,95,96,99])
# print("CLASS TOPPER",topper[0])
# print("high score in 4 subject",topper[1])











# # program to demonstrate the use of index method
# tup=(1,3,5,6,6,4,5,)
# print(tup.index(6))




# # program to print the location at which an element in proesent in the list using the index() method
# student=("vaibhav","maggi","gajanan","sanket","kailas")
# print(student.index("kailas"))

# print(student.index("santosh"))













# # # program to count the number of times letter "v" appers in the specified string

# tup= "(vvjhvvasjkvavvavavvhuvvjvhv)"
# appers = tup.count('v')
# print(appers)
# print(type(tup))




# def double(a):
#     return ([i*2 for i in a])

# tup = 1,2,3,4
# print(type(tup))
# print("original value",tup)
# print("after call value",double(tup))










# # Program to manipulate efficienty each value that is passed to the tuple using variable length arguments
# def display(*tup):
#     print(tup)
# tup = (1,3,45,6,6,77)
# display(tup)








# # Program t illustrate scatter in terms of Tuple
# tup =(56,3)
# q, r = divmod(tup)
# print(q,r)                #TypeError: divmod expected 2 arguments, got 1


# tup =(56,3)
# q,r= divmod(*tup)
# print(q,r)








# # program to show the use of zip function
# tup = (1,2,3,4,5)
# list1= ['a','b','b','d']
# a=list(zip(tup,list1))
# print(type(a))
# print(a)






# program to use zip()fuction on variable-length sequences 
# tup = (1,2,3,4,5)
# list1= ['a','b','b','d']
# a=list(zip(tup,list1))
# print(a)






# # Program to print elements in a tuple using for loop
# # tup= (1,4,6,3,6,6,77)
# tup1= ((1,"s"),(2,"b"),(3,"f"),(2,"h"),(3,"w"))
# for i,j in tup1:
#     print(i,j)






# # write a program that uses enumerate() function to print elements as well as theier indeces.
# # tup=(1,3,5,6,4,3,)
# for i,element in enumerate("abcsefghigklm"):
#     print(i,element)





# # Program to sort a tuple of values 
# tup = (3,45,3,2,1,566,3,5,7,9,23)
# print(sorted(tup))






# # Program to illustrate string formatting function with tuple 
# tup = ("henna",89,34,4)
# print("%s got %d marks in csa and her aggregate was %.2f" %(tup[0],tup[1],tup[2]))






# # write a program to swap two values using tuple assignment.
# val1= 12
# val2=33
# print("val1",val1,"\nval2 ",val2)
# (val1,val2) =(val2,val1)
# print("val1",val1,"\nval2 ",val2)
# print(type(val1))







# # Write a program using a function that returns the area and circumference of a circle whose radius is passed as and argument.

# pi =3.14
# def cal_a_r(radi):
#     a= pi*radi*radi
#     b= 2*pi*radi
#     return a,b

# radius = float(input("enter a radius of circul:"))
# a = cal_a_r(radius)


# print("area of circle is: ",a[0])
# print("circomference of corcle is :",a[1])    #/////////// this is a optinal method not recommended














# # write a program that has a nested list to store toppers details. Edit the details and reprint the details.



# toppers = (('vaibhav','bca',80.3),('gajanan','bcs',93.2),('sanket','Btech',99.9))
# for i in toppers:
#     print(i)
# choice =input("do you want to edit the details:")
# if choice =="y":
#     name=input("Enter a name of the students whose detaails are to be edited:")
#     new_name=input("enter a new name:")
#     new_course= input("enter a corredt course:")
#     new_aggr= input("enter the correct aggregate:")

#     i =0
#     new_topper=()
#     while i<len(toppers):
#         if toppers[i][0]== name:
#             new_topper += (new_name, new_course,new_aggr)
#         else:
#             new_topper+=toppers[i]
#         i+=1
#     for i in new_topper:
#         print(i)
        







# #  write a program that scans an email address and forms a tuple of user name and domain
# addr= "vaibhavnagargoje@gmail.com"
# username,domain = addr.split("@")
# print("username:",username)
# print("domain",domain)








# # write a program that has a list of numbers (both postitive as bell as nagative.) make a new tuple that has only positive values from this list.list
# tup1 = (-44 ,-33 ,3 ,45,3 ,2,-5,45)

# new_tup=()
# for i in tup1:
#     if i >0:
#         new_tup+=(i,)

# print(new_tup)






# # write a program that accept different numbers of arguments and return sum of onlu the positive values passed to it.

# def sum_pass(*args):
#     sum=0
#     for i in args:
#         if i > 0:
#             sum+=i
#     return sum
    
# a=sum_pass(2,4,-3,-22,6,-5,1,5,-6,-66)
# print(a)










# # # write a two program that has two sequences. first  which stores some questions and second stores and the corresponding answere. use the zip()
# # function to form a valid question answer series.

# ques = ["roll_no","name","course"]
# ans =[14,"vaibhav","BCs"]
# for i,j in zip(ques,ans):
#     print("what is your name",i,"?")
#     print("my ",i,"is",j)





















# sets//////////////////********************************************************************************************************************************************

# set = {1,4,5,6,3,2,2,3,22}
# print(set)
# print(type(set))





# # program to convert a list of values into a set 
# s= set ([2,5,3,5,5,6,6,"abx",3.4,"a"])
# print(s)
# print(type(s))







# # program to create a set 
# list1 = [3,4,2,5,33]
# print(set(list1))
# tup1 = (3,4,2,4)
# print(set(tup1))
# str="adfafah"
# print(set(str))
# print(set("the my name is vaibhav and i am a pro coder".split()))




# # program to find intersection, union, and summetric difference between two sets 
# coders = set(["vaibhav","sanket","kailas","akshay","mauli"])
# analysts = set(["maggi","gajanan","shiv","mauli","vaibhav"])
# print("coders",coders)
# print("analysts",analysts)
# print("people working as codeder as well as analysts:",coders.intersection(analysts))
# print("all people",coders.union(analysts))
# print("people working as coder but not analystic",coders.difference(analysts))
# print("people working as analysts but not coders: ",analysts.difference(coders))
# print("people working in only one of the group: ",coders.symmetric_difference(analysts))



    









# # Progeam to illustrate updating of a set

# s= {2,4,2}
# print(type(s))
# print(s[0])







# # Program to iterate through a set
# s = set("hello")
# for i in s:
#     print(i,end="")















# # Write a program that generates a set of prime numbers and another set of odd numbers. Demonstrate th result of union, intersection,
# # diffrence and symmetric diffrence operations on these sets.

# odd = set ([x*2+1 for x in range(1,10)])
# print(odd)
# primes= set()
# # for i in range (2,20): # this algorithem is write by me.
# #     k=2
# #     for k in range(2,i):
# #         if i%k==0:
# #             break
# #     else:
# #         primes.add(i)
# # for i in range (2,20):
# #     j= 2
# #     flag = 0
# #     while (j<i)/2:
# #         # print(i)
# #         if i%j==0:
# #             flag= 1
# #             # print(i)
# #         j+=1
# #     if flag==0:
# #         primes.add(i)
# print(primes)

# print("Union:",odd.union(primes))
# print("Intersection:",odd.intersection(primes))
# print("Symmatric difference:",odd.symmetric_difference(primes))
# print("difference:",odd.difference(primes))










# Write a program that creates two sets. one of even numbers in range 1-10 and the other has all composite numbers in range 1-20
# demonstrate the use all(), issuperset(), and sum() functions on the sets.

# even= set([x*2 for x  in range(1,10)])
# print("evens",even)
# composite =set()
# for i in range (2,20):
#     j=2
#     flag=00
#     while (j<i)/2:
#         if i%j==0:
#             composite.add(i)
#         j+=1

# print("composite :",composite)
# print("superset:",even.issuperset(composite))
# print("all:",all (even))
# print("length of composite:",len(composite))
# print("sum of total numbers in even set:",sum(even))






# # write a program that create two sets - squares and cubes in range 1-10 deminstrate the use of update(). pop(), remove(), add() and clear () function.

# squ = set([x**2 for x in range(1,10)])
# cube = set([x**3 for x in range(1,10)])

# print("squres",squ)
# print("cube",cube)
# squ.update(cube)
# print(squ)
# squ.add(11*11)
# squ.add(11*11*11)
# print("after add 2 value:",squ)
# print("pop:",squ.pop())
# squ.remove(512)
# print("after remove:",squ)
# squ.clear()
# print(squ)








# # write a program that has a list of countries. Create a set of the countries and print the names of the countries in sorted order 

# countries = ["india","russia,", "china","brazil","america","england"]
# set1 = sorted(countries)
# set(set1)
# print(type(set1))
# print(set1)







#  //******************************************************************Dictionaries**************************************//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# program to create 10 key- value pairs where key is a number in the range 1-10 and the value is twice the nubmber

# dict1= {x:x*2 for x in range(1,10)}
# print(dict1)









# # program to access value stored in a dictionary 
# dict1 ={"roll_no":"16/1","name":"vaibhav","course":"bcs"}
# print(dict1["roll_no"])
# print(dict1["name"])
# print(dict1["course"])













# # program to add a new iten and modify an a item in the dictnary 
# dict1 ={"roll_no":"16/1","name":"vaibhav","course":"bcs"}
# print(dict1["roll_no"])
# print(dict1["name"])
# print(dict1["course"])
# dict1["marks"]= 95
# print(dict1)
# dict1["name"]='xyz'
# print(dict1)





# # Program to demonstrate the use of del statement and clear() function.
# dict1= {"roll":22,"name":"vaibha","course":"bcs"}
# print("name",dict1["name"])
# del dict1["course"]
# print("after del course dict1",dict1)
# dict1.clear()
# print("after clear",dict1)
# del dict1
# print("dict1 dose not exit.....")
# print(dict1)












# # Program to randomly pop() or remove an element from a dictionary 

# dict1 = { "roll_no":44,"name":"vaibhav","cource":'bcs',"langauge":"python","processor":"i5"}
# print("name is a ",dict1.pop('name'))
# print("dictionary after poping name is ",dict1)
# print("cource is",dict1.pop("cource"))
# print("dictionary after poping the cource",dict1)
# print("Randomly popping any item",dict1.popitem())






# # Program to illustrate the use of duplicate keys in a dictionary

# dict1 = {"roll":12,"name":"vaibhav","cource":"bcs","name":"sanket"}
# print(dict1)
# print("dict[roll]",dict1["roll"])
# print("dict['name']",dict1['name'])










# # program to illustrate the use of mutable keys in a dictionary


# dict1 = {"roll":12,"name":"vaibhav","cource":"bcs","name":"vaibhav"}
# print("roll",dict1["roll"])











# # Program to use tuple as keys 
# dict1 = {(1,3),([3,2,1])}
# print(type(dict1))





# # Program to check signal key in a dictionary 
# dict1 = {"roll":12,"name":"vaibhav","cource":"bcs","name":"vaibhav"}
# if 'cource' in dict1:
#     print(dict1['name'])








# # program to sort keys of a dictionary 
# dict1 = {"roll":12,"name":"vaibhav","cource":"bcs","name":"vaibhav"}
# print(sorted(dict1.keys()))






# # Program to access items in a dictionary using for loop 
# dict1 = {"roll":12,"name":"vaibhav","cource":"bcs","name":"vaibhav"}
# print("keys:",end=" ")
# for key in dict1.keys():
#     print(key,end=" ")

# print("\nValues:",end="")
# for value in dict1.values():
#     print(value,end=' ')
# print("\n dictionary :",end=" ")
# for dictionary in dict1.items():
#     print(dictionary,end=" ")








# # Program to illustrate nested dictionary (i.e., use of one dictionary inside another)


# student = {"vaibhav":{"cs":80,"dsa":70},

#             "gajanan":{"cs":90,"dsa":80},
#             "sanket":{"cs":100,"dsa":78,"math":75}
            
#         }
# for kay, value in student.items():
#     print(kay,value)
















# # Program to add an item in a set 
# sport = set(["cricket",'tennis'])
# print(sport)
# sport.add("baseball")
# print(sport)







# # # Program to write fibonachi sereies using dictionary
# dict1 = {0:0,1:1}

# def fibo(n):
#     if n not in  dict1:
#         val = fibo(n-1) + fibo(n-2)
#         dict1[n]= val
#     return dict1[n]
        
    
# num = int(input("Ente a number :"))
# print("fibo series",fibo(num))







# # write a program  that creates a dictionary of cubes of odd numbers in the range 1- 10  

# dict1 = { x:x**3 for x in range(10) if x%2==1}
# print(dict1)









# # write a program that prompts the user to enter a message. Now count and print the number of occurrences of each character.
# def mass_count(mass):
#     letter_count= {}
#     for i in mass:
#         letter_count[i] = letter_count.get(i,0)+1
#     return letter_count
# massage = input("enter the massage:")
# print(mass_count(massage))








# # # write a program to store a sparse matrix as a dictionary
# matrix = [ [ 0,0,0,1,0],
#             [ 2,0,0,0,3],
#             [0,0,0,4,0]
#           ]

# dict1 ={}
# print("Sparse Matrix")
# print(len(matrix))
# print(len(matrix[0]))
# for i in range(len(matrix)):
#     print("\n")
#     for j in range(len(matrix[i])):
#         print(matrix[i][j],end=' ')
#         if matrix[i][j] != 0:
#             dict1[(i,j)] = matrix[i][j]
    
# print("\n Sparse mtrix can be ifficiently represented as Dictionary:")
# print(dict1)       



# # write a program that inverts  a dictionary . That is , it makes key of one dictionary value of another and vice versa. 

# dict1 = {"roll": 34, "name":"vaibhav","course": "computer science"}
# invert_dict = {}
# for key,val in dict1.items():
#     invert_dict[val]=key
# print("original dict",dict1)
# print("after inverted",invert_dict)






# # Write a program that has dictionary of names of students and a list of their marks in 4 subjects. create another dictionary form this dictionary that has name of the 
# # student and their total marks. Find out the  topper and his/her score.

# mark = { "vaibhav":[78,98,89,88],"gajanan":[99,89,87,98],"soni":[23,75,65,35]}
# total= 0
# a = mark["vaibhav"]
# print(a)
# total_mark = mark.copy()
# for key,val in mark.items():
#     total=sum(val)
#     total_mark[key]= total
# print(total_mark)
# max=0
# toper= ' '
# for key ,val in total_mark.items():
#     if val>max:
#         max= val
#         toper = key 
# print(toper,"mark is :",max )











# # Write a program that print a disogram of frequencies of characters occurring in a message 

# mes = 'Hello all, good morning ... Welcome to the  World of Python'
# mes=mes.lower()
# dict1 = dict()
# print(type(dict1))
# for word in mes:
    
#     if word not in dict1:
#         dict1[word]=1
#     else:
#         dict1[word]+=1
# print(dict1)
# for key ,val in dict1.items():
#     print(key,' ',val*"*")











## Write a program that promots the user to enter a filename. Open the file and print the frequency of each word in it.


# filename = input("enter the file name:")
# file= open(filename)
# count= dict()
# for line in file:
#     words = line.split()
#     for word in words:
#         if word not in count:
#             count[word]=1
#         else:
#             count[word]+=1
# print(count) 






# # write a program to count the numbers  of characters in the string and store them in a dictionary data structure 
# str1 = "hello, my name is vaibhav"
# len= len(str1)
# dict1 = {str1:len}
# print(dict1)
   



# # write a program that combiles the lists to a dictionary.

# keys= [ "name","age","course"]
# values= [ "Vaibhav", 21,"bcs"]
# detail = zip(keys,values)
# print(type(detail))
# detail=dict(detail)
# print(type(detail))
# print(detail)




# @ python data structure is now end ////////////////////////////////////////////////////////////////////////////////////////////****************************************************************************************************

















# # ****************************** iterator and Generator **********************************************************************************************************************************


# # Program that uses iter () to travers through the elements of a list 
# list1 = [ 1,3,5,7]
# it = iter(list1)
# # print(set(it)) # cheak for testing
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())















# # Program to traverse through the elements of a list using iter() and for loop 
# list1 = [1,3,4,6,7,8]
# it = iter(list1)
# for i in it:
#     print(i)







# # Program to traverse a list using nest().
# import sys
# list = [ 1,3,5,7]
# it = iter(list)
# while True:
#     try:
#         print(next(it),end=" ")
#     except StopIteration :
#         print("\n All the elements have already been accessed.. No more elements")
#         sys.exit()









# # Program to show that next () is not a implemented on a list 
# list = [1,3,5,4]
# next(list)











# # Program that creates an eterator that goes up indefinitely 
# class counter():
#     val =0
# def __iter__(self):
#     return self
# def __name__(self):

#     val = self.val
#     self.val+=1
#     return val

# c= counter()
# while True:
#     print(next(c))












# # Program that creates an iterator to iterate over astring of letters.
# class iterator:
#     def __init__(self,string):
#         self.str= string
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index >= len(self.str):
#             raise StopIteration
#         str = self.str[self.index]
#         self.index += 1 
#         return str


# it = iterator("hello word")
# for ch in it:
#     print(ch, end=" ")








# # Program to creates an iterator to print squres of numbers .
# class square:
#     def __init__(self):
#         self.val= 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.val+=1
#         return self.val**2


# sq = square()
# count= 0
# for num in sq:
#     print(num,end=" ")
#     if count==10:
#         break
#     count+=1









# # Program that generates an iterator to print odd numbers from 1-20
# class odd:
#     def __iter__(self):
#         self.val=1
#         return self
#     def __next__(self):
#         val = self.val
#         self.val +=2
#         return val

# o= odd()
# for i in o:
#     print(next(o),end= " ")
#     if o.val==21:
#         break









# # Program to illustrate the use of a generator .

# def square():
#     number = 2
#     while True:
#         yield number
#         number *=number


# sq = square()
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))






# # Program that creates a generator and use a for loop to print the Element

# def print_mes():
#     yield "hello"
#     yield "woed"
# gen = print_mes()
# for i in gen:
#     print(i,end= " ")








# # Program to create a generator that starts counting from 0 and raises an exception when counter wquals to 10 
# def counter():
#     val = 0
#     while True:
#         yield val
#         val+=1
#         if val ==10 :
#             raise StopIteration

# c = counter()
# try:
#     while True:
#         print(next(c),end=" ")
# except StopIteration:
#     print("Over")









# # Program to create a generator to print the fibonacci numbers .
# def fibo():
#     a,b= 0,1
#     while a<10:
#         yield b
#         a,b=b,a+b
# iter = fibo() 
# for  i in iter:
#     print(i,end="  ")




# # Program to create a generator that reverse a string.
# def reverse(mass):
#     length = len(mass)
#     for i in range(length-1,-1,-1):
#         yield mass[i]
# mes= "hello"
# for char in reverse(mes):
#     print(char, end=" ")





# # Program to illustrate the use of generator expression 
# list1  = [ 1,3,5,6,7]
# print([x**2 for x in list1])
# nlist = (x**2 for x in list1)
# for i in range(10):
#     print(next(nlist),end=" ")





















