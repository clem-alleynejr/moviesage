# Generated by Django 4.2.2 on 2023-06-17 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(max_length=250)),
                ('image', models.CharField(max_length=250)),
                ('full_title', models.CharField(max_length=250)),
                ('release_date', models.CharField(max_length=250)),
                ('runtime_str', models.CharField(max_length=250)),
                ('director', models.CharField(max_length=250)),
                ('plot', models.CharField(max_length=250)),
                ('stars', models.TextField(max_length=250)),
            ],
        ),
    ]
