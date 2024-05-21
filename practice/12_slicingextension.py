#WAP to extract the file name and extension from the given filepath using string slicing
file=input("Enter the name of file: ")
filearray=file.split(".")
print("The name of file is: ",filearray[0])
print("The Extension of file is:",filearray[1])


print("#####Alternative way#####")
for index in  range(len(file)):
    if file[index]==".":
        end=index
print("the name of file without extension is:",file[0:end])
print("the extension of file is:",file[end+1:])   
