from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

urlpatterns=[
    path('',views.index,name='index'),
    path('registeruser/',views.registeruser,name='registeruser'),
	
]
