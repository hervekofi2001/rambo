from django import forms
from django.forms import fields, widgets
from .models import Article, Category, Technicien

class LoginForm(forms.Form):

    username = forms.CharField(label="Nom d'utilisateur", required=True)
    pwd = forms.CharField(label="Mot de passe", required=True, widget=forms.PasswordInput())


class ArticleForm(forms.ModelForm):        
        class Meta:
            model = Article
            exclude = ('created_at','updated_at')
            fields = ['title','category','descrp','image']
            labels= {'title':'Titre','category':'Categorie','descrp':'Description'}
            widgets={
                'title': forms.TextInput(attrs={'class':'form-control'}),
                'category': forms.Select(attrs={'class':'form-control'}),  
                'descrp': forms.Textarea(attrs={'class':'form-control','rows':500}), 
            }

class TechForm(forms.ModelForm):        
        class Meta:
            model = Technicien
            exclude = ('motdepass','date')
            fields = ['nom','prenoms','email','statut','date']
            widgets={
                'nom': forms.TextInput(attrs={'class':'form-control'}),
                'prenoms': forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'statut': forms.NullBooleanSelect(attrs={'class':'form-control'}),  
          
            }
    
        