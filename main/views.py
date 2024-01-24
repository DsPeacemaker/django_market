from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    """в request попадает экземпляр класса http.request
    который содержит все данные о запросе
    вся возможнач информация о запросе попадает в этот параметр
    POST, GET, какой пользователей и тд
    """
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст на странице о нас',
    }
    return render(request, 'main/about.html', context)
