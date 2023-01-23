from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('Ghat/', views.Ghat),
    path('About/', views.About),
    path('Videos/', views.Videos),
    path('Kashi/', views.Kashi),
    path('StudentLearning/', views.StudentLearning),
    path('Places/', views.Places),
    path('Contact/', views.Contact),
]
