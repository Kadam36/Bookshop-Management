from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path('ShowBooks/<id>',views.ShowBooks),
    path('ViewDetails/<id>',views.ViewDetails),
]
