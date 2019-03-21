from django.db import models


class SurdoWord(models.Model):
    TIME, NATION = range(0, 2)
    CATEGORIES = ((TIME, 'time'), (NATION, 'nation'),)

    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORIES)
    video_link = models.CharField(max_length=255)

    def update(self, data):
        instance = SurdoWord.objects.get(id=self.id)
        instance.name = data.get('name')
        instance.category = data.get('category')
        instance.video_link = data.get('video_link')
        instance.save()

