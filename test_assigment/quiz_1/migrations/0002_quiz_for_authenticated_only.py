# Generated by Django 4.1.4 on 2022-12-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='for_authenticated_only',
            field=models.BooleanField(default=False, verbose_name='is_for_authenticated_only?'),
        ),
    ]
