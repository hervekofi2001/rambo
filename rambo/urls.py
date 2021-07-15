
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from tchat.views import home,detail, itineraire,search,contact,maintenance
from tchat.views import reflecto,login,chatmaps,loginmesure,mesurer, rapport

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reflecto/', reflecto,name="reflecto"),
    path('home/',home, name="home"), 
    path('article/<int:id_article>',detail,name ="detail"),
    path('home/article/recherche',search,name ="search"),
    path('contact/',contact,name ="contact"),
    path('mesurer/',mesurer,name ="mesurer"),
    path('maintenance/',maintenance,name ="maintenance"),
    path('login/',login,name ="login"),
    path('loginmesure/',loginmesure,name ="loginmesure"),
    path('chatmaps/',chatmaps,name ="chatmaps"),
    path('my-admin/',include("app_admin.urls")), 
    path('itineraire/',itineraire,name ="itineraire"),
    path('rapport/<int:id_mesure>',rapport,name ="rapport"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 