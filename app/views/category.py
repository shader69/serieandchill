from django.views.generic import ListView
from app.models import Serie, Categorie


class CategorieView(ListView):
    template_name = 'category.html'
    model = Categorie

    def get_context_data(self, **kwargs):
        result = super(CategorieView, self).get_context_data(**kwargs)
        result['series'] = Serie.objects.all()
        result['categories'] = Categorie.objects.all()
        return result

    def get_queryset(self):
        if 'cat' in self.kwargs:
            object_list = Serie.objects.filter(categories__name=self.kwargs['cat'])
        else:
            object_list = Serie.objects.all()
        return object_list
