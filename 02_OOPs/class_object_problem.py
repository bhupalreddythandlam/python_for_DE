class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

class Department:
    def __init__(self, dept_name, manager):
        self.dept_name = dept_name
        self.manager = manager

manager1 = Employee("Alice", "E123")
dept1 = Department("IT", manager1)

# what exact line of code would you write to print() the id_number of dept1's manager?

print(dept1.manager.id_number)