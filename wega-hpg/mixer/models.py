import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


# Create your models here.
class Mixer(models.Model):
    def __str__(self):
        return self.name
    
    mixer_fileds=[
        'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8',
        
    ]
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    name   = models.CharField(max_length=1024)
    token  = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.JSONField(null=True, blank=True)
    p1 = models.CharField(max_length=1024, default="CaNO3")
    p2 = models.CharField(max_length=1024, default="KNO3")
    p3 = models.CharField(max_length=1024, default="NH4NO3")
    p4 = models.CharField(max_length=1024, default="MgSO4")
    p5 = models.CharField(max_length=1024, default="KH2PO4")
    p6 = models.CharField(max_length=1024, default="K2SO4")
    p7 = models.CharField(max_length=1024, default="Micro")
    p8 = models.CharField(max_length=1024, default="B"  )
    
    z_p1 = models.FloatField(default=0)
    z_p2 = models.FloatField(default=0)
    z_p3 = models.FloatField(default=0)
    z_p4 = models.FloatField(default=0)
    z_p5 = models.FloatField(default=0)
    z_p6 = models.FloatField(default=0)
    z_p7 = models.FloatField(default=0)
    z_p8 = models.FloatField(default=0)

    z_v1 = models.FloatField(default=0)
    z_v2 = models.FloatField(default=0)
    z_v3 = models.FloatField(default=0)
    z_v4 = models.FloatField(default=0)
    z_v5 = models.FloatField(default=0)
    z_v6 = models.FloatField(default=0)
    z_v7 = models.FloatField(default=0)
    z_v8 = models.FloatField(default=0)
    
    def get_current_v_values(self):
        data_sum = {}
        for i in self.mixer_fileds:
            data_sum[i.replace('p', 'v')] = Sum(i.replace('p', 'v'))
        sum_qs = self.mixerhistory_set.aggregate(**data_sum)
        print('sum_qs', sum_qs)
        sum_data = {}
        for i in self.mixer_fileds:
            v = sum_qs.get(i.replace('p', 'v')) - getattr(self, f"z_{i.replace('p', 'v')}")
            sum_data[i] = f"{round(v, 2)}"
        return  sum_data
    
        
        


class MixerHistory(models.Model):
    mixer = models.ForeignKey(Mixer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    p1 = models.FloatField(default=0)
    p2 = models.FloatField(default=0)
    p3 = models.FloatField(default=0)
    p4 = models.FloatField(default=0)
    p5 = models.FloatField(default=0)
    p6 = models.FloatField(default=0)
    p7 = models.FloatField(default=0)
    p8 = models.FloatField(default=0)

    v1 = models.FloatField(default=0)
    v2 = models.FloatField(default=0)
    v3 = models.FloatField(default=0)
    v4 = models.FloatField(default=0)
    v5 = models.FloatField(default=0)
    v6 = models.FloatField(default=0)
    v7 = models.FloatField(default=0)
    v8 = models.FloatField(default=0)
    
    s = models.IntegerField(null=True, blank=True)
