# Generated by Django 2.2.5 on 2019-10-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_auto_20191015_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
