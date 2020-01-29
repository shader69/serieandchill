from audioop import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from app.models import Serie, Comment
from app.forms.create_serie import SerieCreationForm
from app.forms.create_comment import CommentCreationForm


class SerieView(ListView):
    template_name = 'serie.html'
    model = Serie

    def get_context_data(self, **kwargs):
        result = super(SerieView, self).get_context_data(**kwargs)
        result['series'] = Serie.objects.all()                                              #object_list
        result['comments'] = Comment.objects.filter(serie__title=self.kwargs['title'])
        return result

    def get_queryset(self):
        if 'title' in self.kwargs:
            return Serie.objects.filter(title__icontains=self.kwargs['title'])
            # return Comment.objects.filter(serie__title=self.kwargs['title'])
        return Serie.objects.all()

        # query = self.request.GET.get('content')
        # object_list = Serie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        # return object_list


def create_serie(request):
    form = SerieCreationForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.photo = request.FILES['photo']
        form.save()

    context = {
        'form': form
    }
    return render(request, "create_serie.html", context)


def create_comment(request):
    user_id = request.user.id
    serie_id = request.GET.get('serie_id')

    if user_id != None:
        if serie_id != None:
            form = CommentCreationForm(request.POST or None,
                                       initial={'serie': serie_id,
                                                'content': 'Ecrivez un commentaire...',
                                                'rate': '1',
                                                'creator': user_id})
            if form.is_valid():
                form.save()
                #return redirect('app_serie_title', title=serie_id)
                #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                return redirect('app_index')

        else:
            return redirect('app_index')

        context = {
            'form': form
        }
        return render(request, "create_comment.html", context)
    else:
        return redirect('login')


def delete_comment(request):
    user_id = request.user.id
    comment_id = request.GET.get('comment_id')

    if user_id != None:
        if comment_id != None:
            query = Comment.objects.get(id=comment_id)
            query.delete()
            # return redirect('app_serie_nationality')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        else:
            return redirect('app_index')

    else:
        return redirect('app_index')
