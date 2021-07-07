from django.db import models
import geocoder 

class Category(models.Model):
    name =models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Adresse(models.Model):
    lat=models.CharField(max_length=200, default=0)
    lng=models.CharField(max_length=200, default=0)
    date = models.DateTimeField(auto_now=True)

    zone = models.ForeignKey("Zone", on_delete=models.CASCADE)

class Zone(models.Model):
    zone = models.CharField(max_length=50, null= True)

    def __str__(self):
        return self.zone
    
class Article(models.Model):
    title=models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    descrp = models.TextField()
    image = models.ImageField()
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

    def __str__(self):
        return self.nom

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


    
# Create your models here.
