# Generated by Django 3.1.4 on 2021-02-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0007_auto_20210207_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
