# Generated by Django 3.2.2 on 2022-03-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0004_auto_20220329_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.CharField(default='india', max_length=20),
        ),
    ]