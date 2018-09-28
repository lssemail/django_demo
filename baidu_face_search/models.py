from django.db import models
from diango_demo.tools import UUIDTools

# Create your models here.


class baidu_face_search(models.Model):

    id = models.UUIDField(primary_key=True, default=UUIDTools.uuid1_hex, editable=False)
    lession_id = models.CharField(max_length=100)
    stu_no = models.CharField(max_length=32)
    face_token = models.CharField(max_length=100)
    score = models.FloatField()
    user_id = models.CharField(max_length=32)
    error_code = models.CharField(max_length=32)
    error_msg = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "baidu_face_search"
