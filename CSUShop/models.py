from django.db import models

class PreOrders(models.Model):
    name = models.CharField(max_length=50)
    idnum = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    progyear = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ListofOrders(models.Model):
    name = models.CharField(max_length=50)
    idnum = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    progyear = models.CharField(max_length=50)

    def __str__(self):
        return self.name

