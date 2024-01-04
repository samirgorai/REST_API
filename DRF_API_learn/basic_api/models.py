from django.db import models

# Create your models here.

class employee_model(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    sex=models.CharField(max_length=10)
    emp_id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name
    


