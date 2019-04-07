# Generated by Django 2.1.7 on 2019-04-07 04:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailOffer',
            fields=[
                ('name', models.EmailField(max_length=255)),
                ('id', models.UUIDField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 4, 15, 6, 131151, tzinfo=utc)),
        ),
    ]
