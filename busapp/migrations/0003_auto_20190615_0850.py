# Generated by Django 2.2.2 on 2019-06-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0002_busmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busmodel',
            name='departure',
            field=models.DateTimeField(),
        ),
    ]