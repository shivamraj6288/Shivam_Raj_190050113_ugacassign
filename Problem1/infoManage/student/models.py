from django.db import models

class StudentData(models.Model):
    name=models.CharField(max_length=250)
    roll=models.CharField(max_length=9)
    department=models.CharField(max_length=100)
    hostel=models.CharField(max_length=50)

    def __str__(self):
        return self.roll


