from django.db import models

# Create your models here.
class Gender(models.Model):
    description = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.description

class MaritalStatus(models.Model):
    description = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.description

class Designation(models.Model):
    description = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.description

class Department(models.Model):
    description = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.description


class Employee(models.Model):
    empid = models.CharField(max_length=10,unique=True)
    fname = models.CharField(max_length=100,  blank=False)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,)
    #picture = models.ImageField(null=True)

    address = models.CharField(max_length=255, blank=True)
    paddress = models.CharField(max_length=255, blank=True)
    dob = models.DateTimeField(null=False)
    mstatus = models.ForeignKey(MaritalStatus,on_delete=models.CASCADE,)
    post = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,)
    doj = models.DateTimeField(null=True)
    wemail = models.EmailField(max_length=50)
    wphone = models.CharField(max_length=30)


    def __str__(self):
        return self.fname + ' ' + self.lname


class salary(models.Model):

    bp = models.IntegerField()
    da = models.IntegerField()
    ta = models.IntegerField()
    hra = models.IntegerField()
    ma = models.IntegerField()
    pf = models.IntegerField()
    tax = models.IntegerField()
    total = models.IntegerField()
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,)
    # def __str__(self):
    #     return self.designation
