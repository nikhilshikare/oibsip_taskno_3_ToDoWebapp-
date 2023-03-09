from django.urls import path
from todo import views


urlpatterns = [
    path('',views.home,name='home'),
    #<--------- Authentication releted path / urls start here ------->
    path('sign_in',views.Auth.sign_in,name='sign_in'),
    path('sign_out',views.Auth.sign_out,name='sign_out'),
    path('sign_up',views.Auth.sign_up,name='sign_up'),
    #<--------- Authentication releted path / urls ends here ------->
]