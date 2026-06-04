students = ["Adela", "Jade", "Perrie", "Leigh-Anne"]

present_count = 0
absent_count = 0

for student in students:
    present = input(f"Is {student} present? (y/n): ")

    if present.lower() == "y":
        present_count += 1
absent_count = len(students) - present_count
print("No. of Students Present: ", present_count)
print("No. of Students Absent: ", absent_count)

