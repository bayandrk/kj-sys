# Generated by Django 4.2.7 on 2024-06-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mother', '0029_alter_child_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='meal_images_path',
            field=models.CharField(blank=True, choices=[('meat', 'images/meat.jpg'), ('milk', 'images/milk.jpg')], max_length=200, null=True),
        ),
    ]
