import csv

new_employees = [
    ['Name', 'Department', 'Role'],
    ['Alice', 'Engineering', 'Developer'],
    ['Bob', 'Sales', 'Manager'],
    ['Charlie', 'Marketing', 'Designer']
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_employees)

'''
this creates the employees.csv file the data is taken from new_employees list.
'''
