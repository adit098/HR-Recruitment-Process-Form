from django.urls import path
from . import views

# TEMPLATE URLS!
app_name = 'addcandidate'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('addcandidate/', views.add_candidate, name='addcandidate'),
    path('add_candidate_submit', views.add_candidate_submit, name='add_candidate_submit'),
    path('candidatelist', views.list_candidate, name='listcandidate'),
    path('candidateview/<int:pk>', views.view_candidate, name='viewcandidate'),
    path('candidateupdate/<int:pk>', views.update_candidate, name='updatecandidate'),
    path('candidatedelete/', views.delete_candidate, name='deletecandidate'),
]