import random

from pokemon_art import pokemon_sign, transition

import csv

pokemon_list = open("pokemon_list.csv", "r")
reader_1 = csv.reader(pokemon_list)

move_list = open("move_list.csv", "r")
reader_2 = csv.reader(move_list)

pokedex = []
pokedata_moves = []

for row in reader_1:
    pokedex.append(row)

for row in reader_2:
    pokedata_moves.append(row)


class Pokemon:
    """Represents a Pokemon given their name, element, health points, and moves with their corresponding damage """

    def __init__(self, name, element, health, speed, moves):
        self._name = name
        self._element = element
        self._health = health
        self._speed = speed
        self._moves = moves  # dictionary of moves and attack damage and accuracy
        self._battle_ready = True

    def get_pokemon_name(self):
        """returns name of the pokemon"""
        return self._name

    def get_element(self):
        """returns element of the pokemon"""
        return self._element

    def get_health(self):
        """return health points value of the pokemon"""
        return self._health

    def get_speed(self):
        return self._speed

    def get_moves(self):
        """returns dictionary of move name as key and its damage as the value"""
        return self._moves

    def get_moves_list(self):
        """returns a list of moves names the pokemon has"""
        moves_list = []
        for moves in self._moves:
            moves_list.append(moves)
        return moves_list

    def get_attack_damage(self, attack_move):
        """returns the attack damage given the name of attack"""
        return self._moves[attack_move]

    def get_attack_from_num(self, num):
        """returns name of pokemon move given the number the user inputs"""
        moves_list = []
        for moves in self._moves:
            moves_list.append(moves)

        attack_index = int(num) - 1
        for move in self._moves:
            if moves_list.index(move) == attack_index:
                return move

    def get_health_bar(self):
        """displays health bar based on available health"""
        bar_count = (self.get_health() / 10)
        health_bar = "[]" * int(bar_count) + " (HP: " + str(self._health) + " )"
        return health_bar

    def lose_health(self, damage):
        """updates new health after damage taken and returns boolean if pokemon is unavailable to battle"""
        self._health -= damage
        if self._health <= 0:
            self._health = 0
            self._battle_ready = False

    def gain_health(self, health_points):
        """updates new health after healing with potion"""
        self._health += health_points

    def get_availability(self):
        """returns boolean that determines if pokemon is available to battle"""
        return self._battle_ready

    def update_availability(self):
        self._battle_ready = False


class Bag:
    """Represents the user's bag and the items inside of it given their name and their corresponding healing points"""

    def __init__(self, potion_name, health_points):
        self._potion_name = potion_name
        self._health_points = health_points

    def get_potion_name(self):
        """returns the name of the health potion"""
        return self._potion_name

    def get_health_points(self):
        """returns the amount of health the potion recovers"""
        return self._health_points

#    def get_bag_items(self):


class Trainer:
    """Represents a Trainer given their name"""

    def __init__(self, name):
        self._name = name
        self._pokemon_dic = {}    # dictionary key: pokemon name, value: pokemon object
        self._battle_ready = True
        self._forfeit = False

    def get_trainer_name(self):
        """returns name of trainer"""
        return self._name

    def add_pokemon(self, new_pokemon_object):
        """adds new pokemon object into dictionary with their name as the key and pokemon object as value"""
        pokemon_name = new_pokemon_object.get_pokemon_name()
        self._pokemon_dic[pokemon_name] = new_pokemon_object

    def get_pokemon_dic(self):
        """returns dictionary with pokemon name as key and pokemon object as value"""
        return self._pokemon_dic

    def get_pokemon_object(self, pokemon_name):
        """returns pokemon object give pokemon name"""
        return self._pokemon_dic[pokemon_name]

    def get_pokemon_list(self):
        """returns a list of Pokemon object the trainer has"""
        pokemon_list = []
        for pokemon in self._pokemon_dic:
            pokemon_list.append(pokemon)
        return pokemon_list

    def ready_for_battle(self):
        """returns boolean to determine if trainer has pokemon available for battle"""
        trainer_pokemon_count = 0

        for pokemon in self.get_pokemon_dic():
            pokemon_object = self.get_pokemon_object(pokemon)
            if pokemon_object.get_availability():
                trainer_pokemon_count += 1
        print(f"DEBUG: trainer pokemon availability count {trainer_pokemon_count}")

        if trainer_pokemon_count == 0:
            self._battle_ready = False
        return self._battle_ready

    def get_battle_ready(self):
        return self._battle_ready

    def get_forfeit(self):
        """returns a boolean to determine if the player forfeited the match"""
        return self._forfeit

    def choose_forfeit(self):
        """updates player's forfeited status"""
        self._forfeit = True
        self._battle_ready = False


class PokemonBattle:
    """Represents a battle between two trainers given the user object and trainer object and the amount the user plans
    to wager."""

    def __init__(self, player, trainer, wager):
        self._player = player          # player object
        self._trainer = trainer     # trainer object
        self._wager = wager
        self._is_battle = True

    def quit_battle(self):
        self._is_battle = False

    def still_playing(self, trainer):
        """verifies whether the trainer can continue battling by returning a boolean"""
        available_pokemon = 0
        trainer_pokemon = trainer.get_pokemon_list()

        for pokemon in trainer_pokemon:
            pokemon_object = trainer.get_pokemon_object(pokemon)
            if pokemon_object.get_availability():
                available_pokemon += 1
        if available_pokemon == 0:
            self._is_battle = False

    def pokemon_vs(self, player_pokemon):
        # creates pokemon object for trainer and user
        trainer_pokemon = random.choice(self._trainer.get_pokemon_list())

        trainer_pokemon_object = self._trainer.get_pokemon_object(trainer_pokemon.capitalize())
        player_pokemon_object = self._player.get_pokemon_object(player_pokemon.capitalize())

        # displays trainer's pokemon
        print(f"\nLeader {self._trainer.get_trainer_name()} sent out {trainer_pokemon.upper()}!")
        print(f"Leader {self._trainer.get_trainer_name()}'s {trainer_pokemon.upper()}: "
              f"{trainer_pokemon_object.get_health_bar()}")

        # DEBUG: if user spells incorrectly
        print(f"\n{self._player.get_trainer_name()}: I choose you, {player_pokemon.upper()}!")
        print(f"{self._player.get_trainer_name()}'s {player_pokemon.upper()}: "
              f"{player_pokemon_object.get_health_bar()}")

        # display initial health bar
        print(pokemon_sign)
        print(f"\nLeader {self._trainer.get_trainer_name()}'s {trainer_pokemon.upper()}: "
              f"{trainer_pokemon_object.get_health_bar()}")
        print(f"{self._player.get_trainer_name()}'s {player_pokemon.upper()}: "
              f"{player_pokemon_object.get_health_bar()}")

        # determines which move number we are in. helps determine which trainer attacks
        if player_pokemon_object.get_speed() > trainer_pokemon_object.get_speed():
            move_count = 1
        else:
            move_count = 0

        while player_pokemon_object.get_availability() and trainer_pokemon_object.get_availability():
            # create separate function to display health

            if move_count % 2 == 0:
                # trainer attacks
                trainer_attack = random.choice(trainer_pokemon_object.get_moves_list())
                print(f"\nLeader {self._trainer.get_trainer_name()}'s {trainer_pokemon.upper()} used {trainer_attack}!")
                print(transition)

                # update player's health
                trainer_damage = trainer_pokemon_object.get_attack_damage(trainer_attack)
                player_pokemon_object.lose_health(trainer_damage)  # availability will change if it hits 0

            else:
                # player action list
                player_action_list = "1. FIGHT\n2. BAG\n3. RUN"
                print(player_action_list)
                player_action = input("What will you do trainer? Input a number to select action: ")

                if player_action == "3":
                    self._player.choose_forfeit()
                    player_pokemon_object.update_availability()
                    # stop the while loop

                elif player_action == "2":
                    print("\nBAG is currently empty. You spent too much time rummaging.")  # come back to this

                elif player_action == "1":
                    # player's pokemon's move list
                    print(f"\n{player_pokemon.upper()}'s moves: ")
                    for moves in player_pokemon_object.get_moves_list():
                        print(f"{player_pokemon_object.get_moves_list().index(moves) + 1}. {moves}")

                    # player chooses pokemon move
                    player_attack_num = input(f"What will {player_pokemon.upper()} do? Input a number to select move: ")
                    player_attack = player_pokemon_object.get_attack_from_num(player_attack_num)
                    print(f"\n{self._player.get_trainer_name()}'s {player_pokemon.upper()} used {player_attack}!")
                    print(f"\n" * 2)
                    print(transition)

                    # update trainer's health
                    player_damage = player_pokemon_object.get_attack_damage(player_attack)
                    trainer_pokemon_object.lose_health(player_damage)
                else:
                    print("You didn't type a number from the option, so you couldn't make a decision.")

            move_count += 1
            print(f"\n" * 2)
            print(f"\nLeader {self._trainer.get_trainer_name()}'s {trainer_pokemon.upper()}: "
                  f"{trainer_pokemon_object.get_health_bar()}")
            print(f"{self._player.get_trainer_name()}'s {player_pokemon.upper()}: "
                  f"{player_pokemon_object.get_health_bar()}")

        # displays the outcome of the battle
        if self._player.get_forfeit():
            print(f"\n{self._player.get_trainer_name()} forfeits.")

        elif not player_pokemon_object.get_availability():
            print(f"\n{self._player.get_trainer_name()}'s {player_pokemon.upper()} is unable to battle.")

        elif not trainer_pokemon_object.get_availability():
            print(f"\n{self._trainer.get_trainer_name()}'s {trainer_pokemon.upper()} is unable to battle.")

    def trainer_vs(self):
        print(f"\nYou are challenged by Leader {self._trainer.get_trainer_name()}!")

        while self._is_battle:
            print(f"\nHere is your Pokemon list: {self._player.get_pokemon_list()}!")
            player_pokemon = input("Who do you want to take out for battle? ")
            self.pokemon_vs(player_pokemon)

            if self._player.get_forfeit():
                self.quit_battle()
                print("Because you ran away from battle. You owe $$$.") # determine cost
            elif not self._player.get_battle_ready():
                self.quit_battle()
                print("None of your pokemon can battle. You have lost. You owe $$$")
            elif not self._trainer.get_battle_ready():
                print("You won the battle. You earn $$$")
                self.quit_battle()









row_num = random.randint(1,59)
pokedata = pokedex[row_num]


Charizard = Pokemon('Charizard', 'Fire', 100, 100, {'Flamethrower': 20, 'Fly': 15, 'Blast Burn': 40, 'Fire Punch': 30})
Blastoise = Pokemon('Blastoise', 'Water', 90, 60, {'Water Gun': 20, 'Bubblebeam': 10, 'Hydro Pump': 40, 'Surf': 30})
Venusaur = Pokemon('Venusaur', 'Grass', 120, 30, {'Vine Wip': 20, 'Razor Leaf': 10, 'Earthquake': 40, 'Frenzy Plant': 30})


pokemon_1 = Pokemon(pokedata[0], pokedata[1], int(pokedata[2]), int(pokedata[3]), {'Flamethrower': 20, 'Fly': 15, 'Blast Burn': 40, 'Fire Punch': 30})
player_name = input("Player, what is your name? ")
player_object = Trainer(player_name)
player_object.add_pokemon(Charizard)
player_object.add_pokemon(pokemon_1)

grass_trainer = Trainer("MossHead")
grass_trainer.add_pokemon(Venusaur)
# grass_trainer.add_pokemon(Blastoise)


water_trainer = Trainer("Moisty")
water_trainer.add_pokemon(Blastoise)

game = PokemonBattle(player_object, grass_trainer, 10)
game.trainer_vs()



