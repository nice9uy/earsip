# Generated by Django 4.2.7 on 2023-11-22 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earsip_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klasifikasisurat',
            name='group',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='subklasifikasisurat',
            name='group',
            field=models.CharField(max_length=30),
        ),
    ]