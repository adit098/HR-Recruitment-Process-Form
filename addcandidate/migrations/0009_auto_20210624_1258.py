# Generated by Django 2.2.5 on 2021-06-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcandidate', '0008_auto_20210624_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
