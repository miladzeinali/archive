# Generated by Django 3.2.3 on 2023-08-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0009_alter_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[(1, 'Zone'), (2, 'Area'), (3, 'ME'), (4, 'MED'), (5, 'MEDM'), (6, 'Part')], default='assem', max_length=10),
        ),
    ]
