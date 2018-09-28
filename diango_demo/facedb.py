# -*- coding: utf-8 -*-
from django.http import HttpResponse
from baidu_face_search.models import baidu_face_search
import uuid

def get_uuid():
    book_id = uuid.uuid1()
    now_str = str(book_id).replace('-', '')
    return now_str

def save(request):
    lession_id = '65db4c1d77e84ffaadb66ba4dc87d1cf'
    stu_no = '20140072'
    score = 78
    user_id = '20140049'
    error_code = '0'
    error_msg = 'SUCCESS'
    item = baidu_face_search(lession_id=lession_id, stu_no=stu_no, score=score, user_id=user_id, error_code=error_code, error_msg=error_msg)
    item.save()
    return HttpResponse("<p>数据添加成功！</p>")


def nice_save(lession_id, stu_no, score, user_id, error_code, error_msg):

    item = baidu_face_search(lession_id=lession_id, stu_no=stu_no, score=score, user_id=user_id, error_code=error_code,
                             error_msg=error_msg)
    item.save()
    return HttpResponse("<p>数据添加成功！nice</p>")

def list(request):

    authors = ''
    records = baidu_face_search.objects.all()
    for item in records:
        authors += item.author + ","
    return HttpResponse("<p>" + authors + "</p>")


