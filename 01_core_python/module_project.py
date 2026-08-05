import csv

path = r'C:\Users\thand\OneDrive\projects\python for DE\01_core_python\students.csv'

all_students=[]
top_students=[]

with open(path,'r') as file:
    students=csv.reader(file)
    for student in students:
        all_students.append(student)
        if student[2]=="A":
            top_students.append(student)

print(all_students)
print()
print(top_students)

with open("top_students.csv",'w',newline="") as file:
    writer=csv.writer(file)
    writer.writerows(top_students)