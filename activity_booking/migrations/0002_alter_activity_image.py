# Generated by Django 4.2.6 on 2023-10-30 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]