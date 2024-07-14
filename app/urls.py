from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('about',views.about,name='about.html'),
    path('blog',views.blog,name='blog.html'),
    path('contact',views.contact,name='contact.html'),
    path('index-2',views.index2,name='index-2.html'),
    path('portfolio',views.portfolio,name='portfolio.html'),
    path('team',views.team,name='team.html'),
    path('service',views.service,name='services.html'),
]
