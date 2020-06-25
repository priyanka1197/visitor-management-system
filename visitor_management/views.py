from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from accounts.models import Host, guest
from accounts.forms import *
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
## Homepage
def home(request):
    return render(request, 'homepage.html')

## manager details for visitors
def doctors(request):
    hosts = Host.objects.all()
    parameters = {'hosts':hosts}
    return render(request,'doctors.html',parameters)

## Login page for admin
def loginPage(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/dashboard")
        else:
            return redirect('/admin_login/')

    else:
        return render(request,'admin_login.html')
        
def managerlogin(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=host_name,password=Host.host_phone)

        if user is not None:
            auth.login(request, user)
            return redirect("/dashboard")
        else:
            return redirect('/manager_login')

    else:
        return render(request,'manager_login.html')
        
def guest(request):
     if request.POST.get("guest"): 
            host_id = request.POST.get("guest")
            host = Host.objects.get(id = host_id)
            form = Visitorform()
            param = {'form':form,'host':host}
            return render(request, 'guestdetail.html', param)

def save_guest(request):
     if request.method == 'POST':
        host_name = request.POST.get('host')
        host = Host.objects.get(host_name=host_name)
        form = Visitorform(request.POST)
        #import ipdb;ipdb.set_trace()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.host = host_name
            instance.save()
            rec = [host.host_email]
            subject = instance.name +" Checked In !"
            visitor = instance
            ## EMAIL AND SMS TO HOST
            email(subject,visitor,rec)
            messages.success(request,'Information sent to Host, You will be called shortly !!')
            return redirect('/doctors')
        else:
            print(form.errors)
            return HttpResponse
     else:
        return redirect('/doctors')
def email(subject,visitor,rec,host=None):
    ## FILL IN YOUR DETAILS HERE
    sender = 'priyanka4.p.cp@gmail.com'
    html_content = render_to_string('visitor_mail_template.html', {'visitor':visitor,'host':host}) # render with dynamic value
    html_content = render_to_string('host_mail_template.html', {'visitor':visitor}) # render with dynamic value
    text_content = strip_tags(html_content)

    # try except block to avoid wesite crashing due to email error
    try:
        msg = EmailMultiAlternatives(subject, text_content, sender, rec)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except:
        pass
    return

