# Generated by Django 4.2.7 on 2023-12-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earsip_app', '0003_alter_disposisi_no_surat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semuaarsip',
            name='surat_dari',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
