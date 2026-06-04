marks = [["Class A", 85, 92, 78],["Class B", 89, 95, 91],["Class C", 70, 64, 82]]

for classroom in marks:
    room_name = classroom[0]
    total_marks = 0
    no_of_students = 0
    
    print(f"\n{room_name} marks:")
    student_id = 1
    for item in classroom[1:]:
        total_marks += item
        no_of_students += 1
        print(f" Student {student_id} Marks: {item}")
        student_id += 1
        
    class_average = total_marks / no_of_students
    print(f"Average: {class_average:.1f}%")