# Generated by Django 4.2.6 on 2024-01-01 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_comment_id_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]