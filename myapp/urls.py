from django.contrib import admin
from django.urls import path
from myapp import views
admin.site.site_header = "Ice Cream Admin"
admin.site.site_title = "Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Ice Cream Shop"

urlpatterns = [
    path('', views.signin, name='signin'), 
    path("home",views.search_flavours, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("signin",views.signin, name='signin'),
    path('login/', views.user_login, name='login'), 
    path("logout",views.logout_view, name='logout'),

]
