# Generated by Django 3.1.1 on 2021-04-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20210406_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='newspics')),
                ('link', models.TextField(null=True)),
                ('datetimenow', models.DateTimeField()),
            ],
            options={
                'ordering': ('datetimenow',),
            },
        ),
        migrations.AlterModelOptions(
            name='patientdetails',
            options={'ordering': ('date', 'time')},
        ),
    ]