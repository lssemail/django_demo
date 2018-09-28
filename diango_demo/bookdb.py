# -*- coding: utf-8 -*-
from django.http import HttpResponse
from Book.models import Book
from . import datadb

def bookdb(request):

    book1 = Book(id='12345678', author='java', price=123, stock=234, sales=10)
    book1.save()
    return HttpResponse("<p>数据添加成功！</p>")

def book_list(request):

    authors = ''
    records = Book.objects.all()
    for item in records:
        authors += item.author + ","
    return HttpResponse("<p>" + authors + "</p>")


def book_one(request):
    lessonid = '112313131'
    stuno = '43424'
    result = datadb.update(lessonid, stuno)
    return HttpResponse(result)


