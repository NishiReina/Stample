# Generated by Django 3.2.5 on 2021-12-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stamp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stamp',
            name='judgement',
            field=models.BooleanField(blank=True, default=False, verbose_name='判定'),
        ),
    ]
