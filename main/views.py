from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request) -> HttpResponse:
    """в request попадает экземпляр класса http.request
    который содержит все данные о запросе
    вся возможнач информация о запросе попадает в этот параметр
    POST, GET, какой пользователей и тд
    """

    categories = Categories.objects.all()

    context = {
        'title': 'Пекарня Колобок - Вкус настоящего хлеба',
        'content': 'Интернет-магазин пекарни Колобок',
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'Колобок - О нас',
        'content': 'О нас',
        'text_on_page': 'Вкус настоящей домашней выпечки',
    }
    return render(request, 'main/about.html', context)

def delivery(request) -> HttpResponse:
    context = {
        'title': 'Колобок - Доставка и оплата',
        'content': 'Как мы доставляем',
        'text_on_page': 'Вкус настоящей домашней выпечки',
    }
    return render(request, 'main/delivery.html', context)

def contacts(request) -> HttpResponse:
    context = {
        'title': 'Колобок - Контакты',
        'content': 'Наши контакты',
        'text_on_page': 'Вкус настоящей домашней выпечки',
    }
    return render(request, 'main/contacts.html', context)