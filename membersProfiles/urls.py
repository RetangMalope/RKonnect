from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.membersAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
]
