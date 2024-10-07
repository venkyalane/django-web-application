from faker import Faker
import random
from students.models import StudentID, Student, Department, Subject, SubjectMarks


fake = Faker()

def seed_db(n):
    try:
        for _ in range(n):
            departments_obj = Department.objects.all()
            random_index = random.randint(0, len(departments_obj)-1)
            department = departments_obj[random_index]
            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)
            Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address)

    except Exception as e:
        print(e)

def create_subjects_marks(n):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            sub_obj = Subject.objects.all()
            for subject in sub_obj:
                SubjectMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(0,100))
    except Exception as e:
        print(e)






