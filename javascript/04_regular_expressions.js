/*
    \d        digit
    \D        non-digit
    \w        word char
    \W        non-word char
    \s        whitespace
    \S        non-whitespace
    .         any char
    ^         start of string
    $         end of string
    |         or
    ?         optional
    *         0 or more
    +         1 or more
    {n}       exactly n
    {n,m}     n to m
    [abc]     any of a,b,c
    [^abc]    none of
    (...)     capture group
    (?:...)   non-capture group
    (?<name>...)  named group
*/

// DIGITS ONLY

console.log(/^\d+$/.test("12345"));
console.log(/^\d+$/.test("12a45"));

// LETTERS ONLY

console.log(/^[A-Za-z]+$/.test("Hello"));
console.log(/^[A-Za-z]+$/.test("Hello1"));

// ALPHANUMERIC

console.log(/^[A-Za-z0-9]+$/.test("abc123"));
console.log(/^[A-Za-z0-9]+$/.test("abc 123"));

// LOWERCASE ONLY

console.log(/^[a-z]+$/.test("hello"));
console.log(/^[a-z]+$/.test("Hello"));

// UPPERCASE ONLY

console.log(/^[A-Z]+$/.test("HELLO"));
console.log(/^[A-Z]+$/.test("Hello"));

// EXACT LENGTH

console.log(/^\d{4}$/.test("2026"));
console.log(/^\d{4}$/.test("20260"));

// LENGTH RANGE

console.log(/^\w{3,8}$/.test("alice"));
console.log(/^\w{3,8}$/.test("al"));
console.log(/^\w{3,8}$/.test("alexander1"));

// OPTIONAL CHARACTER (?)

console.log(/^colou?r$/.test("color"));
console.log(/^colou?r$/.test("colour"));

// ONE OR MORE (+)

console.log(/^a+$/.test("aaa"));
console.log(/^a+$/.test(""));

// ZERO OR MORE (*)

console.log(/^a*$/.test("aaa"));
console.log(/^a*$/.test(""));

// OR PATTERN (|)

console.log(/^(cat|dog|bird)$/.test("cat"));
console.log(/^(cat|dog|bird)$/.test("fish"));

// CHARACTER NEGATION ([^...])

console.log(/^[^0-9]+$/.test("hello"));
console.log(/^[^0-9]+$/.test("hello1"));

// STARTS WITH (^)

console.log(/^Mr/.test("Mr. Smith"));
console.log(/^Mr/.test("Dr. Smith"));

// ENDS WITH ($)

console.log(/\.com$/.test("site.com"));
console.log(/\.com$/.test("site.org"));

// EMAIL

const emailPattern = /^[\w.-]+@[\w.-]+\.\w+$/;
console.log(emailPattern.test("alice@example.com"));
console.log(emailPattern.test("alice@@example.com"));
console.log(emailPattern.test("alice.com"));

// PHONE WITH OPTIONAL COUNTRY CODE

const phonePattern = /^(\+91)?\d{10}$/;
console.log(phonePattern.test("9876543210"));
console.log(phonePattern.test("+919876543210"));

// URL

console.log(/^https?:\/\//.test("https://example.com"));
console.log(/^https?:\/\//.test("http://example.com"));
console.log(/^https?:\/\//.test("ftp://example.com"));

// GROUPS - EXTRACT PARTS

const m1 = "alice@example.com".match(/^(\w+)@(\w+)\.(\w+)$/);
console.log(m1[0]);          // alice@example.com (full match)
console.log(m1[1]);          // alice
console.log(m1[2]);          // example
console.log(m1[3]);          // com
console.log(m1.slice(1));    // ["alice", "example", "com"]

// NAMED GROUPS

const m2 = "alice@example.com".match(/^(?<user>\w+)@(?<domain>[\w.]+)$/);
console.log(m2.groups.user);   // alice
console.log(m2.groups.domain); // example.com
console.log(m2.groups);        // { user: "alice", domain: "example.com" }