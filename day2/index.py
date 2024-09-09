# we can declare a variable inside a function It will call function scope , we can access those variables only in that function
"""
def myFunc():
  x="Akash"

myFunc()

"""

#also we can make a variable function scope to global scope using global key keyword
"""
def myFunc():
  global x
  x= "Bangladesh"

myFunc()
print(x)

"""

#