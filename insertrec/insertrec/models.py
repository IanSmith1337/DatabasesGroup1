from django.db import models


class insertdata(models.Model):
    stname=models.CharField(max_length=100)
    stemail=models.CharField(max_length=100)
    stmob=models.IntegerField()


class dispdata(models.Model):
    rank=models.IntegerField()
    zipcode=models.CharField(max_length=100)