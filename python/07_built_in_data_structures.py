# LIST

nums = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]

print(nums)
print(nums[0], nums[-1])
print(nums[1:4])
print(nums[::-1])
print(*fruits) # print("apple", "banana", "cherry)
print([*nums, *fruits])
print(len(nums))
print(20 in nums)

nums.append(60)                      # [10, 20, 30, 40, 50, 60]
nums.insert(0, 5)       # [5, 10, 20, 30, 40, 50, 60]
nums.pop()                           # 60 -> [5, 10, 20, 30, 40, 50]
nums.pop(1)
nums.remove(20)                      # [5, 10, 30, 40, 50]
print(nums)

nums[0] = 999
nums[0] = 5

nums.extend([60, 70])
nums.sort()
nums.reverse()
nums.count(10)
nums.index(30)
nums.clear()

# TUPLE - Accept Duplicate, but couldn't able to modify

t = (30, 10, 20, 30)
single = (42,)
empty = ()

print(t)
print(t[0], t[-1])
print(t[1:])
print(len(t))

x, y, z, a = t
print(x, y, z)

first, *rest = (1, 2, 3, 4, 5)
print(first, rest)

a, b = 5, 10
a, b = b, a
print(a, b)

t.count(10)
t.index(20)

# SET - Could not accept Duplicate, also sort automatically

s1 = {11, 11, 1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1)
print("=====", {3, 1, 2, 2, 3, 3, 3})

s1.add(6)
s1.discard(2)
print(s1)

print(s1 | s2)      # union
print(s1 & s2)      # intersection
print(s1 - s2)      # difference
print(s1 ^ s2)      # symmetric difference

print(3 in s1)

s1.update([10, 20])
s1.remove(10)
s1.pop()
s1.issubset(s2)
s1.isdisjoint({100})

fs = frozenset([1, 2, 3])

# DICT

student = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}

print(student)
print(student["name"])
print(student.get("email", "N/A"))
print(len(student))

student["age"] = 23
student["email"] = "alice@example.com"
print(student)

del student["email"]
print(student)

print("name" in student)
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

student.update({"city": "Boston"})
student.pop("age")
student.popitem()
student.setdefault("country", "USA")

print(student)

# ARRAY

from array import array

int_arr = array("i", [10, 20, 30, 40, 50])
float_arr = array("f", [1.1, 2.2, 3.3])

print(int_arr)
print(int_arr[0], int_arr[-1])
print(int_arr.tolist())

int_arr.append(60)
int_arr.extend([70, 80])
print(int_arr.tolist())

int_arr.insert(0, 5)
int_arr.remove(5)
int_arr.pop()
print(len(int_arr))