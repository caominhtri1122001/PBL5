# Generated by Django 4.0.3 on 2022-06-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorbell', '0002_guestimage_time_alter_guestimage_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestimage',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
