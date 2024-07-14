from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    teamcontent = Team.objects.all()
    
    index ={
        'teamcontent':teamcontent,
        
    }
    return render(request,"index.html",index)
def contact(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Message = request.POST.get('message')
        formData = Contact(name = Name, email = Email, subject = Subject, message = Message)
        formData.save()
    return render (request,"contact.html")
def about(request):
    TestimonialContent = Testimonial.objects.all()
    context ={
       
        'TestimonialContent':TestimonialContent
    }
    return render(request,"about.html",context)
def index2(request):
    return render(request,"index-2.html")
def service(request):
    return render(request,"services.html")
def team(request):
    team = Team.objects.all()
    context = {
        'team' : team,
    }
    return render(request,"team.html",context)
def portfolio(request):
    return render(request,"portfolio.html")
def blog(request):
    return render(request,"blog.html")