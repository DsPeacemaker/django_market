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
        'text_on_page': 'Наша продукция готовится исключительно из натуральных продуктов без использования красителей, ароматизаторов и усилителей вкуса. Поэтому вкус изделий из пекарни Колобок — это вкус настоящей домашней выпечки.'
        + ' Мы вкладываем душу в нашу работу, используя только лучшие ингредиенты, потому что все, что мы делаем, мы делаем с любовью. Порадуйте себя, своих родных и близких, ведь вы дарите не только вкусную и натуральную выпечку ؘ– вы дарите здоровье, радость и любовь.',
        'title_image_text': 'Наша выпечка самая вкусная!',
        'title_image_description': 'Пальчики оближешь!'
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