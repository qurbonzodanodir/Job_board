from django.shortcuts import render
from django.views import generic
from .models import *
from django.urls import reverse_lazy

class JobListView(generic.ListView):
    model = Job
    template_name = 'home.html'

class JobCreateView(generic.CreateView):
    model = Job
    template_name = 'create_job.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class JobUpdateView(generic.UpdateView):
    model = Job
    template_name = 'update_job.html'
    fields ='__all__'
    success_url = reverse_lazy('home')


class JobDeleteView(generic.DeleteView):
        model = Job
        template_name = 'delete_job.html'
        fields ='__all__'
        success_url = reverse_lazy('home')    



class Job_CategoryCreateView(generic.CreateView):
    model = Job_Category
    template_name = 'create_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')



class Job_CategoryUpdateView(generic.UpdateView):
    model = Job_Category
    template_name = 'update_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')





class CompanyCreateView(generic.CreateView):
    model = Company
    template_name = 'create_company.html'
    fields ='__all__'
    success_url = reverse_lazy('home')


