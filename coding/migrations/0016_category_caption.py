# Generated by Django 3.2.3 on 2023-08-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0015_alter_category_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='caption',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
