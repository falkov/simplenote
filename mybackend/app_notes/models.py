from django.db import models


class NoteModel(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    body = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
