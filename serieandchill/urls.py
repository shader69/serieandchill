"""serieandchill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from django.template import RequestContext, Template
from django.http import HttpResponse

from app.views.index import IndexView
from app.views.categorie import CategorieView
from app.views.search import SearchView
from app.views.serie import SerieView
from app.views.nationality import NationalityView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path(r'', IndexView.as_view(), name='app_index'),
    path('categorie/<str:cat>', CategorieView.as_view(), name='app_serie_categorie_title'),
    path('categorie', CategorieView.as_view(), name='app_serie_categorie'),
    path('nationality/<str:nat>', NationalityView.as_view(), name='app_serie_nationality_title'),
    path('nationality', NationalityView.as_view(), name='app_serie_nationality'),
    path('search', SearchView.as_view(), name='app_serie_search'),
    path('serie/<str:title>', SerieView.as_view(), name='app_serie_title'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
