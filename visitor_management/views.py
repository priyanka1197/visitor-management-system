from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from accounts.models import guest , Host
from accounts.forms import *
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
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
        
def guestdetail(request):
     if request.POST.get("guest"):    
            host_id = request.POST.get("guest")
            host = Host.objects.get(id = host_id)
            form = Visitorform()
            param = {'form':form,'host':host}
            return render(request, 'guestdetail.html', param)

def save_guest(request):
   if request.method == 'POST':
        hostname = request.POST.get('host')
        host = Host.objects.get(host_name=hostname)
        form = Visitorform(request.POST,request.FILES)
        #import pdb ; pdb.set_trace()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.hostname = hostname
            instance.save()
            rec = [host.host_email]
            subject = instance.name +" Checked In !"
            guest = instance
            ## EMAIL AND SMS TO HOST
            email(subject,guest,rec)
            messages.success(request,'Information sent to Host, You will be contacted shortly !!')
            return redirect('/doctors')
        else:
            pass
   else:
        return redirect('/doctors')
def email(subject,guest,rec,host=None):
    ## FILL IN YOUR DETAILS HERE
    sender = 'priyanka4.p.cp@gmail.com'
    html_content = render_to_string('hmail.html', {'guest':guest}) # render with dynamic value
    text_content = strip_tags(html_content)

    # try except block to avoid wesite crashing due to email error
    try:
        msg = EmailMultiAlternatives(subject, text_content, sender, rec)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except:
        pass
    return
@csrf_exempt
def checkin(request): 
    mid = request.GET.get("mid")  
    form = time()
    param = {'form':form,'mid':mid}
    return render(request, 'checkin.html', param)
@csrf_exempt
def checkinsubmit(request):     
     if request.method == 'POST':
         form = time(request.POST)
         #import pdb;pdb.set_trace()
         if form.is_valid():
           timeassign = form.cleaned_data['timeassigned'] 
           mid = form.cleaned_data['mid']
           Guest = guest.objects.get(id=mid)          
           message = "Your Meeting confirmed with "+Guest.hostname+". is at "+timeassign+". Your otp is 2954"
           recipients = [Guest.email]
           subject = "Visitors meeting confirmation"
           sender = 'Priyanka4.p.cp@gmail.com'
           send_mail(subject, message, sender, recipients)
           return render(request, 'doctors.html')

def company(request):
    return render(request, 'company.html')

def barcode(request):
    #instantiate a drawing object
    d = barcode.MyBarcodeDrawing("")
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')
