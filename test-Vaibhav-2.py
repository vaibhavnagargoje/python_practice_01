
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
# # s2= student('maggi',19,'coding lover','sweet')
# # s1.a='soonali'
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

# # import pyfiglet
# # a= pyfiglet.figlet_format("happay birthday snehal")
# # print(a)




# # x=0
# # while x<20:
# #     x=x+3
# #     print(x)
# # print(x)





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









# *******fuction as Object 

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




# Write a program that copies one Pthon script into another in such a way the all comment lines are skipped and not copied in the destination file.
with open ("01.py","rb")as file1:
    with open("02.py","wb") as file2:
        while True:
            buf= file1.readline()
            if len(buf)!=0:
                if buf[1] =='#':
                    continue
                else:
                    file2.write(buf)
            else:
                break

print("file copied!!")































