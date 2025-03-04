from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
]

urlpatterns += staticfiles_urlpatterns()