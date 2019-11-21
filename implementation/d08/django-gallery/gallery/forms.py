from django.forms import ModelForm
from gallery.models import GalleryModel

class GalleryForm(ModelForm):
     class Meta:
        model = GalleryModel
        fields = ['image', 'title']