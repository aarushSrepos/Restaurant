from django.db import models

# Create your models here.

class TableRecord(models.Model):

    clientName = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=1)



class OrderRecord(models.Model):

    tableNumber = models.ForeignKey(TableRecord, on_delete=models.CASCADE)
    dish = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.FloatField()

