# Generated by Django 4.2.1 on 2025-01-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_natijalar_ball'),
    ]

    operations = [
        migrations.AddField(
            model_name='natijalar',
            name='javoblari',
            field=models.TextField(blank=True, null=True),
        ),
    ]
