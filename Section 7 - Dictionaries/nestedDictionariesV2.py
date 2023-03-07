#LCCS Computer Science
#Nov 2022
#Nested Dictionaries

#Building a nested dictionary

class_list = []            #Empty list
class_dict = { }           #Empty Dictionary

numberOfStudents = int(input("How many students' names do you want to add? \n"))
noOfResults = int(input("How many results do you want to add per students? \n"))

for i in range(numberOfStudents):
    name = input("Enter student name \n")
    class_dict[name]={ }   #creating a key in the dictionary using the name - the value is another dictionary
    
    #next populate the nested dictionary associated with each name:
    for r in range(noOfResults):
        subject = input("Enter subject:")
        result = input("Enter result:")
        class_dict[name][subject]=result
    
    print(class_dict)
    print("---------------")
print(class_dict)
