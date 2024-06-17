"""
Необходимые утилиты
"""
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse


class AuthenticatedMixin:
    """
    С помощью метода dispatch проверяем аутентификацию пользователя.
    Если пользователь не аутентифицирован, то перенаправляем его на страницу аутентификации
          HttpResponseRedirect(reverse('visitca:login')),
    Если пользователь аутентифицирован, то ничего не выполняем
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('visitca:login'))
        return super(AuthenticatedMixin, self).dispatch(request, *args, **kwargs)


class DataMixin:
    """
    Передаем необходимый контент
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_count'] = len(models.ViewCount.objects.all())
        return context
