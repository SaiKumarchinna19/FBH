# Generated by Django 5.1.6 on 2025-04-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_account_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='otp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(default='chinnasaikumar24@gmail.com', max_length=254),
        ),
    ]
