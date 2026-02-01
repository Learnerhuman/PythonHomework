# 1. Round float to 2 decimals
x = float(input("Enter a float: "))
print(round(x, 2))
# 2. Largest and smallest of three numbers
a = float(input("Enter first: "))
b = float(input("Enter second: "))
c = float(input("Enter third: "))
print("Largest:", max(a, b, c))
print("Smallest:", min(a, b, c))
# 3. Km to meters and centimeters
km = float(input("Enter km: "))
print("Meters:", km * 1000)
print("Centimeters:", km * 100000)
# 4. Integer division and remainder
a = int(input("Enter first: "))
b = int(input("Enter second: "))
print("Division:", a // b)
print("Remainder:", a % b)
# 5. Celsius to Fahrenheit
c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)
# 6. Last digit
n = int(input("Enter number: "))
print("Last digit:", abs(n) % 10)
# 7. Even or odd
n = int(input("Enter number: "))
print(n % 2 == 0)
# 1. Age from birth year
name = input("Name: ")
year = int(input("Birth year: "))
print(name, "is", 2026 - year, "years old")
# 2. Extract car names
txt = "LMaasleitbtui"
print(txt[1::2])  # Maserati
# 3. Length, upper, lower
s = input("Enter string: ")
print(len(s))
print(s.upper())
print(s.lower())
# 4. Palindrome
s = input("Enter string: ")
print(s == s[::-1])
# 5. Vowels and consonants
s = input("Enter string: ").lower()
vowels = "aeiou"
v = sum(1 for i in s if i in vowels)
c = sum(1 for i in s if i.isalpha() and i not in vowels)
print("Vowels:", v, "Consonants:", c)
# 6. Contains another string
a = input("Main string: ")
b = input("Check: ")
print(b in a)
# 7. Replace word
s = input("Sentence: ")
old = input("Replace: ")
new = input("With: ")
print(s.replace(old, new))
# 8. First and last char
s = input("String: ")
print(s[0], s[-1])
# 9. Reverse
s = input("String: ")
print(s[::-1])
# 10. Word count
s = input("Sentence: ")
print(len(s.split()))
# 11. Contains digit
s = input("String: ")
print(any(char.isdigit() for char in s))
# 12. Join list
words = ["Python", "is", "fun"]
print("-".join(words))
# 13. Remove spaces
s = input("String: ")
print(s.replace(" ", ""))
# 14. Compare strings
a = input("First: ")
b = input("Second: ")
print(a == b)
# 15. Acronym
s = input("Sentence: ")
print("".join(word[0].upper() for word in s.split()))
# 16. Remove character
s = input("String: ")
ch = input("Character: ")
print(s.replace(ch, ""))
# 17. Replace vowels with *
s = input("String: ")
vowels = "aeiouAEIOU"
for v in vowels:
    s = s.replace(v, "*")
print(s)
# 18. Starts and ends
s = input("Sentence: ")
start = input("Starts with: ")
end = input("Ends with: ")
print(s.startswith(start) and s.endswith(end))
# 1. Username & password not empty
u = input("Username: ")
p = input("Password: ")
print(bool(u) and bool(p))
# 2. Numbers equal
a = int(input())
b = int(input())
print(a == b)
# 3. Positive and even
n = int(input())
print(n > 0 and n % 2 == 0)
# 4. All different
a, b, c = map(int, input().split())
print(a != b and b != c and a != c)
# 5. Same length
a = input()
b = input()
print(len(a) == len(b))
# 6. Divisible by 3 and 5
n = int(input())
print(n % 3 == 0 and n % 5 == 0)
# 7. Sum > 50
a = int(input())
b = int(input())
print(a + b > 50)
# 8. Between 10 and 20
n = int(input())
print(10 <= n <= 20)
