import random


class Pokemon:
    def __init__(self, name, element, health, moves):
        self._name = name
        self._element = element
        self._health = health
        self._moves = moves  # dictionary of moves and attack damage
        self._fainted = False       #

    def get_name(self):
        return self._name

    def get_element(self):
        return self._element

    def get_health(self):
        return self._health

    def get_moves(self):
        return self._moves

    def get_health_bar(self):
        """displays health bar based on available health"""
        bar_count = (self.get_health() / 10)
        health_bar = "[]" * int(bar_count)
        return health_bar

    def lose_health(self, damage):
        self._health -= damage

    def gain_health(self, health_points):
        self._health += health_points


class Bag:
    def __init__(self, potion_name, health_points):
        self._potion_name = potion_name
        self._health_points = health_points

    def get_potion_name(self):
        return self._potion_name

    def get_health_points(self):
        return self._health_points

#    def get_bag_items(self):


class Trainer:
    def __init__(self, name):
        self._name = name
        self._pokemon_dic = {}    # dictionary key: pokemon name, value: pokemon object

    def add_pokemon(self, new_pokemon_object):
        self._pokemon_dic[new_pokemon_object.get_name()] = new_pokemon_object

    def get_pokemon_list(self):
        """returns a list of Pokemon the trainer has"""
        pokemon_list = []
        for pokemon in self._pokemon_dic:
            pokemon_list.append(pokemon)
        return pokemon_list



Charizard = Pokemon('Charizard', 'Fire', 100, {'Flamethrower': 20, 'Fly': 10, 'Blast Burn': 40, 'Fire Punch': 30})
Blastoise = Pokemon('Blastoise', 'Water', 90, {'Water Gun': 20, 'Bubblebeam': 10, 'Hydro Pump': 40, 'Surf': 30})
Venusaur = Pokemon('Venusaur', 'Grass', 120, {'Vine Wip': 20, 'Razor Leaf': 10, 'Earthquake': 40, 'Frenzy Plant': 30})

player_name = input("Player, what is your name? ")
player_object = Trainer(player_name)            # creating player
player_object.add_pokemon(Charizard)

grass_trainer = Trainer("MossHead")
player_object.add_pokemon(Venusaur)

water_trainer = Trainer("Moisty")
player_object.add_pokemon(Blastoise)

