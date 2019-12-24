from django.views.generic import ListView

from app.models import Serie


class LoginView(ListView):
    template_name = 'login/index.html'
    model = Serie
    # queryset = Serie.objects.filter(categorie__icontains='Action')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        # result['title'] = 'Serie à voir'
        return result
