from django.db import models
from django.contrib.auth.models import User
from DjangoBase.base_abstracts.models import BaseModel, BaseTrackingModel
from users.utils import UserTypes
from companies.models import Company

# Create your models here.
class UserExtension(BaseModel, BaseTrackingModel):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    user_first_name = models.CharField(max_length=255)
    user_last_name = models.CharField(max_length=255)
    user_type = models.CharField(default='Employee', max_length=255, choices=[(tag.value, tag.name) for tag in UserTypes.all()])
    user_address = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_zip_code = models.CharField(max_length=255)
    user_phone_number = models.CharField(max_length=255, blank=True, null=True)
    user_emial = models.CharField(max_length=255, blank=True, null=True)
    foreign_id = models.CharField(max_length=255, blank=True, null=True)
    sick_time_max = models.DecimalField(max_digits=5, decimal_places=2, default=48)
    sick_time_used = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sick_time_current = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sick_time_accural_rate = models.DecimalField(max_digits=5, decimal_places=2, default=2)
    hire_date = models.DateField()
    is_terminated = models.BooleanField(default=False)
    termination_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'User Extension'
        verbose_name_plural = 'User Extensions'