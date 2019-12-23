from django.views.generic import ListView

from app.models import Serie, Nationalite


class NationalityView(ListView):
    template_name = 'nationality.html'
    model = Nationalite

    def get_context_data(self, **kwargs):
        result = super(NationalityView, self).get_context_data(**kwargs)
        result['series'] = Serie.objects.all()
        result['nationalities'] = Nationalite.objects.all()
        return result

    def get_queryset(self):
        if 'nat' in self.kwargs:
            object_list = Serie.objects.filter(nationalite__name=self.kwargs['nat'])
        else:
            object_list = Serie.objects.all()
        return object_list
