# Generated by Django 4.1.5 on 2023-01-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('content', models.JSONField(default=dict)),
            ],
        ),
    ]