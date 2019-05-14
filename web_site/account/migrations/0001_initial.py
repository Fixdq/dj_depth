# Generated by Django 2.2.1 on 2019-05-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.CharField(blank=True, help_text='ID', max_length=30, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '有效'), (1, '无效'), (2, '待审核')], default=2, help_text='状态', verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='最后修改时间', verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('stu_time', models.DateTimeField(verbose_name='学习时间')),
            ],
            options={
                'verbose_name': 'student',
                'db_table': 'db_stu',
            },
        ),
    ]