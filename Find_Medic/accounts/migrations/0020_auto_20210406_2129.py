# Generated by Django 3.1.1 on 2021-04-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20210406_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetails',
            name='daddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patientdetails',
            name='dcity',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patientdetails',
            name='dcontact',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='patientdetails',
            name='demail',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patientdetails',
            name='dfee',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patientdetails',
            name='dstate',
            field=models.CharField(max_length=50, null=True),
        ),
    ]