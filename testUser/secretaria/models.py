from django.db import models
from django.contrib.auth.models import Group, User


class Club(models.Model):
    name                = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.name}'
    
class CarnetSocio(models.Model):

    name  = models.CharField(max_length=60)
    club  = models.ForeignKey(Club,on_delete=models.CASCADE)
    user  = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(Group,on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'