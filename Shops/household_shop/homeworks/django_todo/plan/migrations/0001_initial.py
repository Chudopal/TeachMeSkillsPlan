# Generated by Django 4.0.6 on 2022-07-20 17:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('started_at', models.DateField(default=datetime.date.today)),
                ('finished_at', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('depends_on', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.event')),
            ],
            options={
                'db_table': 'events',
            },
        ),
    ]