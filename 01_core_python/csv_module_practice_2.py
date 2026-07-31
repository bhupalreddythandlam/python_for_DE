import csv

path=r'C:\Users\thand\OneDrive\projects\python for DE\01_core_python\students.csv'
top_student_list=[]
average_student_list=[]

with open(path,"r") as student:
    reader=csv.reader(student)
    header=next(reader)
    for row in reader:
        if row[2]=="A":
            top_student_list.append(row)
        else:
            average_student_list.append(row)


print(header)
print("-----Average students data-----")
for row in average_student_list:
    print(row)

print()

print("-----top students data-----")
for row in top_student_list:
    print(row)
