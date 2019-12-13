from django.views.generic import ListView

from app.models import Serie


class IndexView(ListView):
    template_name = 'index.html'
    model = Serie

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        # result['title'] = 'Serie à voir'
        return result
