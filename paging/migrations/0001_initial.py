# Generated by Django 4.1.5 on 2023-01-04 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(null=True)),
                ('page_count', models.IntegerField(null=True)),
                ('page_size', models.IntegerField(null=True)),
                ('left_page', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.IntegerField()),
                ('page_count', models.IntegerField(default=0)),
                ('duration', models.IntegerField()),
                ('start_time', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'pending'), ('D', 'done'), ('NS', 'not started')], default='NS', max_length=3)),
            ],
        ),
    ]
