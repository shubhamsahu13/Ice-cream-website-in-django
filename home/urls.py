from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Shubham Ice creams Admin"
admin.site.site_title = "Shubham Ice creams Admin Portal"
admin.site.index_title = "Welcome to Shubham Ice creams"

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services')
]
