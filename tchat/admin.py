from django.contrib import admin
from .models import Article, Mesurer, Zone
from .models import Category
from .models import Contact,Reflecto,Adresse
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

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Reflecto)
admin.site.register(Adresse)
admin.site.register(Zone)
admin.site.register(Mesurer)









# Register your models here.
