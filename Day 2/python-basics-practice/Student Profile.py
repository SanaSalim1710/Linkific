student = {
    "Student ID": 12345678,
    "Name": "Olivia Rodrigo",
    "Status": "Enrolled",
    "Courses": ["Film Studies", "Sociology"]
}
# change existing value
student["Status"] = "Intermission"
# add new key-value pair
student["GPA"] = 3.7

# check gpa and create honours key 
if student["GPA"] >= 3.7:
    student["Honours"] = True
else: 
    student["Honours"] = False
print("Student Profile\n")
for key,val in student.items():
    # only print honours key for honours students
    if key == "Honours":
        if val == True:
            print("Honours student")
    else:
        print(f"{key}: {val}")

