# Generated by Django 4.1.5 on 2023-01-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paging', '0002_processespersecond'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='page_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='memory',
            name='size',
            field=models.IntegerField(null=True),
        ),
    ]