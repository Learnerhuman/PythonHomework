#task 1
def convert_cel_to_far(c):
    return c * 9 / 5 + 32

def convert_far_to_cel(f):
    return (f - 32) * 5 / 9

f = float(input("Enter a temperature in degrees F: "))
c = convert_far_to_cel(f)
print(f"{f} degrees F = {c:.2f} degrees C")

c = float(input("\nEnter a temperature in degrees C: "))
f = convert_cel_to_far(c)
print(f"{c} degrees C = {f:.2f} degrees F")

#task 2
def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

principal = float(input("Enter the initial amount: "))
rate = float(input("Enter the annual rate (e.g. 0.05 for 5%): "))
years = int(input("Enter the number of years: "))

invest(principal, rate, years)

#task 3
n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(f"{i} is a factor of {n}")
#task 4

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    students = []
    tuition = []
    for uni in data:
        students.append(uni[1])
        tuition.append(uni[2])
    return students, tuition

def mean(lst):
    return sum(lst) / len(lst)

def median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]

students, tuition = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuition)

print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")

print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,}\n")

print(f"Tuition mean: $ {mean(tuition):,.2f}")
print(f"Tuition median: $ {median(tuition):,}")
print("*" * 30)

#task 5
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
