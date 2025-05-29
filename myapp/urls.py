from django.contrib import admin
from django.urls import path
from myapp import views
admin.site.site_header = "Ice Cream Admin"
admin.site.site_title = "Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Ice Cream Shop"

urlpatterns = [
    path("",views.index, name='myapp'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),

]
