from django.views.generic import ListView
from django.db.models import Q

from app.models import Serie

from django.template import RequestContext, Template
from django.http import HttpResponse, request


class SearchView(ListView):
    template_name = 'search.html'
    model = Serie

    #     def get_context_data(self, **kwargs):
    #         result = super(SearchView, self).get_context_data(**kwargs)
    #         result['series'] = Serie.objects.all()
    #         result['categories'] = Categorie.objects.all()
    #         return result

    def get_queryset(self):
        # if 'title' in self.kwargs:
        #     return Serie.objects.filter(title__icontains=self.kwargs['title'])
        # return Serie.objects.all()

        query = self.request.GET.get('q')
        # return Serie.objects.filter(title__icontains=query)
        object_list = Serie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return object_list
