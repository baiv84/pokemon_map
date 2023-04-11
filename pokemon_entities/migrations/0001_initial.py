# Generated by Django 3.1.14 on 2023-04-11 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Имя (рус)')),
                ('title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя (англ)')),
                ('title_jp', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя (япон)')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография')),
                ('next_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolutions', to='pokemon_entities.pokemon', verbose_name='Эволюционирует в')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('appeared_at', models.DateTimeField(verbose_name='Время появления')),
                ('disappeared_at', models.DateTimeField(verbose_name='Время исчезновения')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Уровень развития')),
                ('health', models.IntegerField(blank=True, null=True, verbose_name='Уровень здоровья')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='Уровень силы')),
                ('defence', models.IntegerField(blank=True, null=True, verbose_name='Уровень защиты')),
                ('stamina', models.IntegerField(blank=True, null=True, verbose_name='Уровень выносливости')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Покемон')),
            ],
        ),
    ]
