import os 
myfile = open("file1.txt", "w")
myfile.write("we just created our second file using code")
myfile.close()

myfile = open("file1.txt", "r")
print(myfile.read())
myfile.close()

os.remove("file1.txt")
