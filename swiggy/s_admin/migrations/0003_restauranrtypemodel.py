# Generated by Django 3.0.4 on 2020-04-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_admin', '0002_areamodel_citymodel_statemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestauranrTypeModel',
            fields=[
                ('type_no', models.IntegerField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=40)),
            ],
        ),
    ]