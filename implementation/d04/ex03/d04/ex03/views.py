from django.shortcuts import render

# Create your views here.
def ex03(request):
    return render(request, 'ex03/index.html', {'rows': range(0, 255, 5)})