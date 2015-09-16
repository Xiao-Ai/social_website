from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from account.models import User, Info
from employer.models import Employer, Job
from models import Education, Experience, EducationForm, ExperienceForm

# Create your views here.
def resume(request):
    context = {}
    user_id = request.session["user_id"]
    user_obj = User.objects.get(id=user_id)
    info_obj = Info.objects.get(email=user_obj)
    
    try:
        education_obj = Education.objects.get(user=user_obj)
        experience_obj = Experience.objects.get(user=user_obj)
    except:
        education_obj = None
        experience_obj = None

    # For users: get offers
    try:
        offers = Job.objects.filter(employees=user_obj)
        context.update({ 'offers':offers })
    except:
        pass

    # For users: get user_obj, job_obj
    try:
        user_id = request.session["user_id"]
        user_obj = User.objects.get(id=user_id)
        info_obj = Info.objects.get(email=user_obj)
        job = Job.objects.get(id=request.session['job_id'])
        context.update({ 'user_obj':user_obj, 'job':job, 'info_obj':info_obj })
    except:
        pass

    context.update({ 'user_obj': user_obj, 'info_obj':info_obj, 'education_obj':education_obj, 'experience_obj':experience_obj })
    template = 'resume/resume.html'
    return render(request, template, context)

def resume_edu(request):
    user_id = request.session["user_id"]
    user_obj = User.objects.get(id=user_id)
    email = user_obj.email
    user_list = User.objects.all()
    info_obj = Info.objects.get(email=user_obj)

    if request.method == 'POST':
        edu_form = EducationForm(request.POST)
        if edu_form.is_valid():
            print 'valid'
            user = edu_form.cleaned_data['user']
            degree = edu_form.cleaned_data['degree']
            school = edu_form.cleaned_data['school']
            department = edu_form.cleaned_data['department']
            
            new_edu, created = Education.objects.get_or_create(user=user, \
                                                               degree=degree, \
                                                               school=school, \
                                                               department=department)
            
            if created:
                new_edu.save()
                return HttpResponseRedirect('/resume/resume_exp/')
    else:
        print 'no'
        edu_form = EducationForm()

    context = { 'user_obj': user_obj, 'info_obj':info_obj, 'edu_form':edu_form, 'email':email, 'user_list':user_list }
    template = 'resume/resume_edu.html'
    return render(request, template, context)

def resume_exp(request):
    user_id = request.session["user_id"]
    user_obj = User.objects.get(id=user_id)
    email = user_obj.email
    user_list = User.objects.all()
    info_obj = Info.objects.get(email=user_obj)

    if request.method == 'POST':
        exp_form = ExperienceForm(request.POST)
        if exp_form.is_valid():
            user = exp_form.cleaned_data['user']
            activity = exp_form.cleaned_data['activity']
            internship = exp_form.cleaned_data['internship']
            awards = exp_form.cleaned_data['awards']
            association = exp_form.cleaned_data['association']
            other = exp_form.cleaned_data['other']
             
            new_exp, created = Experience.objects.get_or_create(user=user, \
                                                               activity=activity, \
                                                               internship=internship, \
                                                               awards=awards, \
                                                               association=association, \
                                                               other=other, \
                                                               )

            if created:
                new_exp.save()
                return HttpResponseRedirect('/resume/')
    else:
        exp_form = ExperienceForm()

    context = {'user_obj': user_obj, 'info_obj':info_obj, 'exp_form':exp_form, 'email':email, 'user_list':user_list}
    template = 'resume/resume_exp.html'
    return render(request, template, context)

def job_offer(request):
    context = {}
    user_obj = User.objects.get(id=request.session["user_id"])

    # For users: get user_obj, job_obj and send resume
    try:
        info_obj = Info.objects.get(email=user_obj)
        context.update({ 'info_obj':info_obj })
    except:
        pass

    # get offers
    try:
        offers = Job.objects.filter(employees=user_obj)
        context.update({ 'offers':offers })
    except:
        pass

    template = 'resume/job_offer.html'
    context.update({ 'user_obj':user_obj, })
    return render(request, template, context)
