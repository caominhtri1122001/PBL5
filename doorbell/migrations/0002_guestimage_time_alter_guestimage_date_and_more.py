# Generated by Django 4.0.3 on 2022-06-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorbell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestimage',
            name='time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='guestimage',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='guestimage',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]