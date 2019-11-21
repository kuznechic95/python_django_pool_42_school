import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyForm
from .utils import Utils

# Create your views here.
utils = Utils()

def main(request):
    form = MyForm()

    return render(request, 'ex02/index.html', {
        'history': utils.get_logs(),
        'form': form
    })

def post_new(request):

    if request.method == 'POST':
        post = MyForm(request.POST)
        if post.is_valid():
            utils.write_log(request.POST.get('content'))
    return HttpResponseRedirect('/ex02')