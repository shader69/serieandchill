from django.urls import reverse
from django.views.generic import ListView

from app.models import Serie
from app.models import Categorie


class CategorieView(ListView):
    template_name = 'categorie.html'
    model = Categorie

    # def get_success_url(self):
    #     return reverse('app_index')


    def get_context_data(self, **kwargs):
        result = super(CategorieView, self).get_context_data(**kwargs)
        result['series'] = Serie.objects.all()
        # result['categories'] = Categorie.objects.all()                    = in object_list
        return result
