from django.http import Http404
from django.shortcuts import render

posts = [
    {
        'id': 1,
        'title': 'Лунный свет',
        'location': 'Нью-Йорк',
        'date': '11.11.2021',
        'text': 'Полный текст первого поста.',
        'author': 'Автор 1',
        'category': 'personal',
    },
    {
        'id': 2,
        'title': 'Путешествие',
        'location': 'Париж',
        'date': '12.11.2021',
        'text': 'Полный текст второго поста.',
        'author': 'Автор 2',
        'category': 'travel',
    },
    {
        'id': 3,
        'title': 'Работа',
        'location': 'Берлин',
        'date': '13.11.2021',
        'text': 'Полный текст третьего поста.',
        'author': 'Автор 3',
        'category': 'work',
    },
]


def index(request):
    return render(request, 'blog/index.html', {'post': posts})


def post_detail(request, id):
    for post in posts:
        if post['id'] == id:
            return render(request, 'blog/detail.html', {'post': post})
    raise Http404('Пост не найден')


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {'post': category_slug})
