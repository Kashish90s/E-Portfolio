# Generated by Django 4.2.3 on 2023-08-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
