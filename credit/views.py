from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from . import forms
from .forms import ContactForm
from .models import Kategoriya, Tolov, Tovar, Xaridor,Users_Message


# Create your views here.
class homepageview(TemplateView):
    template_name = 'home.html'

class AdminPanelView(LoginRequiredMixin,ListView):
    model = Xaridor
    template_name = 'dashboard.html'
    login_url = 'login'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context    


class BarchaXaridorlarView(LoginRequiredMixin,ListView):
    model = Xaridor
    template_name = 'BarchaXaridorlar.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class XaridorCreateView(LoginRequiredMixin,CreateView):
    model = Xaridor
    template_name = 'xaridorqoshish.html'
    fields = ['ism','familiya','OtasiningIsmi','manzil','pasportSeriyaRaqami','telefon','rasm','tovarKategoriyasi','tanlanganTovar','muddat',]
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class XaridorXaqida(LoginRequiredMixin,DetailView):
    model = Xaridor
    template_name = 'XaridorXaqida.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class XaridorUpdateView(LoginRequiredMixin,UpdateView):
    model = Xaridor
    template_name = 'XaridorTahrirlash.html'
    fields = ['ism','familiya','OtasiningIsmi','manzil','pasportSeriyaRaqami','telefon','rasm','tovarKategoriyasi','tanlanganTovar','muddat',]
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class XaridorDeleteView(LoginRequiredMixin,DeleteView):
    model = Xaridor
    template_name = 'XaridorDelete.html'
    success_url = reverse_lazy('BarchaXaridorlar')
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class KategoriyalarView(LoginRequiredMixin,ListView):
    model = Kategoriya
    template_name = 'Kategoriyalar.html'
    login_url = 'login'
    context_object_name = 'kategoriya'

class KategoriyaDeleteView(LoginRequiredMixin,DeleteView):
    model = Kategoriya
    template_name = 'KategoriyaDelete.html'
    success_url = reverse_lazy('Kategoriyalar')
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class KategoriyaUpdateView(LoginRequiredMixin,UpdateView):
    model = Kategoriya
    template_name = 'KategoriyaTahrirlash.html'
    fields = ['nomi']
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class CreateCategory(LoginRequiredMixin,CreateView):
    model = Kategoriya
    template_name = 'Kategoriyaqoshish.html'
    fields = ['nomi']
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 
        
class CreateTovar(LoginRequiredMixin,CreateView):
    model = Tovar
    template_name = 'tovarqoshish.html'
    fields = ['nomi','rangi','xotirasi','narxi','rasm','category']
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class TovarXaqida(LoginRequiredMixin,DetailView):
    model = Tovar
    template_name = 'TovarXaqida.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class TovarUpdateView(LoginRequiredMixin,UpdateView):
    model = Tovar
    template_name = 'TovarTahrirlash.html'
    fields = ['nomi','narxi','rangi','xotirasi','rasm','category']
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class TovarDeleteView(LoginRequiredMixin,DeleteView):
    model = Tovar
    template_name = 'TovarDelete.html'
    success_url = reverse_lazy('adminpanel')
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class ContactCreateView(CreateView):
    model = Users_Message
    template_name = 'home.html'
    fields = ('Ism', 'Familiya', 'Telefon_raqam', 'Xabar')


class XabarPageView(LoginRequiredMixin, ListView):
    model = Users_Message
    template_name = 'xabarlar.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 
    

class CreateTolov(LoginRequiredMixin,CreateView):
    model = Tolov
    template_name = 'tolovQoshish.html'
    fields = ['xaridor','miqdori']
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 

class XisobotlarView(LoginRequiredMixin,ListView):
    model = Tolov
    template_name = 'xisobotlar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context 