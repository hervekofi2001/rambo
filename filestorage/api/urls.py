from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import File

# Serializers define the API representation.
class DocSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

# ViewSets define the view behavior.
class DocViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = DocSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'files', DocViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

from django.shortcuts import render

def read_file(req, id) :
    try:
        src = File.objects.get(pk = id).file.name[7:]
    except:
        HttpResponse("Inexistant. Vérifiez que le reflecto ait bien envoyé le rapport")    
    return render(req, 'send_file.html', { 'src': src } )

urlpatterns = [
    path('', include(router.urls)),
    path('read/<int:id>', read_file )
]