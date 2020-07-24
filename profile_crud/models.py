from django.db import models
from accounts.models import CustomUser



# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number=models.IntegerField()
    profile_image=models.ImageField(null=True,blank=True)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
