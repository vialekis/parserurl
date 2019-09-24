from django.db import models
import uuid

class URLItem(models.Model):
    STATUS_JOB_SEND = 0
    STATUS_JOB_DONE = 1
    STATUS_CHOICES =[(STATUS_JOB_SEND,"отправлено, результата не знаю"),(STATUS_JOB_DONE,"выполнено"),]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    key_word = models.CharField(max_length=20)
    count_word = models.PositiveIntegerField("Количество", null=True, blank=True)
    datestamp = models.DateTimeField(verbose_name='Задача обновлена',auto_now=True)
    date_create = models.DateTimeField(verbose_name='Задача отправлена',auto_now_add=True)
    status = models.IntegerField("Статус",choices=STATUS_CHOICES, default=STATUS_JOB_SEND)

    def __str__(self):
        return self.url

    class Meta:
        ordering = ('-date_create',)
# Create your models here.
