# Generated by Django 4.2.7 on 2023-11-30 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earsip_app', '0002_alter_tempsuratkeluar_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposisi',
            name='no_surat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='earsip_app.semuaarsip'),
        ),
    ]
