from django.db import models

# Create your models here.
class student(models.Model):
    studentname= models.CharField(max_length=100)
    studentAge= models.IntegerField()
    studentCity= models.CharField(max_length=40)
    studentEmail= models.EmailField(null=True)
    
    class Meta:
      db_table = "student"


