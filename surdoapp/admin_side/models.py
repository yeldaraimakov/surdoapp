from django.db import models


class SurdoWord(models.Model):
    TIME, ALPHABET, ACQUAINTANCE, HUMAN, FAMILY, MONTHS, DAYS, NATURE, SEASONS = range(0, 9)
    CATEGORIES = ((TIME, 'Время, календарь'), (ALPHABET, 'Алфавит'), (ACQUAINTANCE, 'Знакомство'),
                  (HUMAN, 'Человек'), (FAMILY, 'Семья'), (MONTHS, 'Названия месяцев'), (DAYS, 'Дни недели'),
                  (NATURE, 'Природа'), (SEASONS, 'Времена года'), )

    name_ru = models.CharField('Название (рус)', max_length=255)
    name_kz = models.CharField('Название (каз)', max_length=255)
    category = models.IntegerField('Категория', choices=CATEGORIES, default=TIME)
    video_link_ru = models.CharField('Ссылка на ютуб (рус)', max_length=255, blank=True, null=True)
    video_link_kz = models.CharField('Ссылка на ютуб (каз)', max_length=255, blank=True, null=True)

    def update(self, data):
        instance = SurdoWord.objects.get(id=self.id)
        instance.name = data.get('name')
        instance.category = data.get('category')
        instance.video_link_ru = data.get('video_link_ru')
        instance.video_link_kz = data.get('video_link_kz')
        instance.save()
