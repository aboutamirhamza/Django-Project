from django.db import models

# Create your models here.
class Work(models.Model):
    company = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.company

class UserProfile(models.Model):
    name = models.CharField(max_length = 250)
    age = models.IntegerField()
    contact = models.CharField(max_length = 250)
    company = models.ForeignKey(Work, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name