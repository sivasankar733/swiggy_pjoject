# Generated by Django 3.0.4 on 2020-04-15 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=40)),
                ('admin_password', models.CharField(max_length=30)),
                ('otpcode', models.IntegerField(unique=True)),
            ],
        ),
    ]
