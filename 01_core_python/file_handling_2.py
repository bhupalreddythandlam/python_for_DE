path = r"c:\Users\thand\OneDrive\projects\python for DE\01_core_python\students.csv"

# r stands for raw uses to tell Python to treat the string exactly as it is written and ignore the backslashes.

with open(path,"r") as students:
    student_data = students.read()
    print(student_data)



# with open(path,"a") as students:
#     students.write("\nZane,Computer Science,A") 
# adds the student at very last line
# if run every time every time the student will be added thats why commented!

with open(path,"r") as student_101:
    student_data=student_101.read()
    print(student_data)

print()

student_record=[]
with open(path,"r") as students:
    for student in students:
       student_record.append(student.strip().split(",")) # this splits the every row in to 2d list and stores in student_record

print()

print(student_record[0]) # takes the first record in list

print()
for student in student_record:
     print(student[0]) # prints the every student names in the list;

