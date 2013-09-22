from django.db import models

'''
Created on Sep 22, 2013

@author: brain
'''

class StateSet(models.Model):
    name = models.CharField(max_length=100, default='DefaultStateSet')
    description = models.TextField()
    states_wrap = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

