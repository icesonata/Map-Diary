import floppyforms.__future__ as forms
from .models import Memory

# https://django-floppyforms.readthedocs.io/en/latest/geodjango.html
class PointWidget(forms.gis.PointWidget, forms.gis.BaseGMapWidget):
        google_maps_api_key = 'AIzaSyA4nphBk8bIaoTXcK87fiKwlmbBhyW8_Fk'

class MemoryCreateForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['name', 'comment', 'location']
        widgets = {
            'location': PointWidget(attrs={
                'map_width': 450,
                'map_height': 450,
            }),
        }