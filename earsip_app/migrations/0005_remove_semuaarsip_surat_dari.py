# Generated by Django 4.2.7 on 2023-12-02 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earsip_app', '0004_alter_semuaarsip_surat_dari'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semuaarsip',
            name='surat_dari',
        ),
    ]