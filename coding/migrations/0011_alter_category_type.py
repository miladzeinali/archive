# Generated by Django 3.2.3 on 2023-08-08 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0010_alter_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('Zone', 'Zone'), ('Area', 'Area'), ('ME', 'ME'), ('MED', 'MED'), ('MEDM', 'MEDM'), ('Part', 'Part')], default='assem', max_length=10),
        ),
    ]
