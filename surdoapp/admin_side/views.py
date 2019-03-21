from django.views.generic import FormView, ListView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from surdoapp.admin_side.models import SurdoWord
from surdoapp.admin_side.forms import SurdoWordForm


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class WordListView(ListView):
    template_name = 'admin_side/words_list.html'
    model = SurdoWord

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = SurdoWord.objects.all()
        return context


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class WordFormView(FormView):
    form_class = SurdoWordForm
    template_name = 'admin_side/word_form.html'

    def get_initial(self):
        initial = super(WordFormView, self).get_initial()
        if self.kwargs.get('id'):
            initial['word'] = get_object_or_404(SurdoWord, id=self.kwargs['id'])
        return initial

    def form_valid(self, form):
        word = self.get_initial().get('word')
        if word:
            # update word
            form.instance = get_object_or_404(SurdoWord, id=word.id)
            word.update(form.data)
        else:
            # create word
            form.save(commit=True)
        return redirect(reverse('words_list'))

    def get_context_data(self, **kwargs):
        if self.kwargs.get('id'):
            kwargs['word'] = get_object_or_404(SurdoWord, id=self.kwargs['id'])
        return super().get_context_data(**kwargs)


@login_required(login_url='/django-admin/login')
def delete_word(request, id):
    word = get_object_or_404(SurdoWord, id=id)
    word.delete()
    return redirect(reverse('words_list'))
