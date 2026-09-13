# Lesson 03 strings operations

s = "Hello, Python" # 12
print(s)
# Index:  0  1  2  3  4  5  6  7  8  9  10 11 12
# Char:   H  e  l  l  o  ,     p  y  t  h  o  n

print(s[8])
print(s[5:10]) # , @ 5th index
print(s[-3: -1])
print(s[::-1])
# Functions
# (len(s))  # length of the string


a = "Hello"
b = "Python" 
c = a + b
c = a + ", " + b # Hello, Python
print(c) # Hello, Python
print(b * 3) # PythonPythonPython
# in operator
print("th" in c) # True

# print(c.upper()) # HELLO, PYTHON
# print(c.lower()) # hello, python
# print(c.capitalize()) # Hello, python
# print(c.title()) # Hello, Python
# print(c.replace("Python", "World")) # Hello, World

raw = "  hello python  "
print(raw)   
print(raw.strip())
print(raw.lstrip())    # "python  "
print(raw.rstrip())    # "  python"


# split
# url = "api.github.com/users/octocat/repos"
# parts = url.split("/")      # ["api.github.com", "users", "octocat", "repos"]
raw = "hello python, how are you"
sp = raw.split() # ['hello', 'python'] # ["hello", "python,", "how", "are", "you?"]
print(sp)

raw = "hello python, how are you, yes"
sp = raw.split(",") # ["hello python', ' how are you ', 'yes']
#sp = raw.split(", y") # ["hello python', ' how are you ', 'es']
print(sp)

raw = "https://www.google.com"
sp = raw.split(".") # ["https://www", "google", "com"]
#sp = raw.split("//") # ["https:", "www.google.com"]
print(sp)


z = "www.google.com"
j = "/"
print(j.join(z))  # "w/w/w/./g/o/o/g/l/e/./c/o/m"

text = "Hello, Python"
# print(text.find("Python"))      # 7
# print(text.count("l"))          # 2
# print(text.startswith("Hello")) # True
# print(text.endswith("Python"))  # True

multiline = """
first
second
third
"""
print(multiline) # first second third

# 04_regular_expression.py