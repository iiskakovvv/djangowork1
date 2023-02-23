from django.db import models
from datetime import datetime

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    msg = models.TextField()
    dateTime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'Вы получили сообщение от {self.name} "{self.email}"'


    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'