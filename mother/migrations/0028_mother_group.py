# Generated by Django 4.2.7 on 2024-06-04 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('mother', '0027_rename_important_notice_child_important_nots'),
    ]

    operations = [
        migrations.AddField(
            model_name='mother',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]