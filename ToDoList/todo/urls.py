from django.urls import path
from todo import views


urlpatterns = [
    path('',views.home,name='home'),
    #<--------- Authentication releted path / urls start here ------->
    path('sign_in',views.Auth.sign_in,name='sign_in'),
    path('sign_out',views.Auth.sign_out,name='sign_out'),
    path('sign_up',views.Auth.sign_up,name='sign_up'),
    #<--------- Authentication releted path / urls ends here ------->
    path('add_todo',views.TODO_LIST.add_todo,name='add_todo'),
    path('delete_id',views.TODO_LIST.delete_id,name='delete_id'),
    path('add_complete',views.TODO_LIST.add_complete,name='add_complete'),
    path('edit_todo',views.TODO_LIST.edit_todo,name='edit_todo'),
]