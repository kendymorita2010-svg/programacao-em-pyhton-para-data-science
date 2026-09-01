
import matplotlib.pyplot as plt
import numpy as np
import random


# 151 Pokémon da 1ª geração
pokemons = [
    'Bulbasaur', 'Ivysaur', 'Venusaur',
    'Charmander', 'Charmeleon', 'Charizard',
    'Squirtle', 'Wartortle', 'Blastoise',
    'Caterpie', 'Metapod', 'Butterfree',
    'Weedle', 'Kakuna', 'Beedrill',
    'Pidgey', 'Pidgeotto', 'Pidgeot',
    'Rattata', 'Raticate',
    'Spearow', 'Fearow',
    'Ekans', 'Arbok',
    'Pikachu', 'Raichu',
    'Sandshrew', 'Sandslash',
    'Nidoran♀', 'Nidorina', 'Nidoqueen',
    'Nidoran♂', 'Nidorino', 'Nidoking',
    'Clefairy', 'Clefable',
    'Vulpix', 'Ninetales',
    'Jigglypuff', 'Wigglytuff',
    'Zubat', 'Golbat',
    'Oddish', 'Gloom', 'Vileplume',
    'Paras', 'Parasect',
    'Venonat', 'Venomoth',
    'Diglett', 'Dugtrio',
    'Meowth', 'Persian',
    'Psyduck', 'Golduck',
    'Mankey', 'Primeape',
    'Growlithe', 'Arcanine',
    'Poliwag', 'Poliwhirl', 'Poliwrath',
    'Abra', 'Kadabra', 'Alakazam',
    'Machop', 'Machoke', 'Machamp',
    'Bellsprout', 'Weepinbell', 'Victreebel',
    'Tentacool', 'Tentacruel',
    'Geodude', 'Graveler', 'Golem',
    'Ponyta', 'Rapidash',
    'Slowpoke', 'Slowbro',
    'Magnemite', 'Magneton',
    'Farfetch’d',
    'Doduo', 'Dodrio',
    'Seel', 'Dewgong',
    'Grimer', 'Muk',
    'Shellder', 'Cloyster',
    'Gastly', 'Haunter', 'Gengar',
    'Onix',
    'Drowzee', 'Hypno',
    'Krabby', 'Kingler',
    'Voltorb', 'Electrode',
    'Exeggcute', 'Exeggutor',
    'Cubone', 'Marowak',
    'Hitmonlee', 'Hitmonchan',
    'Lickitung',
    'Koffing', 'Weezing',
    'Rhyhorn', 'Rhydon',
    'Chansey',
    'Tangela',
    'Kangaskhan',
    'Horsea', 'Seadra',
    'Goldeen', 'Seaking',
    'Staryu', 'Starmie',
    'Mr. Mime',
    'Scyther',
    'Jynx',
    'Electabuzz',
    'Magmar',
    'Pinsir',
    'Tauros',
    'Magikarp', 'Gyarados',
    'Lapras',
    'Ditto',
    'Eevee',
    'Vaporeon', 'Jolteon', 'Flareon',
    'Porygon',
    'Omanyte', 'Omastar',
    'Kabuto', 'Kabutops',
    'Aerodactyl',
    'Snorlax',
    'Articuno', 'Zapdos', 'Moltres',
    'Dratini', 'Dragonair', 'Dragonite',
    'Mewtwo', 'Mew'
]


# Escolhe um Pokémon aleatoriamente
pokemon = random.choice(pokemons)


# Gera atributos aleatórios
valores = [
    random.randint(1, 100),  # HP
    random.randint(1, 100),  # Ataque
    random.randint(1, 100),  # Defesa
    random.randint(1, 100),  # Velocidade
    random.randint(1, 100)   # Ataque Especial
]


# Categorias
categorias = [
    'HP',
    'Ataque',
    'Defesa',
    'Velocidade',
    'Ataque Especial'
]


# Fecha o gráfico
valores += valores[:1]

angulos = np.linspace(
    0,
    2 * np.pi,
    len(categorias) + 1
)


# Cria o gráfico radar
fig, ax = plt.subplots(
    subplot_kw={'polar': True}
)


ax.plot(angulos, valores)
ax.fill(angulos, valores, alpha=0.25)


ax.set_xticks(angulos[:-1])
ax.set_xticklabels(categorias)


ax.set_ylim(0, 100)


ax.set_title(
    f'{pokemon} - Status Aleatórios',
    pad=20
)


plt.show()