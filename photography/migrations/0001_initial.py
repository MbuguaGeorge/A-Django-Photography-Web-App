# Generated by Django 3.1.4 on 2021-02-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_id', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
