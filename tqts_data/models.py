from django.db import models
import uuid
# Create your models here.


class tqts_data(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    check_num = models.IntegerField()
    stuno = models.CharField(max_length=32)
    pitch = models.FloatField(blank=True, null=True)
    yaw = models.FloatField(blank=True, null=True)
    roll = models.FloatField(blank=True, null=True)
    sim = models.FloatField(blank=True, null=True)
    status = models.IntegerField()
    status_present = models.CharField(max_length=32, blank=True, null=True)
    lessonid = models.CharField(max_length=32)
    deviceid = models.CharField(max_length=32)
    kpoint = models.CharField(max_length=666, blank=True, null=True)
    box = models.CharField(max_length=666, blank=True, null=True)
    gdate = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'tqts_data'
        unique_together = (('check_num', 'stuno', 'deviceid'),)