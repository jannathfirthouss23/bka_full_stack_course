# lesson 5: if else elif

# if
# elif
# else

age = 18

if age > 18:
    print("adult")
else:
    print("not adult")

age = 18

if age > 18:
    print("adult")
    age = age + 1
    print("next year you would be", age, "years old")
elif age < 18:    
    print("not adult")
else:
    print("you are exactly 18!") # output: you are exactly 18!


age = 62

if age < 18:
    print("you are not old enough")
elif age > 18 and age < 60:    
    print("you are old enough")
    age = age + 1
    print("next year you would be", age, "years old")   
elif 60 < age <  float('inf'): # POS INFINITY
    print("you are a senior citizen")   
else:
    print("you are exactly 18!") 