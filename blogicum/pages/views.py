from django.shortcuts import render

app_name = 'pages'


def about(request):
    return render(request, 'pages/about.html', {'title': 'О проекте'})


def rules(request):
    return render(request, 'pages/rules.html', {'title': 'Правила сайта'})
