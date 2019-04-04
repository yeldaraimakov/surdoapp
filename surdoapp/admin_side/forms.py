from django import forms

from .models import SurdoWord


class SurdoWordForm(forms.ModelForm):
    initial_fields = ['name_ru', 'name_kz', 'category', 'video_link_ru', 'video_link_kz', ]

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial')
        self.word = kwargs.get('initial').get('word')
        for key in self.initial_fields:
            if hasattr(self.word, key):
                initial[key] = initial.get(key) or getattr(self.word, key)
        kwargs['initial'] = initial
        super(SurdoWordForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SurdoWord
        fields = ['name_ru', 'name_kz', 'category', 'video_link_ru', 'video_link_kz', ]


class CreateWordsListForm(forms.Form):
    category = forms.ChoiceField(label='Категория', choices=SurdoWord.CATEGORIES)
    name_ru_list = forms.CharField(label='Наименование (рус)', widget=forms.Textarea)
    name_kz_list = forms.CharField(label='Наименование (каз)', widget=forms.Textarea)
    links_ru_list = forms.CharField(label='Ссылка на ютуб (рус)', widget=forms.Textarea, required=False)
    links_kz_list = forms.CharField(label='Ссылка на ютуб (каз)', widget=forms.Textarea, required=False)
