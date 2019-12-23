from django.views.generic import ListView
from app.models import Serie


class SerieView(ListView):
    template_name = 'serie.html'
    model = Serie

    # def get_context_data(self, **kwargs):
    #     result = super(SearchView, self).get_context_data(**kwargs)
    #     result['series'] = Serie.objects.all()
    #     return result

    def get_queryset(self):
        if 'title' in self.kwargs:
            return Serie.objects.filter(title__icontains=self.kwargs['title'])
        return Serie.objects.all()

        # query = self.request.GET.get('content')
        # object_list = Serie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        # return object_list

