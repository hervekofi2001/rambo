from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import fields
from django.db.models.fields import NullBooleanField



User = get_user_model()

class Utilisateur(User):

    is_client = models.BooleanField(default=False)
    is_technicien = models.BooleanField(default=False)
    is_partenaire = models.BooleanField(default=False)
    
    class Meta:

        verbose_name="utilisateur"
        verbose_name_plural="Utilisateurs"



class Category(models.Model):
    name =models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Adresse(models.Model):
    lat=models.CharField(max_length=200, default=0)
    lng=models.CharField(max_length=200, default=0)
    zone = models.ForeignKey("Zone", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
 

class Zone(models.Model):
    zone = models.CharField(max_length=50, null= True)
    
    def __str__(self):
        return self.zone
    
class Article(models.Model):

    title=models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    descrp = models.TextField()
    image = models.ImageField(null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    


class Contact(models.Model):

    nom=models.CharField(max_length=50)
    prenoms=models.CharField(max_length=50)
    email=models.EmailField()
    motdepass=models.CharField(max_length=8)
    localisation=models.CharField(max_length=50)
    gps=models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, null=True, blank=True, editable=False)

class Technicien(models.Model):
    nom=models.CharField(max_length=50)
    prenoms=models.CharField(max_length=50)
    email=models.EmailField()
    motdepass=models.CharField(max_length=8)
    statut = models.CharField(max_length=50, null= True)
    date = models.DateField(auto_now_add=True, null=True, blank=True, editable=False)


    def __str__(self):
        return self.nom

class Mesurer(models.Model):

    NumFiber=models.CharField(max_length=5)
    PerteConnecteur=models.CharField(max_length=50)
    CumuleConnecteur=models.CharField(max_length = 50)
    PerteDistance=models.CharField(max_length=50)
    CumuleDistance=models.CharField(max_length = 50)
    BilanPertes=models.CharField(max_length = 50)
    LongueurCable=models.CharField(max_length = 50)
    Episure=models.CharField(max_length = 50)
    rapport = models.CharField(max_length = 255, blank=True, editable=False)
    date = models.DateField(auto_now_add=True, null=True, blank=True, editable=False)

    def __str__(self):
        return self.NumFiber

class Reflecto(models.Model):
    
    NumFiber=models.CharField(max_length=5)
    PerteConnecteur=models.CharField(max_length=50)
    CumuleConnecteur=models.CharField(max_length = 50)
    PerteDistance=models.CharField(max_length=50)
    CumuleDistance=models.CharField(max_length = 50)
    BilanPertes=models.CharField(max_length = 50)
    LongueurCable=models.CharField(max_length = 50)
    Episure=models.CharField(max_length = 50)
    photo = models.ImageField(null = True)

    def __str__(self):
        return self.NumFiber


    