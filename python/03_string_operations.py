s = "Hello, Python"

print(len(s))
print(s[0], s[-1], s[7:13])
print(s[::-1])

a = "Hello"
b = "World"
print(a + b)
print(a * 3)
print("Python" in s)

print(s.upper())
print(s.lower())
print(s.title())
print(s.replace("Python", "World"))

raw = "  hello python  "
print(raw.strip())          # "python"
raw.lstrip()                # "python  "
raw.rstrip()                # "  python"

url = "api.github.com/users/octocat/repos"
parts = url.split("/")      # ["api.github.com", "users", "octocat", "repos"]
print(parts)
print(parts[2])             # api.github.com
print(parts[-1])            # repos

path = "/".join(parts[3:])
print(path)                 # users/octocat/repos

csv = "apple,banana,cherry"
print(csv.split(","))

text = "Hello, Python"
print(text.find("Python"))      # 7
print(text.count("l"))          # 2
print(text.startswith("Hello")) # True
print(text.endswith("Python"))  # True

print("abc".isalpha(), "123".isdigit(), "abc123".isalnum())

name, score = "Alice", 92.5
print(f"{name} scored {score:.2f}")
print(f"{name:<10}|{score:>10.2f}")

print("Line1\nLine2")
print("Tab\there")
print(r"Raw: C:\Users\name")

multiline = """first
second
third"""
print(multiline)

print("hello".capitalize())
print("HELLO".swapcase())
print("42".zfill(5))
print("hi".center(10, "*"))
print("abc".index("b"))

