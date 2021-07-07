"""rambo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from tchat.views import home,detail, itineraire,search,contact,maintenance
from tchat.views import reflecto,login,chatmaps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reflecto/', reflecto,name="reflecto"),
    path('home/',home, name="home"), 
    path('article/<int:id_article>',detail,name ="detail"),
    path('home/article/recherche',search,name ="search"),
    path('contact/',contact,name ="contact"),
    path('maintenance/',maintenance,name ="maintenance"),
    path('login/',login,name ="login"),
    path('chatmaps/',chatmaps,name ="chatmaps"),
    path('my-admin/',include("app_admin.urls")), 
    path('itineraire/',itineraire,name ="itineraire"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 