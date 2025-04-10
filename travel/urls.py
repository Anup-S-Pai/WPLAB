from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name="wander"
urlpatterns=[
    path('',views.index,name="homePage"),
    path('logout/',views.logoutApp,name="logoutPage"),
    path('about/',views.about,name="aboutPage"),
    path('login/',views.loginApp,name="loginPage"),
    path('register/',views.registerApp,name="registerPage"),
    path('feedback/',login_required(views.feedback),name="feedbackPage"),
    path('weather/', views.weatherForecast, name="weatherForecast"),
]