from django.db import models

# Create your models here.
class student(models.Model):
    studentname= models.CharField(max_length=100)
    studentAge= models.IntegerField()
    studentCity= models.CharField(max_length=40)
    studentEmail= models.EmailField(null=True)
    
class Meta:
    db_table = "student"

def __str__(self):
    return self.studentname


class product(models.Model):
    Productname = models. CharField(max_length=100)
    Productprice = models. IntegerField()
    ProductDscription = models.TextField()
    Productstock = models.PositiveIntegerField()
    Productcolor = models.CharField(max_length=20,null=True)
    Productstatus = models.BooleanField(default=True)
   
class Meta:
    db_table ="product"
     
def __str__(self):
    return self.productname
      
class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
class Meta:
    db_table = "studentprofile"

def _str_(self):
    return self.studentId.studentName
      

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
class Meta:
    db_table = "category"

def _str_(self):
    return self.categoryName   
    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
class Meta:
    db_table = "service"

   



class accountholder(models.Model):
    holderNname=models.CharField(max_length=50)
    holderAge=models.IntegerField()
    holderpassword=models.IntegerField()
    holdercity=models.CharField(max_length=50)
    holdergender=models.CharField(max_length=50)


    class Meta:
        db_table ="accountholder"



class bank(models.Model):
    bankBranch=models.CharField(max_length=50)
    accounttype=models.CharField(max_length=50)
    password=models.IntegerField()
    accountNumber=models.IntegerField() 
    signcher=models.CharField(max_length=50)
    accountholderID=models.ForeignKey(accountholder,on_delete=models.CASCADE)
   
    class Meta:
        db_table ="bank"



class 