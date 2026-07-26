with open("sample.txt","w") as newfile:
    newfile.write("this is a sample text file\n")
    newfile.write("hello my name is Bhupal T\n")
    newfile.write("student at saveetha school of engineering!\n")
    newfile.write("---------------------------------------------")

# when there is no file called sample.txt python creates new file with mentioned name.

# with open open the file in selected mode (read,write,append) and closes the file after automatically

with open("sample.txt","r") as file:
    data=file.read()
    print(data)

#after writting the data we used read mode that prints the data which is in sample.txt

with open("sample.txt","w") as newfile:
    newfile.write("hello,how are you?\n")
    
#if we use the write mode for file the data in file is overwritten 
#like completely delete the data in file and replaces with new data

with open("sample.txt","r") as file:
    data=file.read()
    print(data)

# append "a" is the mode that write the new line in the file at last of the file

with open("sample.txt","a") as file:
    file.write("this is the new line from append mode")

# when we open the file in "a" append mode we need to write the data using write key word.

with open("sample.txt","r") as file:
    data = file.read()
    print(data)