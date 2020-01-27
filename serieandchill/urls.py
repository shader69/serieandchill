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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from app.views.index import IndexView
from app.views.login import LoggedView
from app.views.registration import create_user as SignupView
from app.views.registration import edit_password as PasswordchangeView
from app.views.registration import edit_profile as ProfilechangeView
from app.views.category import CategorieView
from app.views.search import SearchView
from app.views.serie import SerieView, create_serie as CreateserieView, create_comment as CreatecommentView
from app.views.nationality import NationalityView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    # path('login/', auth_views.LoginView, {'template_name': 'registration/login.html'}, name='login'),
    # path('logout/', auth_views.LogoutView, name='logout'),
]

urlpatterns += i18n_patterns(
    path(r'', IndexView.as_view(), name='app_index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/home', LoggedView.as_view(), name='home'),
    path('accounts/signup/', SignupView, name='signup'),
    # path('accounts/password_change', PasswordchangeView, name='edit_password'),
    # path('password/', PasswordchangeView, name='edit_password'),
    path('accounts/profile_change', ProfilechangeView, name='edit_profile'),

    path('category/<str:cat>', CategorieView.as_view(), name='app_serie_categorie_title'),
    path('category', CategorieView.as_view(), name='app_serie_categorie'),
    path('nationality/<str:nat>', NationalityView.as_view(), name='app_serie_nationality_title'),
    path('nationality', NationalityView.as_view(), name='app_serie_nationality'),
    path('search', SearchView.as_view(), name='app_serie_search'),
    path('serie/<str:title>', SerieView.as_view(), name='app_serie_title'),
    path('createserie', CreateserieView, name='app_serie_create'),
    path('createcomment', CreatecommentView, name='app_comment_create'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
