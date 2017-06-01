from django.contrib import admin
from .models import Teacher, Class, Student, Parent, Post


class StudentInline(admin.TabularInline):
    model = Student


class ClassAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]

admin.site.register(Teacher)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Post)
