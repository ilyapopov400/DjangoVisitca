# Create your views here.

from . import models
from . import forms
from . import utils

from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.shortcuts import render, redirect


class Index(utils.AuthenticatedMixin, utils.DataMixin, TemplateView):
    '''
    Стартовая страница приложения
    '''

    template_name = "visitca/index.html"


class ListHouses(utils.AuthenticatedMixin, utils.DataMixin, ListView):
    """
    Просмотр всех домов
    """
    template_name = "visitca/list_houses.html"
    model = models.Houses
    context_object_name = "houses"  # переменная, передающаяся в шаблон
    # (можно использовать по дефолту object_list)


class DetailHouse(utils.AuthenticatedMixin, utils.DataMixin, DetailView):
    """
    Просмотр информации об одном доме
    """
    template_name = "visitca/detail_houses.html"
    model = models.Houses
    context_object_name = "house"  # переменная, передающаяся в шаблон
    # (можно использовать по дефолту object или название модели со строчной буквы)


class CreateHouse(utils.AuthenticatedMixin, utils.DataMixin, CreateView):
    """
    Добавить в БД новый проект дома
    """
    form_class = forms.HouseForm
    template_name = "visitca/create_house.html"
    model = models.Houses
    success_url = reverse_lazy("visitca:list_houses")


class DeleteHouse(utils.AuthenticatedMixin, utils.DataMixin, DeleteView):
    """
    Удалить проект дома
    """
    template_name = "visitca/delete_house.html"
    model = models.Houses
    success_url = reverse_lazy("visitca:list_houses")


class UpdateHouse(UpdateView):
    """
    Изменить проект дома
    """
    model = models.Houses
    form_class = forms.HouseForm
    template_name = "visitca/update_house.html"
    success_url = reverse_lazy("visitca:list_houses")


class RegisterUser(CreateView):
    '''
    Страница регистрации в приложении
    '''
    # form_class = UserCreationForm # стандартная форма для регистрации
    form_class = forms.RegisterUserForm  # собственная форма для регистрации
    template_name = "visitca/register.html"
    success_url = reverse_lazy("visitca:login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        """
        При успешной регистрации автоматически проводим аутентификацию
        и переходим на главную страницу приложения
        :param form:
        :return:
        """
        user = form.save()
        login(self.request, user)
        return redirect("visitca:index")


class LoginUser(LoginView):
    '''
    Страница аутентификации в приложении
    '''
    # form_class = AuthenticationForm  # стандартная форма для аутентификации
    form_class = forms.LoginUserForm  # собственная форма для аутентификации
    template_name = "visitca/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy("visitca:index")


class LogoutUser(LogoutView):
    """
    Выход из идентификации пользователя
    """

    # template_name = "visitca/index_for_no_register_user.html"
    def get_success_url(self):
        return reverse_lazy("visitca:index")
