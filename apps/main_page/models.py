from django.db import models
from .validators import validate_video_extension


class MainPage(models.Model):
    video = models.FileField('Только ".MOV, .avi, .mp4, .webm, .mkv" форматы поддерживаются',
                             upload_to='media/main_page_video_uploaded/%Y/%m/%d',
                             validators=[validate_video_extension])
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class Slider(models.Model):
    image = models.ImageField('Слайдер',
                              upload_to='media/slider_image/%Y/%m/%d')

    def __str__(self):
        return 'Фото {}'.format(self.id)
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'


class Worker(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField('Фото фотографа',
                              upload_to='media/photographer_image/%Y/%m/%d')
    position = models.TextField('Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
