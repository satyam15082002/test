# Generated by Django 3.0.5 on 2020-04-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='video',
        ),
        migrations.AlterField(
            model_name='upload',
            name='img',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]
