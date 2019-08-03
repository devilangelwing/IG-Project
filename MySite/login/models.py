from django.db import models




# Create your models here.
class Test(models.Model):
    test_field = models.CharField(max_length=255)
    test_field1 = models.CharField(max_length=255)
