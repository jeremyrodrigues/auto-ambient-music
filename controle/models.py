from django.db import models
from controle.choices import *

# Create your models here.
class Music (models.Model):
    url = models.URLField(unique=True)
    description = models.CharField(max_length=256)
    def __str__(self):
        return self.description

class Time (models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS, default=0)
    initial_time = models.TimeField()
    final_time = models.TimeField()
    music = models.ForeignKey('Music', related_name='times', on_delete=models.CASCADE)
    vol = models.IntegerField(choices=VOLUMES, default=3)
    def __str__(self):
        return f'{WEEKDAYS[self.weekday][1]} ({self.initial_time} - {self.final_time}) - {self.music} Vol = {self.vol}'