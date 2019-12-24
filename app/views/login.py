from django.views.generic import ListView

from app.models import Serie


class LoggedView(ListView):
    template_name = 'registration/homepage.html'
    model = Serie

    def get_context_data(self, **kwargs):
        result = super(LoggedView, self).get_context_data(**kwargs)
        result['series'] = Serie.objects.all()
        return result
