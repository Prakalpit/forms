from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=23)
    email=models.EmailField()
    bio=models.TextField()


    def __str__(self):
        return self.name
