from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=35)
    age = models.PositiveSmallIntegerField()
    profession = models.CharField(max_length=40, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'
