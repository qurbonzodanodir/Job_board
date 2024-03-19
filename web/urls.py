from django.urls import path
from .views import *

urlpatterns = [
    path('',JobListView.as_view(),name='home'),
    path('create_category',Job_CategoryCreateView.as_view(),name='create_category'),
    path('create_company',CompanyCreateView.as_view(),name='create_company'),
    path('create_job',JobCreateView.as_view(),name='create_job'),
    path('update_job/<int:pk>/',JobUpdateView.as_view(),name='update_job'),
    path('delete_job/<int:pk>/',JobDeleteView.as_view(),name='delete_job'),
    path('update_category/<int:pk>/',Job_CategoryUpdateView.as_view(),name='update_category'),



    

]
