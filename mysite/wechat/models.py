from django.db import models

class Record(models.Model):
    user = models.CharField(max_length=30)
    step = models.IntegerField()
    time = models.DateTimeField(auto_now_add = True)
