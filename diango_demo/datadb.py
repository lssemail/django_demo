# -*- coding: utf-8 -*-
from django.http import HttpResponse
from tqts_data.models import tqts_data


def update(lesson_id, stu_no):

    result = False
    records = tqts_data.objects.filter(lessonid=lesson_id, stuno=stu_no).order_by('-sim')[0:1]
    if len(records):
        record = records[0]
        record.sim = 0.987654321
        record.status_present = 1
        record.save()
        result = True
    return HttpResponse(result)
