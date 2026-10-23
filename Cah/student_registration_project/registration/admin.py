from django.contrib import admin  # type: ignore[import-not-found]
from .models import Student

admin.site.register(Student)