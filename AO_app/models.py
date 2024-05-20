from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class ContactRequest(models.Model):
    type_of_request = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(region='MA')
    email = models.EmailField()
    observations = models.TextField()

    def __str__(self):
        return self.full_name
    
class TableData(models.Model):
    site = models.CharField(max_length=100)
    numero_ao = models.CharField(max_length=100)
    designation = models.TextField()
    date_lancement = models.DateField()
    date_remise = models.DateField()
    date_ouverture = models.DateField()
    estimation_projet_dhht = models.FloatField()
    seance_ouverture = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)

    def __str__(self):
        return self.numero_ao
    
