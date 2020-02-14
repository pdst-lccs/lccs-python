# Solution to question
# Version 3. A dictionary to store results for multiple students
results = {}

subject = input("Enter subject name: ")
results['subject'] = subject
name = input ("Enter student name: ")
while name != "":
    mark = input ("Enter percentage mark for "+name+": ")
    results[name] = mark
    name = input ("Enter student name: ")

print(results)
