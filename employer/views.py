from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from models import Employer, EmployerForm, Job, JobForm
from account.models import User, Info

# Create your views here.

def home(request):
    try:
        employer_id = request.session['employer_id']
        employer = Employer.objects.get(id=employer_id)
        context = { 'employer':employer }
    except:
        employer = None

    jobs = Job.objects.filter(employer=employer)
    
    template = 'employer/employer_home.html'
    context.update({ 'jobs':jobs })
    return render(request, template, context)

def login(request):
    try:
        del request.session['employer_id']
    except:
        request.session['employer_id'] = None

    if request.method == 'POST':
        login = EmployerForm(request.POST)
        form_email = request.POST.get('email')
        form_password = request.POST.get('password')
        try:
            employer_obj = Employer.objects.get(email=form_email)
        except:
            employer_obj = None
            context = { 'no_employer':"no_employer" }
            template = 'employer/redirect.html'
            return render(request, template, context)

        if form_password == employer_obj.password:
            request.session['employer_id'] = employer_obj.id
            return HttpResponseRedirect('/employer/home')
        else:
            context = { 'employer_wrong_password':"employer_wrong_password" }
            template = 'employer/redirect.html'
            return render(request, template, context)
       
    else:
        login = EmployerForm()

    template = 'employer/employer_login.html'
    context = {'login': login}
    return render(request, template, context)

def register(request):
    if request.method == 'POST':
        register_form = EmployerForm(request.POST)
        if register_form.is_valid():
            new_register = register_form.save(commit=False)
            corporation = register_form.cleaned_data['corporation']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']

            new_register, created = Employer.objects.get_or_create(corporation=corporation, \
                                                                   password=password, \
                                                                   email=email)
        if created:
            new_register.save()
            return HttpResponseRedirect('/employer/')
    else:
        register_form = EmployerForm()

    template = 'employer/employer_register.html'
    context = {'register_form': register_form}
    return render(request, template, context)

def post(request):
    try:
        employer_id = request.session['employer_id']
        employer = Employer.objects.get(id=employer_id)
        context = { 'employer':employer }
    except:
        employer = None

    if request.method == 'POST':
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            new_job = job_form.save(commit=False)
            title = job_form.cleaned_data['title']
            description = job_form.cleaned_data['description']
            requirement = job_form.cleaned_data['requirement']
            address = job_form.cleaned_data['address']
            others = job_form.cleaned_data['others']
            new_job, created = Job.objects.get_or_create(employer=employer, \
                                                        title=title, \
                                                        description=description, \
                                                        requirement=requirement, \
                                                        address=address, \
                                                        others=others
                                                        )
            if created:
                new_job.save()
                return HttpResponseRedirect('/employer/home/')
    else:
        job_form = JobForm()
    
    employer_list = Employer.objects.all()
    
    template = 'employer/employer_post.html'
    context.update({ 'job_form':job_form, 'employer_list':employer_list })
    return render(request, template, context)

def job(request, job_id):
    job = Job.objects.get(id=job_id)
    request.session['job_id'] = job_id
    user_info_list = []
    context = {}

    # For employers: show employees
    employee_list = job.employees.all()

    # For employers: get employer id
    try:
        employer_id = request.session['employer_id']
        employer = Employer.objects.get(id=employer_id)
        context = { 'employer':employer }
    except:
        employer = None
    
    # For users: get user_obj, job_obj
    try:
        user_id = request.session["user_id"]
        user_obj = User.objects.get(id=user_id)
        info_obj = Info.objects.get(email=user_obj)
        job = Job.objects.get(id=job_id)
        context.update({ 'user_obj':user_obj, 'job':job, 'info_obj':info_obj })
    except:
        pass

    # For users: send resume
    if request.method == 'POST':
        try:
            job.applicants.add(user_obj)
        except:
            pass

    # For users: get offers
    try:
        offers = Job.objects.filter(employees=user_obj)
        context.update({ 'offers':offers })
    except:
        pass


    request.session['job_id'] = job.id
    for user in job.applicants.all():
        user_info_list += Info.objects.filter(email=user)
    template = 'employer/employer_job.html'
    context.update({ 'job':job, 'user_info_list':user_info_list, 'employee_list':employee_list })
    return render(request, template, context)

def hired(request):
    job = Job.objects.get(id=request.session['job_id'])
    # For employers: get employer id
    try:
        employer_id = request.session['employer_id']
        employer = Employer.objects.get(id=employer_id)
        context = { 'employer':employer }
    except:
        employer = None

    # For employers: get applicant id and hire
    applicant_id = request.session['applicant_id']
    applicant = User.objects.get(id=applicant_id)
    job.employees.add(applicant)


    template = 'employer/redirect.html'
    context.update({})
    return render(request, template, context)

def jobs_all(request):
    context = {}
    job_list = Job.objects.all()
    template = 'employer/jobs_all.html'

    # For users: get user_obj, job_obj and send resume
    try:
        user_id = request.session["user_id"]
        user_obj = User.objects.get(id=user_id)
        info_obj = Info.objects.get(email=user_obj)
        context.update({ 'user_obj':user_obj, 'info_obj':info_obj })
    except:
        pass
    
    # get offers
    try:
        offers = Job.objects.filter(employees=user_obj)
        context.update({ 'offers':offers })
    except:
        pass
    
    context.update({ 'job_list':job_list })
    return render(request, template, context)
    