# Generated by Django 3.1.2 on 2022-05-11 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        #('django_celery_beat', '0015_edit_solarschedule_events_choices'),
        ('stocks', '0002_auto_20220503_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='periodic_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_beat.periodictask'),
        ),
    ]
