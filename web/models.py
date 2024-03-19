from django.db import models

class Job_Category(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length = 50)
    address_company = models.CharField(max_length = 130)



    def __str__(self):
        return self.name




class Job(models.Model):
    name = models.CharField(max_length = 50)
    phone_number = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(Job_Category, on_delete = models.CASCADE)
    company = models.ForeignKey(Company,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    