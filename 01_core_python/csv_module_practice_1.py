import csv

path = r'C:\Users\thand\OneDrive\projects\python for DE\01_core_python\students.csv'
students_list = []
top_students = []

with open(path,"r") as students:
    student_data = csv.reader(students)
    for student in student_data:
        students_list.append(student)

'''
the module csv automatically reads the data in csv file
no need to so extra operations like strip(),split(",")
'''

for i in students_list:
    print(i)

top_students=[student for student in students_list if student[2]=="A"]

print()

for i in top_students:
    print(i)



