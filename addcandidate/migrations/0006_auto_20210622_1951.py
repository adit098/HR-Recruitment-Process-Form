# Generated by Django 2.2.5 on 2021-06-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcandidate', '0005_auto_20210622_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='aadhar',
            field=models.FileField(blank=True, null=True, upload_to='aadhar/'),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='additional_notes_on_second_meeting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='interview_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='interview_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='negative_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='positive_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='second_meeting_status',
            field=models.CharField(blank=True, choices=[('shortlisted', 'Shortlisted'), ('rejected', 'Rejected')], max_length=50, null=True),
        ),
    ]