
from os import name
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from tchat.views import (
        CreaTech, LogoutView, ajouterArticle,home,detail, itineraire,search,contact,maintenance,
        reflecto,chatmaps,loginmesure,mesurer, rapport, 
        LoginView,LogoutView,adminView1,adminView2,adminView3, adminView4, supprimerArticle,visuel,dashbord,modifierArticle,CreaTech
    ) 

urlpatterns = [
    path('', LoginView, name="Login_url"),
    path("logout_url", LogoutView, name="Logout_url"),
    path('admin/', admin.site.urls),
    path('reflecto/', reflecto,name="reflecto"),
    path('home/',home, name="home"), 
    path('article/<int:id_article>',detail,name ="detail"),
    path('recherche/',search,name ="search"),
    path('contact/',contact,name ="contact"),
    path('mesurer/',mesurer,name ="mesurer"),
    path('maintenance/',maintenance,name ="maintenance"),
    path('loginmesure/',loginmesure,name ="loginmesure"),
    path('chatmaps/',chatmaps,name ="chatmaps"),
    path('itineraire/',itineraire,name ="itineraire"),
    path('pageadmin1/',adminView1,name ="adminView1"),
    path('pageadmin2/',adminView2,name ="adminView2"), 
    path('pageadmin3/',adminView3,name ="adminView3"),
    path('pageadmin4/',adminView4,name ="adminView4"),
    path('ajouter_article/',ajouterArticle.as_view(),name ="ajouter_article"),
    path('creer_technicien/',CreaTech.as_view(),name ="creer_technicien"),
    path('modifier_article/<int:pk>',modifierArticle.as_view(),name ="modifier_article"),
    path('supprimer_article/<int:id_article>',supprimerArticle,name ="supprimer_article"),
    path('dashbord/',dashbord,name ="dashbord"),
    path('visuel/',visuel,name ="visuel"),  path('ajouter_article/',ajouterArticle.as_view(),name ="ajouter_article"),
    path('rapport/<int:id_mesure>',rapport,name ="rapport"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 