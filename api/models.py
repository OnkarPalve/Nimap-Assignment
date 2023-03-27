from django.db import models

# Create your models here.

#Client Model
class Client(models.Model):
    client_name=models.CharField(max_length=20)
    created_at= models.DateTimeField()
    created_by=models.CharField(max_length=20)

    def __str__(self):
        return self.client_name
    
    
    
#Project Model
class Project(models.Model):
    project_name=models.CharField(max_length=100)
    created_at=models.DateTimeField
    created_by=models.CharField(max_length=20)

    client=models.ForeignKey(Client, on_delete=models.CASCADE)
