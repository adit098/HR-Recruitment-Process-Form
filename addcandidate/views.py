from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls.conf import include
from .models import *
from json import dumps
from django.db.models import Q, fields
from .forms import ExtraMeetingForm, RecruitmentForm
from django.forms import modelformset_factory, formset_factory


def home(request):
    return render(request, 'addcandidate/home.html')


@login_required
def add_candidate(request):
    roles = Role.objects.all()
    positions = Constants.POSITION
    sources = Constants.SOURCE
    param_values = Constants.PARAMETER_VALUES
    roles_parameters = {}
    for role in roles:
        r = Role.objects.filter(role=role.role).values_list('rating_parameters__parameters')
        r = list(i[0] for i in r)
        roles_parameters[role.role] = r

    # print(roles_parameters, roles_parameters['sales'], type(roles_parameters['sales']))
    roles_parameters = dumps(roles_parameters)

    # print(roles_parameters)
    param_no = 4
    param_val_no = 3

    attitudes = Attitude.objects.all()


    context = {
        'roles': roles,
        'positions': positions,
        'sources': sources,
        'roles_parameters': roles_parameters,
        'param_values': param_values,
        'param_no': range(param_no),
        'param_val_no': range(param_val_no),
        'attitudes': attitudes
    }
    return render(request, 'addcandidate/addcandidate.html', context)


@login_required
def list_candidate(request):
    if request.user.is_superuser:
        completed_recruitment_forms = Recruitment.objects.filter(Q(first_meeting_status="rejected")  | Q(second_meeting_status="shortlisted") | Q(second_meeting_status="rejected")).order_by('-pk')
        incompleted_recruitment_forms = Recruitment.objects.filter(~(Q(first_meeting_status="rejected")  | Q(second_meeting_status="shortlisted") | Q(second_meeting_status="rejected"))).order_by('-pk')
        all_recruitment_forms = Recruitment.objects.all().order_by('-pk')
    else:
        completed_recruitment_forms = Recruitment.objects.filter(Q(HR=request.user) & (Q(first_meeting_status="rejected")  | Q(second_meeting_status="shortlisted") | Q(second_meeting_status="rejected"))).order_by('-pk')
        incompleted_recruitment_forms = Recruitment.objects.filter(Q(HR=request.user) & ~((Q(first_meeting_status="rejected")  | Q(second_meeting_status="shortlisted") | Q(second_meeting_status="rejected")))).order_by('-pk')
        all_recruitment_forms = Recruitment.objects.filter(Q(HR=request.user)).order_by('-pk')

    print(completed_recruitment_forms)
    print(incompleted_recruitment_forms)
    print(all_recruitment_forms)


    context = {
        'completed_recruitment_forms': completed_recruitment_forms,
        'incompleted_recruitment_forms': incompleted_recruitment_forms,
        'all_recruitment_forms': all_recruitment_forms
    }

    return render(request, 'addcandidate/listcandidate.html', context)


@login_required
def view_candidate(request, pk):
    context = {}
    candidate = Recruitment.objects.get(pk=pk)
    if candidate.HR != request.user:
        return HttpResponseRedirect(reverse("addcandidate:listcandidate"))

    context["candidate"] = candidate

    return render(request, "addcandidate/viewcandidate.html", context)


@login_required
def update_candidate(request, pk):
    # context = {}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Recruitment, pk = pk)
 
    # pass the object as instance in form
    form = RecruitmentForm(instance = obj)
    candidate = Recruitment.objects.get(pk=pk)
    if candidate.HR != request.user:
        return HttpResponseRedirect(reverse("addcandidate:listcandidate"))


    extra_meeting_objects = []
    extra_meeting_forms = []
    for extra_meeting in candidate.more_meetings.all():
        extra_meeting_objects.append(extra_meeting)
        extra_meeting_forms.append((ExtraMeetingForm(instance=extra_meeting)))


    last_meet_id = list(ExtraMeeting.objects.all().values_list('pk'))[-1][0]


    ExtraMeetingFormSet = modelformset_factory(ExtraMeeting, form=ExtraMeetingForm, fields='__all__', extra=0)
    formset = ExtraMeetingFormSet(queryset=candidate.more_meetings.all())

    print(formset.is_valid())


    # ExtraMeetingFormSet = formset_factory(ExtraMeetingForm)
    # formset = ExtraMeetingFormSet()
    

    
 
    # save the data from the form and
    # redirect to detail_view

    print("-------------------sdfkjhfehl--------------------------------------------", form.is_valid())
    if request.method == 'POST':
        form = RecruitmentForm(request.POST, request.FILES, instance = obj)
        formset = ExtraMeetingFormSet(request.POST, queryset=candidate.more_meetings.all())

        print(form.is_valid())
        print(formset.is_valid())
        print(formset.errors)
        print(formset.non_form_errors())
        # print(form)
        if form.is_valid() and formset.is_valid():
            inst = form.save(commit=False)
            print("hjhjhlhlohhlhlhlh")

            print(formset.is_valid())
            print(formset.errors)
            print(formset.non_form_errors())
            for data in formset:
                data.save()

            extra_meetings_in_update = ExtraMeeting.objects.filter(pk__gt=last_meet_id)
            for mt in extra_meetings_in_update:
                inst.more_meetings.add(mt)
            inst.save()
            

            
            
            return HttpResponseRedirect(reverse("addcandidate:viewcandidate", args=(pk,)))


 
    # add form dictionary to context
    roles = Role.objects.all()
    positions = Constants.POSITION
    sources = Constants.SOURCE
    param_values = Constants.PARAMETER_VALUES
    roles_parameters = {}
    for role in roles:
        r = Role.objects.filter(role=role.role).values_list('rating_parameters__parameters')
        r = list(i[0] for i in r)
        roles_parameters[role.pk] = r

    # print(roles_parameters, roles_parameters['sales'], type(roles_parameters['sales']))
    roles_parameters = dumps(roles_parameters)

    param_no = 4
    param_val_no = 3

    attitudes = Attitude.objects.all()


    context = {
        'roles': roles,
        'positions': positions,
        'sources': sources,
        'roles_parameters': roles_parameters,
        'param_values': param_values,
        'param_no': range(param_no),
        'param_val_no': range(param_val_no),
        'attitudes': attitudes,
        'form': form,
        'extra_meeting_forms': extra_meeting_forms,
        'formset': formset,
        'last_meet_id': last_meet_id
    }

 
    return render(request, "addcandidate/updatecandidate.html", context)


@login_required
def delete_candidate(request):
    if request.method == 'POST':
        candidate_id=request.POST["dlt_candidate"]
        print("candidate_id--------------------------------", candidate_id, type(candidate_id))
        candidate=Recruitment.objects.get(pk=candidate_id)
        for extra_meeting in candidate.more_meetings.all():
            extra_meeting.delete()
        candidate.delete()
    return HttpResponseRedirect(reverse("addcandidate:listcandidate"))



@login_required
def add_candidate_submit(request):
    if request.method == 'POST':
        fn = request.POST.get("first-name")
        mn = request.POST.get("middle-name")
        ln = request.POST.get("last-name")
        print(fn, mn, ln)

        contact = request.POST.get("contact-number")
        linkedin  = request.POST.get("linkedin-link")

        state = request.POST.get('input-state')
        district = request.POST.get('input-district')
        print(state, district)

        date_called = request.POST.get('date-called')
        time_called = request.POST.get('time-called')

        role = Role.objects.get(role=request.POST.get('role'))
        position = request.POST.get('position')

        other_role = request.POST.get('other-role')
        other_position = request.POST.get('other-position')

        rp1 = request.POST.get('roles-parametrs-0')
        rp2 = request.POST.get('roles-parametrs-1')
        rp3 = request.POST.get('roles-parametrs-2')
        rp4 = request.POST.get('roles-parametrs-3')
        print(rp1, rp2, rp3, rp4)

        attitudes = request.POST.getlist('attitude')
        print("hello", attitudes, type(attitudes))
        

        p_note = request.POST.get('positive-note')
        n_note = request.POST.get('negative-note')
        a_note = request.POST.get('additional-note')

        source = request.POST.get('source')
        other_source = request.POST.get('other-source')

        fm_status = request.POST.get('first-meeting-status')
        fm_a_note = request.POST.get('additional-note-first-meeting')
        print("status1", fm_status)

        interview_date = request.POST.get('date-interview')
        interview_time = request.POST.get('time-interview')

        sm_status = request.POST.get('second-meeting-status')
        sm_a_note = request.POST.get('additional-note-second-meeting')
        print("status2", sm_status)

        email = request.POST.get('email')

        candidate = Recruitment.objects.create(
            HR=request.user,
            first_name=fn,
            middle_name=mn,
            last_name=ln,
            contact_number=contact,
            linkedin_link=linkedin,
            state=state,
            city=district,
            date_called=date_called,
            time_called=time_called,
            role=role,
            position=position,
            other_role=other_role,
            other_position=other_position,
            first_param_val=rp1,
            second_param_val=rp2,
            third_param_val=rp3,
            fourth_param_val=rp4,

            positive_notes=p_note,
            negative_notes=n_note,
            additional_notes=a_note,
            source=source,
            other_source=other_source,
            first_meeting_status=fm_status,
            additional_notes_on_first_meeting=fm_a_note,
            second_meeting_status=sm_status,
            additional_notes_on_second_meeting=sm_a_note,
            email=email
            )

        for attitude in attitudes:
            at_obj = Attitude.objects.get(attitude=attitude)
            candidate.attitude.add(at_obj)

        if 'resume' in request.FILES:
            candidate.resume = request.FILES['resume']

        if 'aadhar' in request.FILES:
            candidate.aadhar = request.FILES['aadhar']

        if interview_date != "":
            candidate.interview_date = interview_date

        if interview_time != "":
            candidate.interview_time = interview_time

        addtional_meeting_no = 3
        print('date-interview-' +str(addtional_meeting_no))
        while True:
            print("here")
            try:
                print("here1")
                extra_meet_obj = ExtraMeeting.objects.create(
                    extra_interview_date=request.POST['date-interview-'+str(addtional_meeting_no)],
                    extra_interview_time=request.POST['time-interview-'+str(addtional_meeting_no)],
                    extra_meeting_status=request.POST[str(addtional_meeting_no)+'no-meeting-status'],
                    additional_notes_on_extra_meeting=request.POST['additional-note-' + str(addtional_meeting_no)+'-meeting'],
                )
                candidate.more_meetings.add(extra_meet_obj)
                addtional_meeting_no+=1
            except:
                print("breaking----------")
                break

        

        
        candidate.save()

        return HttpResponseRedirect(reverse("addcandidate:listcandidate"))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # 'username' from name input box in login.html
        password = request.POST.get('password')  # 'password' from name input box in login.html

        user = authenticate(username=username, password=password)
        print(user)

        if user:
            print(user.is_active)
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('addcandidate:home'))
            else:
                return HttpResponseRedirect("ACCOUNTS NOT ACTIVE")
        else:
            messages.error(request, 'username or password not correct')
            return redirect('addcandidate:user_login')

    else:
        print('now first i m going to template file')
        return render(request, 'addcandidate/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('addcandidate:home'))