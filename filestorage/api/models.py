from django.db import models

class File(models.Model) :
    file = models.FileField(upload_to = 'static/uploaded')
    created_at = models.DateField(auto_now_add = True)