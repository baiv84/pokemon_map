import pytz
import folium
from django.shortcuts import render
from django.utils.timezone import localtime
from pokemon_entities.models import Pokemon
from pokemon_entities.models import PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]


DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    """Add pokemon to the map view"""
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    """Show all pokemons on the map"""
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    now_date_time = localtime(timezone=pytz.timezone("Europe/Moscow"))
    pokemons = PokemonEntity.objects.filter(appeared_at__lte=now_date_time,
                                            disappeared_at__gte=now_date_time)

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemon_url = request.build_absolute_uri(pokemon.pokemon.photo.url)
        pokemons_on_page.append(dict(pokemon_id=pokemon.pokemon.id,
                                     img_url=pokemon_url,
                                     title_ru=pokemon.pokemon.title_ru))
        add_pokemon(
                folium_map,
                pokemon.lat,
                pokemon.lon,
                pokemon_url
        )

    return render(request, 'mainpage.html', context={
                'map': folium_map._repr_html_(),
                'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    """Show pokemon with particular <pokemon_id> on the map"""
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    one_pokemon = Pokemon.objects.get(id=pokemon_id)
    one_pokemon_url = request.build_absolute_uri(one_pokemon.photo.url)
    now_date_time = localtime(timezone=pytz.timezone("Europe/Moscow"))

    pokemon_entities = one_pokemon.entities.filter(appeared_at__lte=now_date_time,
                                                   disappeared_at__gte=now_date_time)
    for entity in pokemon_entities:
        add_pokemon(
            folium_map,
            entity.lat,
            entity.lon,
            one_pokemon_url
        )

    previous_evolution = None
    next_evolution = None

    previous_pokemon = one_pokemon.previous_evolutions.first()
    next_pokemon = one_pokemon.next_evolution

    if previous_pokemon:
        previous_evolution = dict(title_ru=previous_pokemon.title_ru,
                                  pokemon_id=previous_pokemon.id,
                                  img_url=request.build_absolute_uri(previous_pokemon.photo.url))
    if next_pokemon:
        next_evolution = dict(title_ru=next_pokemon.title_ru,
                              pokemon_id=next_pokemon.id,
                              img_url=request.build_absolute_uri(next_pokemon.photo.url))
    pokemon_dict = dict(pokemon_id=pokemon_id,
                        title_ru=one_pokemon.title_ru,
                        title_en=one_pokemon.title_en,
                        title_jp=one_pokemon.title_jp,
                        description=one_pokemon.description,
                        img_url=one_pokemon_url,
                        previous_evolution=previous_evolution,
                        next_evolution=next_evolution)

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_dict,
    })
