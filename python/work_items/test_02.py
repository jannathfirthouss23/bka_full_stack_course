# LESSON 5

age = 60
gender = ""

if age < 18:
    if gender == "Male":
        print("You are a male.")
    else:
        print("You are a female.")
    print("You are not old enough.")
elif age > 18 and age < 60:
    print("You are old enough.")
    age = age + 1
    print("Next year you would be", age, "years old")
elif 60 <= age < float('inf'): # POS INFINITY
    print("You are a senior citizen.")
else:
    print("You are exactly 18!")

x = "You are not old enough." if age < 18 else "You are old enough." if age > 18 else "You are exactly 18!"
print(x)

print("=" * 60)

# LESSON 6

match gender:
    case "Male":
        print("You are a male.")
    case "Female":
        print("You are a female.")
    case _:
        print("You have no gender.")