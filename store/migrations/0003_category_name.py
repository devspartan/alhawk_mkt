# Generated by Django 3.1.3 on 2020-12-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]