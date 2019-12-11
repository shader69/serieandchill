from django.contrib import admin

# Register your models here.
from app.models import Serie
from app.models import Categorie
from app.models import Nationalite

admin.site.register(Serie)
admin.site.register(Categorie)
admin.site.register(Nationalite)
