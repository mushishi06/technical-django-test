# Generated by Django 2.2.17 on 2021-01-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='capital',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='topLevelDomain',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]