"""
from the students.csv find the students with "A" grade,
create the new list file called top_students_list
"""

path = r'C:\Users\thand\OneDrive\projects\python for DE\01_core_python\students.csv'
students_list=[]
top_students_list=[]

with open(path,"r") as students:
    for student in students:
        students_list.append(student.strip().split(","))

for student in students_list:
    if student[2]=="A":
        top_students_list.append(student)

for student in students_list:
    print(student)

print()

for top_student in top_students_list:
    print(top_student)