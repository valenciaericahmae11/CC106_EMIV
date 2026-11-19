from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'first_name',
        'last_name',
        'gender',
        'date_of_birth',
        'contact_number',
    )
    search_fields = ('student_id', 'first_name', 'last_name')
    list_filter = ('gender',)
