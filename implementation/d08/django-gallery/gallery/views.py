from django.shortcuts import render
from django.views.generic import DetailView, FormView,ListView
from .models import GalleryModel
from .forms import GalleryForm


class HomePageView(ListView):
    model = GalleryModel
    template_name = 'gallery/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['form'] = GalleryForm
        return context

    def post(self, request , *args , **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ImageFormViev(FormView):
    template_name = 'gallery/home.html'

    form_class = GalleryForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(ImageFormViev, self).form_valid(form)