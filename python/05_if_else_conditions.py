age = 18

if age >= 18:
    print("adult") # Indentation
else:
    print("")

ageResult = "adult" if age >= 18 else ""
print(ageResult)

temperature = 35
if temperature > 30:
    print("hot")
else:
    print("not hot")

tempResult = "hot" if temperature > 30 else "not hot"
print(tempResult)

num = 7
if num % 2 == 0:
    print("even")
else:
    print("odd")

numResult = "even" if num % 2 == 0 else "odd"
print(numResult)

score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

scoreResult = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(scoreResult)

age = 25
has_license = True
if age >= 18 and has_license:
    print("can drive")

print("can drive" if age >= 18 and has_license else "")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("weekend")

dayResult = "weekend" if day in ("Saturday", "Sunday") else "weekday"

fruit = "apple"
if fruit in ["apple", "banana", "cherry"]:
    print("fruit found")

print("fruit found" if fruit in ["apple", "banana", "cherry"] else "not found")

x = 10
label = "even" if x % 2 == 0 else "odd"
print(label)

age = 25
has_id = True
has_ticket = True

if age >= 18:
    if has_id:
        if has_ticket:
            print("welcome")
        else:
            print("buy ticket first")
    else:
        print("ID required")
else:
    print("adults only")

print("welcome" if age >= 18 and has_id and has_ticket else "buy ticket first" if age >= 18 and has_id else "ID required" if age >= 18 else "adults only")