

students = []

while True:
    Ask = input("Do you Want to Add Student:").lower()
    try:
        if Ask == "Yes".lower():
            student_name = input("Enter Student Name:")
            student_id = int(input("Enter Student ID:"))


            def get_students_titlecase():
                students_titlecase = []
                for student in students:
                    students_titlecase = student["name"].title()
                return students_titlecase


            def print_students_titlecase():
                students_titlecase = get_students_titlecase()
                print(students_titlecase)


            def add_student(name, student_id):
                student = {"name": name, "student_id": student_id}
                students.append(student)

            Ask = input("Do you Want to Add Student:").lower()
            if Ask == "Yes".lower():
                student_list = get_students_titlecase()
                add_student(student_name, student_id)
                print_students_titlecase()
                print(students)
            else:
                continue
        else:
            print("Type Yes if you To Enter The Student Cred".center(50))
    except Exception:
        print("Write Valid Values")
