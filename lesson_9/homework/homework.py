# ---------- Custom Exceptions ----------
class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


# ---------- Classes ----------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"


class Member:
    MAX_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < Member.MAX_BOOKS


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException("Book not found in the library")

    def borrow_book(self, member, title):
        book = self.find_book(title)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed")

        if not member.can_borrow():
            raise MemberLimitExceededException("Member has reached borrowing limit")

        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed '{book.title}'")

    def return_book(self, member, title):
        for book in member.borrowed_books:
            if book.title == title:
                book.is_borrowed = False
                member.borrowed_books.remove(book)
                print(f"{member.name} returned '{book.title}'")
                return
        raise BookNotFoundException("This book was not borrowed by the member")


# ---------- Testing ----------
library = Library()

book1 = Book("1984", "George Orwell")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Python Basics", "John Doe")
book4 = Book("Data Science", "Jane Smith")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

member1 = Member("Alice")
library.add_member(member1)

try:
    library.borrow_book(member1, "1984")
    library.borrow_book(member1, "The Hobbit")
    library.borrow_book(member1, "Python Basics")
    library.borrow_book(member1, "Data Science")  # Should raise exception
except Exception as e:
    print("Error:", e)

library.return_book(member1, "1984")
####task2
aa= """grades.csv
Name,Subject,Grade
Alice,Math,85
Bob,Science,78
Carol,Math,92
Dave,History,74"""

import csv

grades = []

# Read CSV
with open("grades.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = float(row["Grade"])
        grades.append(row)

# Calculate averages
subject_totals = {}
subject_counts = {}

for row in grades:
    subject = row["Subject"]
    grade = row["Grade"]

    subject_totals[subject] = subject_totals.get(subject, 0) + grade
    subject_counts[subject] = subject_counts.get(subject, 0) + 1

averages = {
    subject: subject_totals[subject] / subject_counts[subject]
    for subject in subject_totals
}

# Write average_grades.csv
with open("average_grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in averages.items():
        writer.writerow([subject, avg])

print("Average grades saved to average_grades.csv")
sa="""[
    {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
]
"""
import json
import csv

# Load tasks
with open("tasks.json", "r") as file:
    tasks = json.load(file)

# Display tasks
print("Tasks:")
for task in tasks:
    print(
        f"ID: {task['id']}, "
        f"Task: {task['task']}, "
        f"Completed: {task['completed']}, "
        f"Priority: {task['priority']}"
    )

# Example modification
tasks[0]["completed"] = True

# Save changes
with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)
def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    avg_priority = sum(t["priority"] for t in tasks) / total

    return total, completed, pending, avg_priority


total, completed, pending, avg_priority = calculate_stats(tasks)

print("\nTask Statistics:")
print("Total tasks:", total)
print("Completed tasks:", completed)
print("Pending tasks:", pending)
print("Average priority:", avg_priority)


#
with open("tasks.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Task", "Completed", "Priority"])

    for task in tasks:
        writer.writerow([
            task["id"],
            task["task"],
            task["completed"],
            task["priority"]
        ])

print("Tasks exported to tasks.csv")
