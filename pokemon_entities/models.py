from django.db import models


class Pokemon(models.Model):
    """Pokemon model"""
    title_ru = models.CharField(max_length=200, verbose_name='Имя (рус)')
    title_en = models.CharField(max_length=200, null=True,
                                blank=True, verbose_name='Имя (англ)')
    title_jp = models.CharField(max_length=200, null=True,
                                blank=True, verbose_name='Имя (япон)')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(null=True, blank=True, verbose_name='Фотография')
    next_evolution = models.ForeignKey('self',
                                       on_delete=models.SET_NULL,
                                       related_name='previous_evolutions',
                                       null=True,
                                       blank=True,
                                       verbose_name='Эволюционирует в')

    def __str__(self):
        """Object text representation"""
        return self.title_ru


class PokemonEntity(models.Model):
    """Pokemon entity model"""
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                verbose_name='Покемон')
    appeared_at = models.DateTimeField(verbose_name='Время появления')
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    level = models.IntegerField(null=True, blank=True,
                                verbose_name='Уровень развития')
    health = models.IntegerField(null=True, blank=True,
                                 verbose_name='Уровень здоровья')
    strength = models.IntegerField(null=True, blank=True,
                                   verbose_name='Уровень силы')
    defence = models.IntegerField(null=True, blank=True,
                                  verbose_name='Уровень защиты')
    stamina = models.IntegerField(null=True, blank=True,
                                  verbose_name='Уровень выносливости')

    def __str__(self):
        """Object text representation"""
        return f'{self.pokemon}, широта - {self.lat}, долгота - {self.lon}'
