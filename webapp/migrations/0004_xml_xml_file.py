# Generated by Django 3.2.9 on 2021-11-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_xml_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='xml',
            name='xml_file',
            field=models.FileField(blank=True, max_length=500, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
