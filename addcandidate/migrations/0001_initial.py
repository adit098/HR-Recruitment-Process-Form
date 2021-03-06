# Generated by Django 2.2.5 on 2021-06-21 14:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attitude', models.CharField(choices=[('active_listening', 'Active Listening'), ('genuine', 'Genuine'), ('optimistic', 'Optimistic'), ('responsive', 'Responsive'), ('humility', 'Humility'), ('attentive', 'Attentive'), ('honest', 'Honest'), ('laidback', 'Laidback'), ('boastful', 'Boastful'), ('unsure', 'Unsure'), ('brash', 'Brash'), ('disinterested', 'Disinterested'), ('manipulative', 'Manipulative'), ('informal', 'Informal')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.CharField(choices=[('communication', 'Communication'), ('background_knowledge', 'Background / Knowledge'), ('willingness_interest', 'Wilingness / Interest'), ('confidence', 'Confidence'), ('skill_test', 'Skill (Test)'), ('skill', 'Skill'), ('knowledge', 'Knowledge'), ('creativity', 'Creativity')], max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('sales', 'Sales'), ('human_resources', 'Human Resources'), ('marketing', 'Marketing'), ('sales_and_marketing', 'Sales & Marketing'), ('graphic_designer', 'Graphic Designer'), ('operations', 'Operations'), ('content_writer', 'Content Writer'), ('digital_marketing', 'Digital Marketing'), ('python_developer', 'Python Developer'), ('android_developer', 'Android Developer'), ('web_developer', 'Web Developer'), ('administration', 'Administration'), ('relationship_manager', 'Relationship Manager'), ('marketing_communication', 'Marketing Communication'), ('finance', 'Finance'), ('other', 'Other')], max_length=50)),
                ('rating_parameters', models.ManyToManyField(to='addcandidate.Parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=13, unique=True)),
                ('linkedin_link', models.URLField(unique=True)),
                ('resume', models.FileField(upload_to='resume/')),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('date_called', models.DateField(default=django.utils.timezone.now)),
                ('time_called', models.TimeField()),
                ('position', models.CharField(choices=[('intern', 'Intern'), ('executive', 'Executive'), ('other', 'Other')], max_length=50)),
                ('positive_notes', models.TextField()),
                ('negative_notes', models.TextField()),
                ('additional_notes', models.TextField(blank=True)),
                ('source', models.CharField(choices=[('linkedin', 'LinkedIn'), ('internshala', 'Internshala'), ('indeed', 'Indeed'), ('naukri', 'Naukri'), ('letsintern', 'LetsIntern'), ('hellointern', 'HelloIntern'), ('employee_referral', 'Employee Referral'), ('times_jobs', 'Times Jobs'), ('college', 'College'), ('other', 'Other')], max_length=50)),
                ('first_meeting_status', models.CharField(choices=[('shortlisted', 'Shortlisted'), ('rejected', 'Rejected')], max_length=50)),
                ('additional_notes_on_first_meeting', models.TextField(blank=True)),
                ('interview_date', models.DateField()),
                ('interview_time', models.TimeField()),
                ('second_meeting_status', models.CharField(choices=[('shortlisted', 'Shortlisted'), ('rejected', 'Rejected')], max_length=50)),
                ('additional_notes_on_second_meeting', models.TextField(blank=True)),
                ('aadhar', models.FileField(upload_to='aadhar/')),
                ('email', models.CharField(max_length=200)),
                ('attitude', models.ManyToManyField(to='addcandidate.Attitude')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addcandidate.Role')),
            ],
        ),
    ]
