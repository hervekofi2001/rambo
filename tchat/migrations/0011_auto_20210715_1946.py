# Generated by Django 3.1.6 on 2021-07-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tchat', '0010_mesurer_rapport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesurer',
            name='rapport',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
