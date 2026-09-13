# FUNCTIONS

def printing(name): # 2+ usage  # name is called parameter
    print(f"Hello {name}")

printing("Alice") # "Alice" is called argument
printing("Bob")



# RETURN VALUES

def addition(a, b = 1): # 3+ usage
    return a + b

x = addition(1)
y = addition(2, 2)
z = addition(3, 3)

print(x, y, z) # output 2 4 6


# EXCEPTIONS

try:
    print(10/0)
    # print(10/1)
except Exception as error:
    print(error)

print("Hello world")

# class work

def addition(j,f = 1):
   return j + f
   
def subtraction(j,f):
   return j - f
   
def multiplication(j,f):
   return j * f
   
def divition(j,f):
   try:
      return j / f
   except Exception as zero:
       print(zero)

   
a = addition(1)
b = subtraction(2,2)
m = multiplication(3,3)
d = divition(4,4)

print(a,b,m,d)


# CLASS - OOPS

class math: # 3+ usages
    #def __init__(self, a, b): # Constructor (optional)

     def addition(self, a, b = 1): # Methods 1 usage
         return a + b

     def subtraction(self, a, b = 1): # Methods 1 usage
         return a - b 

     def multiplication(self, a, b = 1): # Methods 1 usage
         return a * b

     def divition(self, a, b = 1): # Methods 1 usage
        return a / b

math_1 = math()
a = math_1.addition(1, 2)
b = math_1.subtraction(1, 2)
c = math_1.multiplication(1, 2)
d = math_1.divition(1, 2)
#e = math_1.pi()

print(a, b, c, d) # output 3 -1 2 0.5

class math:
     def __init__(self, a, b): # Constructor (optional)
         self.a = a
         self.b = b  
     def addition(self):
         return self.a + self.b

     def subtraction(self): 
         return self.a - self.b 

     def multiplication(self): 
         return self.a * self.b

     def divition(self): 
        return self.a / self.b

math_1 = math(1, 2)
a = math_1.addition()
b = math_1.subtraction()
c = math_1.multiplication()
d = math_1.divition()
#e = math_1.pi()

print(a, b, c, d) 