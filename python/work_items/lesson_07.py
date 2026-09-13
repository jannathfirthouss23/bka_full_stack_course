# lesson 07
# LIST

x = 10 # &123
y = "string" # &321
mixed = [10,"string",10] # &456
      #   0     1     2
print(mixed)
print(y[2])
print(*mixed) # spread operator - removes list and print each
# output: 10 string 10

mixed.append("20") # its add one word
mixed.insert(1, "hey") # output: [10, "hey", "string",10, '20']
mixed.pop()        # its remove last one word
mixed.pop(0) # index # its remove 10 word
mixed.remove("string") # value   

mixed[0] = "world"

print(mixed)

# TUPLE - Accept Duplicate, but couldn't able to modify
# TUPLE - READ ONLY

tuples = (10, 20, 30, 40, 10)

print(tuples)
print(tuples.count(10))
print(tuples, len(tuples))
print(tuples[1],tuples[0:2], tuples[::-1], tuples[-1])
print(*tuples) # spread operator - removes tuples and print each

# SET - NO DUPLICATES & SORTED AUTOMATICALLY & NO INDEXING

s1 = {11, 11, 1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s2.add(9) # add
s1.discard(2) # remove
s1.update([10, 20]) # add
s1.remove(10)
s1.pop()

print(s1)
print(s1 | s2) # union
print(s1 & s2) # intersection

print(s2)


# DICTIONARY

student = {
    "name": "Alice",
    "age": 30,# key
    "grade": "A", 
}

print(student)
print(student.get("name"), student["name"])
print(student, len(student))

student["age"] = 40
student.update({"city": "New York"}) # new value
# print(student) 'name': 'Alice', 'age': 40, 'grade': 'A', 'city': 'New York'
student.pop("city") # key name
student.popitem() # last item

print("name" in student) # True
print(list(student.keys()), list(student.values()), list(student.items()))
# ['name', 'age'] ['Alice', 40] [('name', 'Alice'), ('age', 40)]

print(student) # {'name': 'Alice', 'age': 40}