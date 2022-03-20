from django.urls import path
from  .import views


urlpatterns = [
    path('createpost/', views.createpost, name='createpost'),
    path('createcontact/', views.createcontact, name='createcontact'),
    path('contacts/', views.contacts, name='contacts'),


]