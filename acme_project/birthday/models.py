# birthday/models.py
from django.db import models
from django.urls import reverse
from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', help_text='Необязательное поле',
        max_length=20,
        blank=True
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField(
        'Фото',
        upload_to='birthdays_images',
        blank=True
    )

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})
