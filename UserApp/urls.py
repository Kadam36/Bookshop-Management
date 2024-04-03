from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path('ShowBooks/<id>',views.ShowBooks),
    path('ViewDetails/<id>',views.ViewDetails),
    path('Login',views.Login),
    path('SignUp',views.SignUp),
    path('SignOut',views.SignOut),
    path('addToCart',views.addToCart),
    path('showCartItems',views.showCartItems),
      path('MakePayment',views.MakePayment),
    path('thankyou',views.thankyou),
    path('myorders', views.myorders),
    
]

