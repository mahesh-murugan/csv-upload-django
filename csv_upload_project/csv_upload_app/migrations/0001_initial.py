# Generated by Django 3.1.4 on 2020-12-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=40)),
            ],
        ),
    ]
