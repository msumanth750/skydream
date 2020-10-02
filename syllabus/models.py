from django.db import models

# Create your models here.
class SubjectModel(models.Model):
    name = models.CharField(max_length=20,primary_key=True,verbose_name='Subject Name')
    code = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    units = models.IntegerField()
