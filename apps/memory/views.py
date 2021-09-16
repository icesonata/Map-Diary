import folium
from folium.plugins import MousePosition

from django.urls import reverse_lazy

from django.contrib.gis.geos import Point
from django.views.generic import CreateView, DetailView

from .models import Memory
from .forms import MemoryCreateForm

# https://colab.research.google.com/github/giswqs/qgis-earthengine-examples/blob/master/Folium/ee-api-folium-setup.ipynb
basemap = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    )
}

class MemoryCreate(CreateView):
    model = Memory
    template_name = 'memory/create.html'
    form_class = MemoryCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Assign user obj to every new memory obj as fk
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)

def get_geo_location(memory):
    # Get location coordinates
    points = list((memory.location.coords))
    # Reverse latitude with longtitude of the location,
    # the reason is because folium stores coordinates in opposite order,
    # i.e., folium stores in db as (long,lat) instead of (lat,long) 
    return points[::-1]


class MemoryDetail(DetailView):
    model = Memory
    template_name = 'memory/detail.html'

    # Check if user has permission to view the event 
    # in case of memory getting seen by other users 
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, *kwargs)
        mem_id = self.kwargs.get('pk')
        usr = self.request.user
        if len(Memory.objects.filter(author=usr, id=mem_id)) == 0:
            return qs.none()
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        points = get_geo_location(context['memory'])
        
        # Display map using folium
        geomap = folium.Map(location=points, zoom_start=10)
        
        # Mark locations on the map
        folium.Marker(location=points).add_to(geomap)
        
        # Display Google Maps
        basemap['Google Maps'].add_to(geomap)

        # Decorate with small handy widget
        # https://www.kaggle.com/subinium/how-to-use-folium-geospatial-data#plugins.MousePosition
        formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        MousePosition(
            position="topright",
            separator=" | ",
            empty_string="NaN",
            lng_first=True,
            num_digits=20,
            prefix="Coordinates:",
            lat_formatter=formatter,
            lng_formatter=formatter,
        ).add_to(geomap)

        geomap = geomap._repr_html_()
        context['map'] = geomap

        return context
