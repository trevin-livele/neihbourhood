from django.urls import path
from  .import views


urlpatterns = [
    path('createpost/', views.createpost, name='createpost'),
    path('createcontact/', views.createcontact, name='createcontact'),
    path('contacts/', views.contacts, name='contacts'),
    path('posts/', views.posts, name='posts'),
    path('createbuisiness/', views.createbuisiness, name='createbuisiness'),
    path('buisiness/', views.buisiness, name='buisiness'),
    path('addalert/', views.addalert, name='addalert'),
    path('alerts/', views.alerts, name='alerts'),






]