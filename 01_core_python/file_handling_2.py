path = r"c:\Users\thand\OneDrive\projects\python for DE\01_core_python\students.csv"

# r stands for raw uses to tell Python to treat the string exactly as it is written and ignore the backslashes.

with open(path,"r") as students:
    student_data = students.read()
    print(student_data)



with open(path,"a") as students:
    students.write("\nZane,Computer Science,A") # adds the student at very last line

with open(path,"r") as student_101:
    student_data=student_101.read()
    print(student_data)
