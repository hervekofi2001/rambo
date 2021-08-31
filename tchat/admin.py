from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model
from .models import (
    Category, Contact,Reflecto,Adresse, Article, Mesurer, Zone,
    Utilisateur
)
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Admin Stockage mesure')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Administration Stockage mesure')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()

admin.site.site_header = 'Administration Stockage mesure'
admin.site.change_list_template = 'admin/base_site.html'



#User = get_user_model()

#class Utilisateur(User):

   # is_client = models.BooleanField(default=False)
   # is_technicien = models.BooleanField(default=False)
   # is_partenaire = models.BooleanField(default=False)
    
  #  class Meta:

      #  verbose_name="utilisateur"
      #  verbose_name_plural="Utilisateurs"


    
class AdresseAdmin(admin.ModelAdmin):

    list_display   = ('lat', 'lng', 'zone','date')
   

    date_hierarchy = 'date'
    ordering       = ('zone','date')
    search_fields  = ('lng', 'lat')




class ArticleAdmin(admin.ModelAdmin):

    list_display   = ('title', 'created_at', 'updated_at')
    list_filter    = ('title', 'category')
    date_hierarchy = 'created_at'
    ordering       = ('title','created_at')
    search_fields  = ('title', 'descrp')


class ContactAdmin(admin.ModelAdmin):

    list_display   = ('nom', 'prenom', 'localisation','gps')
    list_filter    = ('nom', 'prenom','localisation')
    date_hierarchy = 'date'
    ordering       = ('date')
    search_fields  = ('nom', 'localisation')


class MesurerAdmin(admin.ModelAdmin):

    ist_display   = ('NumFiber', 'PerteConnecteur', 'CumuleConnecteur','PerteDistance','CumuleDistance','BilanPertes',' LongueurCable','Episure','rapport')
    list_filter    = ('NumFiber','date')
    date_hierarchy = 'date'
    ordering       = ('NumFiber','date')
    search_fields  = ('NumFiber','date')





admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Contact,)
admin.site.register(Adresse,AdresseAdmin)
admin.site.register(Zone)
admin.site.register(Mesurer,MesurerAdmin)
admin.site.register(Utilisateur)







