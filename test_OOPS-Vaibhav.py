
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






# Program to illustrate the use of special method in python classes



obj = abc("vaibhav",21)






















