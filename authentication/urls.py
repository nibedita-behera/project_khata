from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views
from .views import RegistrationView,userNameValidation,LogoutView

urlpatterns=[
    path('login', views.user_login, name='login'),
    path('registration', RegistrationView.as_view(),name='registration'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('validate-username',csrf_exempt(userNameValidation.as_view()),name='validate-username'),

]
