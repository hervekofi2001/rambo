from django.db import router
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from geocoder.api import location
from pyroutelib3 import Router
from .models import Article
from .models import Contact
from .models import Reflecto
from .models import Adresse,Zone
from django.http import HttpResponse
from .chat2 import chat
from django.contrib.auth import authenticate
from django.contrib import messages
import folium
import geocoder
import os


def home(request):
   list_articles = Article.objects.all()
   context = {"list_articles":list_articles}
   return render(request,"index.html",context)


def detail(request,id_article):
       article =  Article.objects.get(id=id_article)
       category=article.category
       article_en_relation=Article.objects.filter(category=category)
       return render(request,'detail.html',{"article":article,"aer":article_en_relation})


def search(request):
   query = request.GET["article"]
   list_article=Article.objects.filter(title=query)
   return render(request,"search.html",{"list_article":list_article})

def maintenance(request):
       return render(request,"maintenance.html")

def render_map(request):
       adresses = Adresse.objects.all()
       #creation d'un objet map
       m = folium.Map(zoom_start=5,location=[19,-12])
       #la liste des coordonnées
       if adresses :
              points = [ (float(pt.lat), float(pt.lng)) for pt in adresses ]
              for pt in points :
                     folium.Marker(pt, tooltip="Click for more",popup="Abidjan").add_to(m)
              # reponse html du map
              print(points)
              folium.PolyLine(points).add_to(m)
       m = m._repr_html_()
       zones = Zone.objects.all()
       print("ZONES ", zones)
       context ={
              "m":m,
              "zones": zones
       }
       return render(request,"chatmaps.html", context)	

def chatmaps(request):
       if request.method.lower() == "get" :
              return render_map(request)
       elif request.method.lower() == "post" :
              print("ON EST DANS LE POST", request.POST)
              adresses=Adresse()
              lng=request.POST.get('longitude')
              lat=request.POST.get('latitude')
              zone=request.POST.get('zone')
              adresses.lng = lng
              adresses.lat = lng
              adresses.zone = Zone.objects.get(id=int(zone))
              adresses.save()
              return redirect("chatmaps")
              
def itineraire(request):
       m= folium.Map(location=[1.1 , 1.23], zoom_start=15)
       ptdepart = [ 50.72046, 1.61538]
       ptarrivé =  [1.1 , 1.23]
       folium.Marker(ptdepart, popup= "depart").add_to(m)
       folium.Marker(ptarrivé, popup="arrivé").add_to(m)
       m = m._repr_html_()
       context ={
              "m":m,
       }
       print("routageeeeeee!!!!!!")
       router = Router("foot")
       depart = router.findNode(ptdepart[0], ptdepart[1])
       print(depart)

       arrivé = router.findNode(ptarrivé[0], ptarrivé[1])
       print(arrivé)
      
       routeLatLons=[ptdepart,ptarrivé]
       status, route = router.doRoute(depart, arrivé)
       if status == "succes":
              print("routetrouvée")
              routeLatLons = list(map(router.nodeLatLon, route))
       else:
              print("route non trouvée")

       print(routeLatLons)
       for pt in routeLatLons:
              pt  =  list(pt)
              folium.CircleMarker(pt, radius= 3, fill = True, color  = "red").add_to(m)
   
       folium.PolyLine(routeLatLons, color="blue", weight=2.5, opacity=1).add_to(m)

       print("Le fichier HTML/CARTE est disponible")

       m.save('itineraire.html')
       return render(request,"itineraire.html", context)


def login(request):
       if request.method== "POST":
              username=request.POST['username']
              pwd =request.POST["pwd"]
              print('le nom est:',username)
              user = authenticate(username=username,password=pwd)
              if user is not None:
                     return redirect("home")
              else:
                     messages.error(request,"erreur d'authentification")
                     render(request,"login.html")
       return render(request,"login.html")

def contact(request):
   if request.method=="POST":
          print(request.POST)
          contact=Contact()
          nom=request.POST.get('nom')
          prenoms=request.POST.get('prenoms')
          email=request.POST.get('email')
          motdepass=request.POST.get('motdepass')
          localisation=request.POST.get('localisation')
          gps = request.POST.get('gps')
          contact.nom=nom
          contact.prenoms=prenoms
          contact.email=email
          contact.motdepass=motdepass
          contact.gps = gps
          contact.save()
         

   return render(request,"contact.html")

def reflecto(request):
       liste_mesures=Reflecto.objects.all()
       context = {"liste_mesures":liste_mesures}
       return render(request,"reflecto.html",context)
       

  