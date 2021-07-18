from django import forms
from django.db.models import fields
from .models import *
 



class ExtraMeetingForm(forms.ModelForm):
    # dynamic_id = 3

    class Meta:
        model = ExtraMeeting
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExtraMeetingForm, self).__init__(*args, **kwargs)
        self.fields['extra_interview_date'].widget = forms.DateInput(attrs={
            'type': 'date',
            'id': 'extra-date-interview',
            'class': 'ui input',
            'name': 'extra-date-interview',
            'placeholder': 'Date'})

        self.fields['extra_interview_time'].widget = forms.TimeInput(attrs={
            'type': 'time',
            'id': 'extra-time-interview',
            'class': 'ui input',
            'name': 'extra-time-interview',
            'placeholder': 'Time'})


        self.fields['extra_meeting_status'].widget = forms.RadioSelect(attrs={
            'class': 'ui radio checkbox',
            'name': 'extra-meeting-stat'})

        self.fields['extra_meeting_status'].widget.choices = self.fields['extra_meeting_status'].choices


        self.fields['additional_notes_on_extra_meeting'].widget = forms.TextInput(attrs={
            'type': 'text',
            'id': 'extra-note',
            'name': 'extra-note'})

        # ExtraMeetingForm.dynamic_id += 1


 
# creating a form
class RecruitmentForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Recruitment
 
        # specify fields to be used
        exclude = ('HR', 'state', 'city', 'attitude')
    
    # more_meetings = forms.ModelMultipleChoiceField(queryset=ExtraMeeting.objects.all())


    def __init__(self, *args, **kwargs):
        super(RecruitmentForm, self).__init__(*args, **kwargs)
        self.fields['date_called'].widget = forms.DateInput(attrs={
            'type': 'date',
            'id': 'date-called',
            'class': 'ui input',
            'name': 'date-called',
            'placeholder': 'Date'})

        self.fields['time_called'].widget = forms.TimeInput(attrs={
            'type': 'time',
            'id': 'time-called',
            'class': 'ui input',
            'name': 'time-called',
            'placeholder': 'Time'})

        self.fields['role'].widget = forms.Select(attrs={
            'id': 'role',
            'class': 'ui search fluid dropdown',
            'name': 'role'})

        self.fields['role'].widget.choices = self.fields['role'].choices

        self.fields['position'].widget = forms.Select(attrs={
            'id': 'position',
            'class': 'ui search fluid dropdown',
            'name': 'position'})

        self.fields['position'].widget.choices = self.fields['position'].choices

        self.fields['first_param_val'].widget = forms.RadioSelect(attrs={
            'class': 'ui radio checkbox',
            'name': 'roles-parametrs-0',
            'id': 'rp-0'})
        
        self.fields['first_param_val'].widget.choices = self.fields['first_param_val'].choices


        self.fields['second_param_val'].widget = forms.RadioSelect(attrs={
            'class': 'ui radio checkbox',
            'name': 'roles-parametrs-1',
            'id': 'rp-1'})

        self.fields['second_param_val'].widget.choices = self.fields['second_param_val'].choices


        self.fields['third_param_val'].widget = forms.RadioSelect(attrs={
            'class': 'ui radio checkbox',
            'name': 'roles-parametrs-2',
            'id': 'rp-2'})

        self.fields['third_param_val'].widget.choices = self.fields['third_param_val'].choices


        self.fields['fourth_param_val'].widget = forms.RadioSelect(attrs={
            'class': 'ui radio checkbox',
            'name': 'roles-parametrs-3',
            'id': 'rp-3'})

        self.fields['fourth_param_val'].widget.choices = self.fields['fourth_param_val'].choices


        # self.fields['attitude'].widget = forms.SelectMultiple(attrs={
        #     'id': 'attitude',
        #     'class': 'ui dropdown',
        #     'name': 'attitude',
        #     'multiple': ''})

        # self.fields['attitude'].widget.choices = self.fields['attitude'].choices


        self.fields['source'].widget = forms.Select(attrs={
            'id': 'source',
            'class': 'ui search fluid dropdown',
            'name': 'source'})

        self.fields['source'].widget.choices = self.fields['source'].choices


        self.fields['first_meeting_status'].widget = forms.RadioSelect(attrs={
            'class': 'ui radio checkbox',
            'name': 'first-meeting-status',
            'id': 'm1',
            'onclick': 'firstMeetingStatusCheckUpdate()'})

        self.fields['first_meeting_status'].widget.choices = self.fields['first_meeting_status'].choices


        self.fields['interview_date'].widget = forms.DateInput(attrs={
            'type': 'date',
            'id': 'date-interview',
            'class': 'ui input',
            'name': 'date-interview',
            'placeholder': 'Date'})

        self.fields['interview_time'].widget = forms.TimeInput(attrs={
            'type': 'time',
            'id': 'time-interview',
            'class': 'ui input',
            'name': 'time-interview',
            'placeholder': 'Time'})


        self.fields['second_meeting_status'].widget = forms.RadioSelect(attrs={
            'class': 'ui radio checkbox',
            'name': 'second-meeting-status',
            'id': 'm2',
            'onclick': 'secondMeetingStatusCheckUpdate()'})

        self.fields['second_meeting_status'].widget.choices = self.fields['second_meeting_status'].choices