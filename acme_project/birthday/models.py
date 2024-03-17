# birthday/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from .validators import real_age


User = get_user_model()


class Birthday(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=20
    )
    last_name = models.CharField(
        'Фамилия', help_text='Необязательное поле',
        max_length=20,
        blank=True
    )
    birthday = models.DateField(
        'Дата рождения',
        validators=(real_age,)
    )
    image = models.ImageField(
        'Фото',
        upload_to='birthdays_images',
        blank=True
    )
    author = models.ForeignKey(
        User, verbose_name='Автор записи',
        on_delete=models.CASCADE,
        null=True
    )

    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})


class Congratulation(models.Model):
    text = models.TextField('Текст поздравления')
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
