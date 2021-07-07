from django.contrib import admin
from .models import Article, Zone
from .models import Category
from .models import Contact,Reflecto,Adresse


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Reflecto)
admin.site.register(Adresse)
admin.site.register(Zone)


# Register your models here.
