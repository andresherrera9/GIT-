# Generated by Django 2.2.5 on 2021-04-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referencias', '0002_auto_20210407_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
    ]
