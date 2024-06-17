from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class ViewCount(models.Model):
    """
    Модель для хранения IP адресов пользователей
    Необходимо для подсчета количества просмотра сайта
    """
    ip_address = models.CharField(max_length=100, verbose_name='IP адрес')

    class Meta:
        verbose_name = 'IP адрес пользователя'
        verbose_name_plural = 'IP адреса пользователей'

    def __str__(self):
        return self.ip_address


class Houses(models.Model):
    """
    Модель для хранения данных о проектах домов
    """
    name_house = models.CharField(max_length=100, verbose_name="название проекта дома",
                                  validators=[MinLengthValidator(3)])  # валидация минимальной длинны
    description = models.TextField(verbose_name="описание проекта дома")
    square = models.FloatField(verbose_name="площадь дома")
    dimensions = models.CharField(max_length=100, verbose_name="габариты дома")
    walls = models.CharField(max_length=100, verbose_name="материал стен дома дома")
    image = models.FileField(upload_to="houses_gallery/", verbose_name="картинка дома")

    class Meta:
        verbose_name = 'проект дома'
        verbose_name_plural = 'проекты домов'
        ordering = ["square"]

    def __str__(self):
        return self.name_house

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
