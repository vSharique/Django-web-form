# Generated by Django 2.1 on 2018-08-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateTimeField()),
                ('emailid', models.EmailField(max_length=50)),
                ('ph_no', models.CharField(max_length=10)),
            ],
        ),
    ]