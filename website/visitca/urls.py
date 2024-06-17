from django.urls import path
from . import views

app_name = 'visitca'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # просмотр главной страницы
    path('list_houses/', views.ListHouses.as_view(), name='list_houses'),  # просмотр всех домов
    path('detail_houses/<int:pk>', views.DetailHouse.as_view(), name='detail_house'),  # просмотр одного дома
    path('update_house/<int:pk>', views.UpdateHouse.as_view(), name='update_house'),  # изменение проекта дома
    path('delete_house/<int:pk>', views.DeleteHouse.as_view(), name='delete_house'),  # удаление проекта дома
    path('create_houses/', views.CreateHouse.as_view(), name='create_houses'),  # добавить в БД новый проект дома
    path('register/', views.RegisterUser.as_view(), name='register'),  # регистрация
    path('login/', views.LoginUser.as_view(), name='login'),  # аутентификация
    path('logout/', views.LogoutUser.as_view(), name='logout'),  # выход из приложения

]
