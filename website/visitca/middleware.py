from . import models


class ViewsCounter:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_client_ip(request) -> str:
        """
        Метод для получения апи пользователя
        :param request:
        :return: ip
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')  # В REMOTE_ADDR значение апи пользователя
        return ip

    def __call__(self, request):
        response = self.get_response(request)

        user_ip = self.get_client_ip(request=request)  # получаем апи пользователя
        models.ViewCount.objects.get_or_create(
            ip_address=user_ip)  # добавляем апи пользователя в модель, если ее там нет

        return response


if __name__ == "__main__":
    pass
