from django.contrib.messages import constants
from django.db import models
from django.db.models import constraints
from django.utils import timezone
from django.contrib.auth.models import User


class Constants:
    ROLE = (
        ('sales', 'Sales'),
        ('human_resources', 'Human Resources'),
        ('marketing', 'Marketing'),
        ('sales_and_marketing', 'Sales & Marketing'),
        ('graphic_designer', 'Graphic Designer'),
        ('operations', 'Operations'),
        ('content_writer', 'Content Writer'),
        ('digital_marketing', 'Digital Marketing'),
        ('python_developer', 'Python Developer'),
        ('android_developer', 'Android Developer'),
        ('web_developer', 'Web Developer'),
        ('administration', 'Administration'),
        ('relationship_manager', 'Relationship Manager'),
        ('marketing_communication', 'Marketing Communication'),
        ('finance', 'Finance'),
        ('other', 'Other')
    )

    POSITION = (
        ('intern', 'Intern'),
        ('executive', 'Executive'),
        ('other', 'Other')
    )

    RATING_PARAMETERS = (
        ('communication', 'Communication'),
        ('background_knowledge', 'Background / Knowledge'),
        ('willingness_interest', 'Wilingness / Interest'),
        ('confidence', 'Confidence'),
        ('skill_test', 'Skill (Test)'),
        ('skill', 'Skill'),
        ('knowledge', 'Knowledge'),
        ('creativity', 'Creativity'),
    )

    ATTITUDE = (
        ('active_listening', 'Active Listening'),
        ('genuine', 'Genuine'),
        ('optimistic', 'Optimistic'),
        ('responsive', 'Responsive'),
        ('humility', 'Humility'),
        ('attentive', 'Attentive'),
        ('honest', 'Honest'),
        ('laidback', 'Laidback'),
        ('boastful', 'Boastful'),
        ('unsure', 'Unsure'),
        ('brash', 'Brash'),
        ('disinterested', 'Disinterested'),
        ('manipulative', 'Manipulative'),
        ('informal', 'Informal')
    )

    PARAMETER_VALUES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )

    SOURCE = (
        ('linkedin', 'LinkedIn'),
        ('internshala', 'Internshala'),
        ('indeed', 'Indeed'),
        ('naukri', 'Naukri'),
        ('letsintern', 'LetsIntern'),
        ('hellointern', 'HelloIntern'),
        ('employee_referral', 'Employee Referral'),
        ('times_jobs', 'Times Jobs'),
        ('college', 'College'),
        ('other', 'Other')
    )

    MEETING_STATUS = (
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('meeting_to_be_held', 'Meeting To Be Held')
    )


# class Position(models.Model):
#     position = models.CharField(max_length=50, choices=Constants.POSITION, unique=True)

#     def __str__(self):
#         return self.get_position_display()


class ExtraMeeting(models.Model):
    extra_interview_date = models.DateField(blank=True, default=None, null=True)
    extra_interview_time = models.TimeField(blank=True, default=None, null=True)

    extra_meeting_status = models.CharField(max_length=50, choices=Constants.MEETING_STATUS, blank=True, null=True)
    additional_notes_on_extra_meeting = models.TextField(blank=True, null=True)



class Parameter(models.Model):
    parameters = models.CharField(max_length=50, choices=Constants.RATING_PARAMETERS, unique=True)
    # parameter_value = models.CharField(max_length=50, choices=Constants.PARAMETER_VALUES)

    def __str__(self):
        return self.get_parameters_display()
    

class Role(models.Model):
    role = models.CharField(max_length=50, choices=Constants.ROLE, unique=True)
    rating_parameters = models.ManyToManyField(Parameter)

    def __str__(self):
        return self.get_role_display()
    

class Attitude(models.Model):
    attitude = models.CharField(max_length=50, choices=Constants.ATTITUDE, unique=True)

    def __str__(self):
        return self.get_attitude_display()
    

#recruitment process for candidate filled by HR
class Recruitment(models.Model):
    HR = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    contact_number = models.CharField(max_length=13, unique=True)
    linkedin_link = models.URLField(max_length=200, unique=True, blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date_called = models.DateField(default=timezone.now)
    time_called = models.TimeField()

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    # position = models.ForeignKey(Position, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, choices=Constants.POSITION)

    other_role = models.CharField(max_length=50, blank=True)
    other_position = models.CharField(max_length=50, blank=True)


    first_param_val = models.CharField(max_length=50, choices=Constants.PARAMETER_VALUES)
    second_param_val = models.CharField(max_length=50, choices=Constants.PARAMETER_VALUES)
    third_param_val = models.CharField(max_length=50, choices=Constants.PARAMETER_VALUES)
    fourth_param_val = models.CharField(max_length=50, choices=Constants.PARAMETER_VALUES)

    attitude = models.ManyToManyField(Attitude)

    #Notes
    positive_notes = models.TextField(blank=True)
    negative_notes = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)

    #Sources
    source = models.CharField(max_length=50, choices=Constants.SOURCE)
    other_source = models.CharField(max_length=50, blank=True)

    #1st meeting status
    first_meeting_status = models.CharField(max_length=50, choices=Constants.MEETING_STATUS)
    additional_notes_on_first_meeting = models.TextField(blank=True)

    #if shortlisted then schedule interview
    interview_date = models.DateField(blank=True, default=None, null=True)
    interview_time = models.TimeField(blank=True, default=None, null=True)

    #2nd meeting status
    second_meeting_status = models.CharField(max_length=50, choices=Constants.MEETING_STATUS, blank=True, null=True)
    additional_notes_on_second_meeting = models.TextField(blank=True, null=True)

    more_meetings = models.ManyToManyField(ExtraMeeting, blank=True)

    #if shortlisted then attatch aadhar and add email 
    aadhar = models.FileField(upload_to='aadhar/', blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)












#passwords: 
#deepak - 1234
#mansi - hr@12345
#kassandra - hr@23456
#sakshi - hr@34567