# Generated by Django 2.2.5 on 2019-09-09 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionSchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('monday', models.CharField(choices=[('morning', 'Mañana (6AM a 12M'), ('afternoon', 'Mañana (6AM a 12M'), ('unavailable', 'No disponible')], max_length=32)),
                ('tuesday', models.CharField(choices=[('morning', 'Mañana (6AM a 12M'), ('afternoon', 'Mañana (6AM a 12M'), ('unavailable', 'No disponible')], max_length=32)),
                ('wednesday', models.CharField(choices=[('morning', 'Mañana (6AM a 12M'), ('afternoon', 'Mañana (6AM a 12M'), ('unavailable', 'No disponible')], max_length=32)),
                ('thursday', models.CharField(choices=[('morning', 'Mañana (6AM a 12M'), ('afternoon', 'Mañana (6AM a 12M'), ('unavailable', 'No disponible')], max_length=32)),
                ('friday', models.CharField(choices=[('morning', 'Mañana (6AM a 12M'), ('afternoon', 'Mañana (6AM a 12M'), ('unavailable', 'No disponible')], max_length=32)),
                ('saturday', models.CharField(choices=[('morning', 'Mañana (6AM a 12M'), ('afternoon', 'Mañana (6AM a 12M'), ('unavailable', 'No disponible')], max_length=32)),
                ('sunday', models.CharField(choices=[('morning', 'Mañana (6AM a 12M'), ('afternoon', 'Mañana (6AM a 12M'), ('unavailable', 'No disponible')], max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=1024)),
                ('address', models.CharField(max_length=255)),
                ('geopoint', models.CharField(max_length=100)),
                ('collection_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='hoarding.CollectionSchedule')),
                ('waste_disposer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_disposed', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]