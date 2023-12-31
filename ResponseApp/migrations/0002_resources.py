# Generated by Django 4.2.6 on 2023-12-09 18:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ResponseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('fire', models.IntegerField(default=34)),
                ('medical', models.IntegerField(default=34)),
                ('crime', models.IntegerField(default=34)),
                ('rfid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
