
from django.contrib.messages.api import error, success
from django.db import router
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib import admin, messages
from .models import Article, Category, Technicien, Utilisateur
from .models import Contact,Mesurer,Reflecto, User
from django.contrib.auth.models import User
from .models import Reflecto
from .models import Adresse,Zone
from django.http import HttpResponse, request
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms
import os

from .forms import LoginForm
from.forms import ArticleForm,TechForm



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
   #QuerySet.delete()
   return render(request,"search.html",{"list_article":list_article})

def maintenance(request):
       return render(request,"maintenance.html")

def render_map(request):
       adresses = Adresse.objects.all()
       #creation d'un objet map
       points = None
       #la liste des coordonnées
       if adresses :
              points = [ [ float(pt.lat), float(pt.lng) ] for pt in adresses ]
              
       zones = Zone.objects.all()
       print("ZONES ", zones)
       context ={
              "points":points,
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
              adresses.lat = lat
              adresses.zone = Zone.objects.get(id=int(zone))
              adresses.save()
              return redirect("chatmaps")

              
              
def itineraire(request):
       ptdepart = [ 5.320371637795692, -4.012542557526034]
       ptarrivé =  [5.3444608, -4.0173568]
       gps = Contact.objects.last().gps
       print(gps)
       if gps:
              ptarrivé = gps.split(";")
              ptarrivé  = [ float(i) for i in ptarrivé ]
              print("OUVEAU ", ptarrivé, type(ptarrivé))
       context = {
          "depart": ptdepart,
          "arrivee": list(ptarrivé)
       }
       print(context)
       return render(request,"itineraire.html", context)

""" def login(request):

       if request.method== "POST":
              username=request.POST['username']
              pwd =request.POST["pwd"]
              acteur =request.POST["choix"]
              print(acteur)
              print('le nom est:',username)
              user = authenticate(username=username,password=pwd,choix =acteur)
              if user is not None:
                     
                     return redirect("home") 
              else:
                     messages.error(request,"erreur d'authentification")
                     render(request,"login.html")

       return render(request,"login.html") """

def loginmesure(request):
       if request.method== "POST":
              username=request.POST['username']
              pwd =request.POST["pwd"]
              print('le nom est:',username)
              user = authenticate(username=username,password=pwd)
              if user is not None:
                     return redirect("reflecto")
              else:
                     messages.error(request,"erreur d'authentification")
                     render(request,"loginmesure.html")
       return render(request,"loginmesure.html")


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
       liste_mesures=Mesurer.objects.all()
       context = {"liste_mesures":liste_mesures}
       return render(request,"reflecto.html",context)
 
def rapport(request, id_mesure):
       nom = Mesurer.objects.get(pk= id_mesure).rapport
       return render(request,"rapport.html", {"url":  'rapport/'+nom} )

def handle_uploaded_file(f):  

    import os
    print("\n\n")
    os.system("ls ")  
    with open('static/rapport/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 

def mesurer(request):
       if request.method=="POST":
          print(request.POST)
          mesurer = Mesurer()
          NumFiber=request.POST.get('NumFib')
          PerteConnecteur=request.POST.get('PerteConnecteur')
          CumuleConnecteur=request.POST.get('CumuleConnecteur')
          PerteDistance=request.POST.get('PerteDistance')
          CumuleDistance=request.POST.get('CumuleDistance')
          BilanPerte= request.POST.get('BilanPerte')
          LongueurCable= request.POST.get('LongueurCable')
          Episure= request.POST.get('Episure')
          Rapport = request.FILES.get('rapport')
          handle_uploaded_file(Rapport)
          mesurer.NumFiber = NumFiber
          mesurer.PerteConnecteur=PerteConnecteur
          mesurer.CumuleConnecteur=CumuleConnecteur
          mesurer.PerteDistance = PerteDistance
          mesurer.Episure= Episure
          mesurer.LongueurCable=LongueurCable
          mesurer.BilanPertes=BilanPerte
          mesurer.CumuleDistance=CumuleDistance
          mesurer.rapport=Rapport.name
          mesurer.save()
         

       return render(request,"mesurer.html")

       
def LoginView(request):
        
       if request.POST:
              form = LoginForm(request.POST)
              if form.is_valid():
                     username = form.cleaned_data.get('username')
                     pwd = form.cleaned_data.get('pwd')
                     user = authenticate(username= username, password= pwd )
                     if user:
                            login(request, user)
                            # vérifications

                            if user.is_superuser :
                                   return redirect("dashbord")

                            return redirect('home')
                     else:
                           
                            messages.add_message(request, messages.ERROR, 'Over 9000!',extra_tags='nom utulisateur ou mot de passe incorrecte!')
       return render(request, "login.html")

def LogoutView(request):

       logout(request)
       return redirect('/')




def adminView1(request):
       
       mesures= Mesurer.objects.all()
       context = {"liste_mesures":mesures}
       return render(request,'pageadmin.html',context)

def adminView2(request): 
       contacts = Contact.objects.all()
       context= {"contacts" :contacts}
       return render(request,"pageadmin2.html",context)

def adminView3(request):
       articles = Article.objects.all()
       context= {"articles" : articles }
       utilisateur = User.objects.first()
       return render(request,'pageadmin3.html',context)

def adminView4(request):
       techniciens = Technicien.objects.all()
       context= {"techniciens" : techniciens }
       return render(request,'pageadmin4.html',context)

class ajouterArticle(CreateView):
       model=Article
       form_class=ArticleForm
       template_name="ajouter_article.html"
       success_url= "pageadmin3"

       def form_valid(self, form):
              self.Article = form.save()
              messages.success(self.request,
              "Votre profil a été mis à jour avec succès.") 
              return redirect('/pageadmin3')

class CreaTech(CreateView):
       model=Technicien
       form_class=TechForm
       template_name="technicien.html"
       success_url= "technicien"

       def form_valid(self, form):
              self.Technicien = form.save()
              messages.success(self.request,
              "Votre profil a été mis à jour avec succès.") 
              return redirect('/creer_technicien')



def supprimerArticle(request,id_article):
       id = id_article
       article =  Article.objects.get(id=id_article)
       article.delete()
       return redirect('/pageadmin3')


class modifierArticle(UpdateView):
       model=Article
       template_name="modifier_Article.html"
       success_url= "pageadmin3"
       fields = ['title','category','descrp','image']

       def form_valid(self, form):
              self.Article = form.save()
              messages.success(self.request,
              "Votre profil a été mis à jour avec succès.") 
              return redirect('/pageadmin3')

  

def visuel(request):
        
       return render(request, "statistique.html")

def dashbord(request):
       client=Contact.objects.all().count()
       technicien =Technicien.objects.all().count()
       mesure = Mesurer.objects.all().count()
       article =Article.objects.all().count()
       adresse =Adresse.objects.all().count()
       context = { 'client':client,'mesure':mesure,'technicien':technicien, 'article':article,'adresse':adresse}
       return render(request, "dashbord.html",context)

       #def testadmin(request,id):
              #id=id
              #articles=Article.objects.get(id=id)
              #articles.delete()


