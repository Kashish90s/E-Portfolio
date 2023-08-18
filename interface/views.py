from django.shortcuts import render
from django.http import HttpResponse
from .models import AboutMe, Experience,Education,Skill,SocialLink,Contact,Projects
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from portfolio.settings import EMAIL_HOST_USER #replace root with 

# Create your views here.
def index(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        subject = request.POST.get("subject")
        recipient = ("maharjankashish2@gmail.com",)
       
        cont =Contact.create(name,subject,message,email)
        cont.save()
        template = render_to_string('interface/email.html',{'name':name,'description':message,'mail':email})
        email=EmailMessage(subject,template,EMAIL_HOST_USER,recipient)


        email.fail_silently=False
        if email!=None:
            email.send()
    return render(request,"interface/index.html",{
        "description": AboutMe.objects.all(),"experience":Experience.objects.all(),'education':Education.objects.all(),'skill':Skill.objects.all(),"socialLink":SocialLink.objects.all(),"project":Projects.objects.all()})
