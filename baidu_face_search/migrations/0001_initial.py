# Generated by Django 2.1.1 on 2018-09-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='baidu_face_search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lession_id', models.CharField(max_length=100)),
                ('stu_no', models.CharField(max_length=32)),
                ('faceToken', models.CharField(max_length=100)),
                ('score', models.FloatField()),
                ('user_id', models.CharField(max_length=32)),
                ('error_code', models.CharField(max_length=32)),
                ('error_msg', models.CharField(max_length=100)),
            ],
        ),
    ]
