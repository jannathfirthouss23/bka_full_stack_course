# REGEX
"""
    \d      digit
    \D      non-digit
    \w      word char
    \W      non-word char
    \s      whitespace
    \S      non-whitespace
    .       any char
    ^       start of string
    $       end of string
    |       or
    ?       optional
    *       0 or more
    +       1 or more
    {n}     exactly n
    {n,m    } n to m
    [abc    ] any of a,b,c
    [^ab    c] none of
    (...    ) capture group
    (?:.    ..) non-capture group
    (?P<    name>...) named group
"""

import re

## DIGITS ONLY

print(bool(re.fullmatch(r"\d+", "12345")))          # True
print(bool(re.fullmatch(r"\d+", "12a45")))          # False

## LETTERS ONLY

print(bool(re.fullmatch(r"[A-Za-z]+", "Hello")))    # True
print(bool(re.fullmatch(r"[A-Za-z]+", "Hello1")))   # False

## ALPHANUMERIC

print(bool(re.fullmatch(r"[A-Za-z0-9]+", "abc123")))    # True
print(bool(re.fullmatch(r"[A-Za-z0-9]+", "abc 123")))   # False

## LOWERCASE ONLY

print(bool(re.fullmatch(r"[a-z]+", "hello")))       # True
print(bool(re.fullmatch(r"[a-z]+", "Hello")))       # False

## UPPERCASE ONLY

print(bool(re.fullmatch(r"[A-Z]+", "HELLO")))       # True
print(bool(re.fullmatch(r"[A-Z]+", "Hello")))       # False

## EXACT LENGTH

print(bool(re.fullmatch(r"\d{4}", "2026")))         # True (exactly 4 digits)
print(bool(re.fullmatch(r"\d{4}", "20260")))        # False

## LENGTH RANGE

print(bool(re.fullmatch(r"\w{3,8}", "alice")))      # True (3 to 8 chars)
print(bool(re.fullmatch(r"\w{3,8}", "al")))         # False
print(bool(re.fullmatch(r"\w{3,8}", "alexander1")))  # False

## OPTIONAL CHARACTER (?)

print(bool(re.fullmatch(r"colou?r", "color")))      # True
print(bool(re.fullmatch(r"colou?r", "colour")))     # True

## ONE OR MORE (+)

print(bool(re.fullmatch(r"a+", "aaa")))             # True
print(bool(re.fullmatch(r"a+", "")))                # False

## ZERO OR MORE (*)

print(bool(re.fullmatch(r"a*", "aaa")))             # True
print(bool(re.fullmatch(r"a*", "")))                # True

## OR PATTERN (|)

print(bool(re.fullmatch(r"cat|dog|bird", "cat")))   # True
print(bool(re.fullmatch(r"cat|dog|bird", "fish")))  # False

## CHARACTER NEGATION ([^...])

print(bool(re.fullmatch(r"[^0-9]+", "hello")))      # True (no digits)
print(bool(re.fullmatch(r"[^0-9]+", "hello1")))     # False

## STARTS WITH (^)

print(bool(re.match(r"^Mr", "Mr. Smith")))          # True
print(bool(re.match(r"^Mr", "Dr. Smith")))          # False

## ENDS WITH ($)

print(bool(re.search(r"\.com$", "site.com")))       # True
print(bool(re.search(r"\.com$", "site.org")))       # False

## EMAIL

email_pattern = r"[\w.-]+@[\w.-]+\.\w+"
print(bool(re.fullmatch(email_pattern, "alice@example.com")))       # True
print(bool(re.fullmatch(email_pattern, "alice@@example.com")))      # False
print(bool(re.fullmatch(email_pattern, "alice.com")))               # False

## PHONE (10 digits)

print(bool(re.fullmatch(r"\d{10}", "9876543210")))      # True
print(bool(re.fullmatch(r"\d{10}", "987654321")))       # False

## PHONE WITH OPTIONAL COUNTRY CODE

phone_pattern = r"(\+91)?\d{10}"
print(bool(re.fullmatch(phone_pattern, "9876543210")))      # True
print(bool(re.fullmatch(phone_pattern, "+919876543210")))   # True

## PHONE WITH DASHES

print(bool(re.fullmatch(r"\d{3}-\d{3}-\d{4}", "555-123-4567")))     # True

## URL

print(bool(re.match(r"https?://", "https://example.com")))      # True
print(bool(re.match(r"https?://", "http://example.com")))       # True
print(bool(re.match(r"https?://", "ftp://example.com")))        # False

## GROUPS - EXTRACT PARTS

m = re.fullmatch(r"(\w+)@(\w+)\.(\w+)", "alice@example.com")
print(m.group(0))           # alice@example.com
print(m.group(1))           # alice
print(m.group(2))           # example
print(m.group(3))           # com
print(m.groups())           # ('alice', 'example', 'com')

## NAMED GROUPS

m = re.fullmatch(r"(?P<user>\w+)@(?P<domain>[\w.]+)", "alice@example.com")
print(m.group("user"))      # alice
print(m.group("domain"))    # example.com
print(m.groupdict())        # {'user': 'alice', 'domain': 'example.com'}
