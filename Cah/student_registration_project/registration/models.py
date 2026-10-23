# pyright: reportMissingModuleSource=false
from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    student_id = models.CharField(
        max_length=20,
        unique=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    date_of_birth = models.DateField()
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"