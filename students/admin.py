from django.contrib import admin
from students.models import StudentID, Student, Department, Subject, SubjectMarks

# Register your models here.

admin.site.register(StudentID)
admin.site.register(Department)
admin.site.register(Subject)


class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "marks"]

admin.site.register(SubjectMarks, SubjectMarksAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ["student_id", "student_name", "student_email", "student_age", "department", "student_address"]
admin.site.register(Student, StudentAdmin)