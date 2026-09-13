# LIST

x = 10 # &123
y = "string" # &321
mixed = [10,"string",10] # &456

print(mixed, len(mixed))
print(mixed[1],mixed[0:2], mixed[::-1], mixed[-1])
print(*mixed) # spread operator - removes list and print each

mixed.append("new item")
mixed.insert(2, "hey")
mixed.pop()
mixed.pop(0) # index
mixed.remove("string") # value

mixed[0] = "world"

print(mixed)

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

s1.add(6) # value
s1.discard(2) # value
s1.update([10, 20])
s1.remove(10)
s1.pop()

print(s1)
print(s1 | s2) # union
print(s1 & s2) # intersection

# DICTIONARY

student = {
    "name": "Alice",
    "age": 30,
    "grade": "A",
}

print(student, len(student))
print(student.get("name"), student["name"])

student["age"] = 40
student.update({"city": "New York"}) # new value
student.pop("city") # key name
student.popitem() # last item

print("name" in student)
print(list(student.keys()), list(student.values()), list(student.items()))

print(student)