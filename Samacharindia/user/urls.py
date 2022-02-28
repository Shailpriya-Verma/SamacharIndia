from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home),
    path('index/', views.home),
    path('', views.home),
    path('aboutus/', views.aboutus),
    path('contactus/', views.contactus),
    path('mynews/', views.mynews),
    path('video/', views.video),
    path('readmore/',views.readmore),

]