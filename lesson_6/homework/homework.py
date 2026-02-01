#task1
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper


@check
def div(a, b):
    return a / b


print(div(6, 2))  # 3.0
print(div(6, 0))  # Denominator can't be zero

#task2
FILENAME = "employees.txt"


def add_employee():
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    position = input("Position: ")
    salary = input("Salary: ")

    with open(FILENAME, "a") as f:
        f.write(f"{emp_id}, {name}, {position}, {salary}\n")


def view_all():
    with open(FILENAME, "r") as f:
        print(f.read())


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            if line.startswith(emp_id + ","):
                print("Found:", line)
                found = True

    if not found:
        print("Employee not found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_lines = []
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            if line.startswith(emp_id + ","):
                name = input("New Name: ")
                position = input("New Position: ")
                salary = input("New Salary: ")
                updated_lines.append(f"{emp_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                updated_lines.append(line)

    with open(FILENAME, "w") as f:
        f.writelines(updated_lines)

    if found:
        print("Record updated.")
    else:
        print("Employee not found.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    new_lines = []
    found = False

    with open(FILENAME, "r") as f:
        for line in f:
            if not line.startswith(emp_id + ","):
                new_lines.append(line)
            else:
                found = True

    with open(FILENAME, "w") as f:
        f.writelines(new_lines)

    if found:
        print("Record deleted.")
    else:
        print("Employee not found.")


while True:
    print("\n1. Add")
    print("2. View All")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        break
    else:
        print("Invalid choice!")
#task3
import os
import string
from collections import Counter


if not os.path.exists("sample.txt"):
    text = input("Enter a paragraph to create sample.txt:\n")
    with open("sample.txt", "w") as f:
        f.write(text)

with open("sample.txt", "r") as f:
    text = f.read().lower()

# Remove punctuation
for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()
total_words = len(words)

counter = Counter(words)

top_n = int(input("How many top words to display? "))
top_words = counter.most_common(top_n)

print("\nTotal words:", total_words)
print(f"Top {top_n} most common words:")

for word, count in top_words:
    print(f"{word} - {count} times")

# Save to file
with open("word_count_report.txt", "w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {total_words}\n")
    f.write(f"Top {top_n} Words:\n")
    for word, count in top_words:
        f.write(f"{word} - {count}\n")
