#task 1
import math

class Vector:
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("Vector must have at least one component")
        self.components = tuple(components)

    def __str__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

    # Addition
    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    # Subtraction
    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    # Dot product OR scalar multiplication
    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Unsupported operand")

    # Scalar * Vector
    def __rmul__(self, scalar):
        return self * scalar

    # Magnitude
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    # Normalize
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*[round(a / mag, 3) for a in self.components])
#task 2
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_file(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"
class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        open(self.FILE_NAME, "a").close()

    def _read_all(self):
        with open(self.FILE_NAME, "r") as f:
            return f.readlines()

    def _write_all(self, lines):
        with open(self.FILE_NAME, "w") as f:
            f.writelines(lines)

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")

        # Unique ID check
        for line in self._read_all():
            if line.startswith(emp_id + ","):
                print("Employee ID already exists!")
                return

        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        emp = Employee(emp_id, name, position, salary)
        with open(self.FILE_NAME, "a") as f:
            f.write(emp.to_file())

        print("Employee added successfully!")

    def view_all(self):
        print("\nEmployee Records:")
        for line in self._read_all():
            print(line.strip())

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        for line in self._read_all():
            if line.startswith(emp_id + ","):
                print("Employee Found:")
                print(line.strip())
                return
        print("Employee not found")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        lines = self._read_all()
        updated = False

        for i, line in enumerate(lines):
            if line.startswith(emp_id + ","):
                name = input("New Name: ")
                position = input("New Position: ")
                salary = input("New Salary: ")
                lines[i] = f"{emp_id},{name},{position},{salary}\n"
                updated = True

        if updated:
            self._write_all(lines)
            print("Employee updated successfully!")
        else:
            print("Employee not found")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        lines = self._read_all()
        new_lines = [l for l in lines if not l.startswith(emp_id + ",")]

        if len(lines) == len(new_lines):
            print("Employee not found")
        else:
            self._write_all(new_lines)
            print("Employee deleted successfully!")

    def menu(self):
        while True:
            print("""
1. Add new employee
2. View all employees
3. Search employee
4. Update employee
5. Delete employee
6. Exit
""")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")
#task3
class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return self.__dict__
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, tasks): pass

    @abstractmethod
    def load(self): pass
import json

class JSONStorage(Storage):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Task(**item) for item in data]
        except FileNotFoundError:
            return []
class ToDoApp:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self):
        task = Task(
            input("Task ID: "),
            input("Title: "),
            input("Description: "),
            input("Due Date: "),
            input("Status: ")
        )
        self.tasks.append(task)
        print("Task added!")

    def view_tasks(self):
        for t in self.tasks:
            print(t.task_id, t.title, t.status)

    def filter_tasks(self):
        status = input("Enter status to filter: ")
        for t in self.tasks:
            if t.status.lower() == status.lower():
                print(t.task_id, t.title)

    def save(self):
        self.storage.save(self.tasks)
        print("Tasks saved!")

    def menu(self):
        while True:
            print("""
1. Add Task
2. View Tasks
3. Filter Tasks
4. Save
5. Exit
""")
            choice = input("Choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.filter_tasks()
            elif choice == "4":
                self.save()
            elif choice == "5":
                break
