from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from jcoders.views import contactView, successView

urlpatterns = [
   path('', views.homepage, name='home'),
   path('home/', views.homepage, name='homepage'),
   path('kategorite/', views.kategorite, name='kategorite'),
   path('animacioni/<emri>', views.animactioni, name="animacioni"),
   path('animacioni/', views.search, name="search"),
   path('kontakti/',views.kontakti, name="kontakti"),
   path('rrethne/',views.rrethne, name="rrethne"),
   path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)