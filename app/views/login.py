from django.views.generic import TemplateView


class LoggedView(TemplateView):
    template_name = 'registration/homepage.html'

    def get_context_data(self, **kwargs):
        result = super(LoggedView, self).get_context_data(**kwargs)
        return result
