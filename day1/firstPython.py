# print("Hello world")
"""
import sys
print(sys.version)
"""

# indent is important for python programming
# we need to at least 1 space and maximum up to programmer
"""
if 5 > 2:
     print("Five is grater then 2")
"""

# python variables
# also we can make comment multiple line using   """
"""
x= 3
y = 5
z = "hello world"
if y>x:
  print( z) 
"""

# we can check type of python variable
"""
x= 4
y= "akash"
print(type(x)) #int
print(type(y)) #str

"""

# we can assign another value in a variable
"""
x= 4
x= "akash"
print(x)

"""

# we can made a number to string , a integer to float and also we can make a float to integer
"""
x= 6
print(x)
print(type(x))
y = str(x)
print(y)
print(type(y))
z= float(x)
print(z)

"""

# we can assign a value in a variable on string type using "double quote" or 'single quote'
"""
x= "akash"
y ='batas'
print(x, y)

"""
#python is case sensitive => here A will not replace the value of a
"""
a = "I love my country ,"
A = "I dont love my country"
print(a, A)

"""

#the legal formats of variable name
"""
myvar = "John"  
my_var = "Von"  #Snake Case
myVar = "Mon"   #Camel case
MyVar = "Gon"   #Pascal case
_my_var = "Don"
MYVAR = "Kon"
myvar2 = "Gon"

print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)
"""

#the illegal formats of the variable name
"""
2myvar = "John"
my-var = "John"
my var = "John

"""

# we can assign multiple value in multiple variable in a time
"""
x, y, z = "a", 2, True
print(x, y, z)

"""

#we can set a single value in multiple variables
"""
a= b= c = "single value in multiple variable, "
print(a, b, c)    #single value in multiple variable
"""

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacki
"""
a= [2, 4, "akash", True,]
x,y, z, t= a
print(x,y, z, t)   # 2 4 akash True

"""
# we can use   , +   to print multiple variable
"""
x="how "
y="are "
z= "you"
print(x+ y+z)   # how are you

"""
# + operator not only use for print multiple variable also it used of add operation 
"""
x=4
y=6
print(x+y)  #10
"""

# we can't print multiple type of value using  +  operator for print multiple type of value we need   ,
"""
x= 2
y= "a"
print(x+y)  #it will give error
print(x, y) #2a

"""

