# Generated by Django 5.1 on 2024-09-17 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 9, 17, 14, 50, 17, 8295), null=True, verbose_name='Дата'),
        ),
    ]
