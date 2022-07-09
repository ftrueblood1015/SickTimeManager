from tabnanny import verbose
from django.db import models
from DjangoBase.base_abstracts.models import BaseModel, BaseTrackingModel
# Create your models here.

class Company(BaseModel, BaseTrackingModel):
    company_name = models.CharField(max_length=255)
    comapny_address = models.CharField(max_length=255)
    comapny_city = models.CharField(max_length=255)
    company_state = models.CharField(max_length=255)
    company_zip_code = models.CharField(max_length=255)
    company_phone_number = models.CharField(max_length=255)
    company_emial = models.CharField(max_length=255, blank=True, null=True)
    company_fax = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name ='Company'
        verbose_name_plural = 'Companies'


class Franchise(BaseModel, BaseTrackingModel):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    franchise_name = models.CharField(max_length=255)
    franchise_number = models.CharField(max_length=255)
    franchise_address = models.CharField(max_length=255)
    franchise_city = models.CharField(max_length=255)
    franchise_state = models.CharField(max_length=255)
    franchise_zip_code = models.CharField(max_length=255)
    franchise_phone_number = models.CharField(max_length=255)
    franchise_emial = models.CharField(max_length=255, blank=True, null=True)
    franchise_fax = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name ='Franchise'
        verbose_name_plural = 'Franchises'


class Franchise_Entity(BaseModel, BaseTrackingModel):
    franchise = models.ForeignKey(Franchise, on_delete=models.DO_NOTHING)
    entity_number = models.IntegerField()
    entity_address = models.CharField(max_length=255)
    entity_city = models.CharField(max_length=255)
    entity_state = models.CharField(max_length=255)
    entity_zip_code = models.CharField(max_length=255)
    fentity_phone_number = models.CharField(max_length=255)
    entity_emial = models.CharField(max_length=255, blank=True, null=True)
    entity_fax = models.CharField(max_length=255, blank=True, null=True)
    employees = models.ManyToManyField('users.UserExtension', blank=True)

    class Meta:
        verbose_name ='Franchise Entity'
        verbose_name_plural = 'Franchise Entities'