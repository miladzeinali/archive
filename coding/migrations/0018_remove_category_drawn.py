# Generated by Django 3.2.3 on 2023-09-12 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0017_category_drawn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='drawn',
        ),
    ]
