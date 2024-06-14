# Generated by Django 4.2.7 on 2024-05-18 10:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mother', '0021_child_state_health_alter_child_age_alter_child_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learn', models.CharField(blank=True, max_length=200, null=True)),
                ('activities', models.CharField(blank=True, choices=[('drawing and coloring', 'drawing and coloring'), ('music', 'music'), ('reading stories', 'reading stories')], max_length=200, null=True)),
                ('attiude', models.CharField(blank=True, max_length=200, null=True)),
                ('mood', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('location', models.CharField(blank=True, choices=[('arrive', 'arrive'), ('left', 'left')], max_length=200, null=True)),
                ('Important_notice', models.CharField(blank=True, max_length=200, null=True)),
                ('child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mother.child')),
            ],
        ),
    ]