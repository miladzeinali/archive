

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0016_category_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='drawn',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
