from App.models.student import Student
from App.models.staff import Staff

# Sample Staff
staff_members = [
    Staff(id=1, name="Mr. John Doe"),
    Staff(id=2, name="Ms. Jane Smith"),
]

# Sample Students
students = [
    Student(id=101, name="Alice Johnson", total_hours=12),
    Student(id=102, name="Brian Lee", total_hours=8),
    Student(id=103, name="Carla Singh", total_hours=2),
    Student(id=104, name="David Brown", total_hours=5),
    Student(id=105, name="Emma Davis", total_hours=0),
]

# Dictionaries to simulate database
student_db = {student.id: student for student in students}
staff_db = {staff.id: staff for staff in staff_members}
