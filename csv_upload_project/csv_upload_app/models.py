from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    address = models.TextField()
    department = models.CharField(max_length=40)

    def __str__(self):
        return f"{ self.employee_id=} - {self.name=}"