from django.shortcuts import render

# Create your views here.

def django(request):
    return render(request, 'ex01/content.html', {
        'title': 'Ex01 : Django, framework web.',
        'stylesheet': 'ex01/style1.css',
        'iframe_src': 'https://tutorial.djangogirls.org/en/django/'}
    )

def affichage(request):
    return render(request, 'ex01/content.html', {
        'title': 'Ex01 : Processus d’affichage d’une page statique.',
        'stylesheet': 'ex01/style1.css',
        'iframe_src': 'https://medium.com/faun/dynamic-website-with-django-55db56c1068a'}
    )

def templates(request):
    return render(request, 'ex01/content.html', {
        'title': 'Ex01 : Moteur de templates.',
        'stylesheet': 'ex01/style2.css',
        'iframe_src': 'https://tutorial.djangogirls.org/en/django_templates/'}
    )