from django.views.generic import ListView
from app.models import Serie

from django.shortcuts import redirect
from django.utils import translation
#from django.views.generic.base import View


class IndexView(ListView):
    template_name = 'index.html'
    model = Serie
    # queryset = Serie.objects.filter(categorie__icontains='Action')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        # result['title'] = 'Serie à voir'
        return result


class ActivateLanguageView(ListView):
    language_code = ''
    redirect_to   = ''

    def get(self, request, *args, **kwargs):
        self.redirect_to   = request.META.get('HTTP_REFERER')
        self.language_code = kwargs.get('language_codex')
        translation.activate(self.language_code)
        request.session[translation.LANGUAGE_SESSION_KEY] = self.language_code
        return redirect(self.redirect_to)
