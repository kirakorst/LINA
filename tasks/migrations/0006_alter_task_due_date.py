# Generated by Django 5.1 on 2024-09-10 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 9, 10, 12, 23, 31, 977875), null=True, verbose_name='Дата'),
        ),
    ]
