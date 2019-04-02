from django.views.generic import FormView, ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from surdoapp.admin_side.models import SurdoWord
from surdoapp.admin_side.forms import SurdoWordForm, CreateWordsListForm


@method_decorator([login_required(login_url='/django-admin/login')], name='dispatch')
class WordListView(ListView):
    template_name = 'admin_side/words_list.html'
    model = SurdoWord

    def get_context_data(self, **kwargs):
        category = self.request.GET.get('cat')
        context = super().get_context_data(**kwargs)
        context['cat'] = category
        if category is None:
            context['words'] = SurdoWord.objects.all()
        else:
            context['words'] = SurdoWord.objects.filter(category=category)
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


@login_required(login_url='/django-admin/login')
def create_words_list(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        name_ru_list = request.POST.get('name_ru_list').split('\n')
        name_kz_list = request.POST.get('name_kz_list').split('\n')
        links_list = request.POST.get('links_list').split('\n')

        for i in range(len(name_ru_list)):
            name_ru = name_ru_list[i].strip()
            try:
                name_kz = name_kz_list[i].strip()
            except IndexError:
                continue

            link = ''
            if len(links_list) > i:
                link = links_list[i].strip()

            word = SurdoWord(category=category, name_kz=name_kz, name_ru=name_ru, video_link=link)
            word.save()

        return redirect(reverse('words_list'))

    return render(request, 'admin_side/create_words_list.html', {'form':  CreateWordsListForm()})
