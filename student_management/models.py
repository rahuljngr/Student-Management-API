from django.db import models
import uuid

class Student(models.Model):
    first_name = models.CharField(max_length=100,null = False)
    last_name = models.CharField(max_length=100 , null=True)
    dob = models.DateField()
    grade = models.IntegerField(default=0)
    phone = models.IntegerField()
    email = models.EmailField(max_length=255)

    def __str__(self):
        return "%s %s" %(self.first_name,self.last_name)
    
