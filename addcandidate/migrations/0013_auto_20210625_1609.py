# Generated by Django 2.2.5 on 2021-06-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcandidate', '0012_auto_20210625_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='interview_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='interview_time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]
