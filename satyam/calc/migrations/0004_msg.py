# Generated by Django 3.0.5 on 2020-06-16 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('messages', models.TextField()),
            ],
        ),
    ]