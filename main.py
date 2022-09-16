import random


class Pokemon:
    def __init__(self, name, element, health, moves):
        self._name = name
        self._element = element
        self._health = health
        self._moves = moves  # dictionary of moves and attack damage
        self._battle_ready = True

    def get_pokemon_name(self):
        return self._name

    def get_element(self):
        return self._element

    def get_health(self):
        return self._health

    def get_moves(self):
        return self._moves

    def get_moves_list(self):
        """returns a list of moves names the pokemon has"""
        moves_list = []
        for moves in self._moves:
            moves_list.append(moves)
        return moves_list

    def get_attack_damage(self, attack_move):
        return self._moves[attack_move]

    def get_attack_from_num(self, num):
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
        health_bar = "[]" * int(bar_count)
        return health_bar

    def lose_health(self, damage):
        self._health -= damage
        if self._health <= 0:
            self._battle_ready = False

    def gain_health(self, health_points):
        self._health += health_points

    def check_pokemon_availability(self):
        return self._battle_ready

  #   def pokemon_fainted(self):
   #     self._battle_ready = False


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
        self._battle_ready = True

    def get_trainer_name(self):
        """returns name of trainer"""
        return self._name

    def add_pokemon(self, new_pokemon_object):
        """adds new pokemon object into pokemon dictionary with their name as the key"""
        pokemon_name = new_pokemon_object.get_pokemon_name()
        self._pokemon_dic[pokemon_name] = new_pokemon_object

    def get_pokemon_dic(self):
        """returns pokemon dictionary with pokemon name and pokemon object"""
        return self._pokemon_dic

    def get_pokemon_object(self, pokemon_name):
        """returns pokemon object give pokemon name"""
        return self._pokemon_dic[pokemon_name]

    def get_pokemon_list(self):
        """returns a list of Pokemon names the trainer has"""
        pokemon_list = []
        for pokemon in self._pokemon_dic:
            pokemon_list.append(pokemon) # including name of pokemon. Should I make a list of pokemon objects?
        return pokemon_list

    def ready_for_battle(self):
        trainer_pokemon_count = 0
        for pokemon in self.get_pokemon_dic():
            pokemon_object = self.get_pokemon_object(pokemon)
            if pokemon_object.check_pokemon_availability():
                trainer_pokemon_count += 1
        if trainer_pokemon_count == 0:
            self._battle_ready = False
        return self._battle_ready


class PokemonBattle:
    def __init__(self, player, trainer, wager):
        self._player = player          # player object
        self._trainer = trainer     # trainer object
        self._wager = wager
        self._is_battle = True

    def still_playing(self, trainer):
        """verifies whether the trainer can continue battling by returning a boolean"""
        available_pokemon = 0
        trainer_pokemon = trainer.get_pokemon_list()

        for pokemon in trainer_pokemon:
            pokemon_object = trainer.get_pokemon_object(pokemon)
            if pokemon_object.check_pokemon_availability():
                available_pokemon += 1
        if available_pokemon == 0:
            self._is_battle = False

    def battle(self):

        # introduce starting pokemon from player and trainer
        trainer_pokemon = random.choice(self._trainer.get_pokemon_list())

        print(f"\nYou are challenged by Leader {self._trainer.get_trainer_name()}!")
        print(f"Leader {self._trainer.get_trainer_name()} sent out {trainer_pokemon.upper()}!")

        print(f"\nHere is your Pokemon list: {self._player.get_pokemon_list()}!")
        player_pokemon = input("Who do you want to take out for battle? ")
        # DEBUG: if user spells incorrectly
        print(f"\n{self._player.get_trainer_name()}: I choose you, {player_pokemon.upper()}!")

        # pokemon objects available to start battling
        trainer_pokemon_object = self._trainer.get_pokemon_object(trainer_pokemon.capitalize())
        player_pokemon_object = self._player.get_pokemon_object(player_pokemon.capitalize())

        move_count = 1

        print(f"\n" * 10)
        print(f"\nLeader {self._trainer.get_trainer_name()}'s {trainer_pokemon.upper()}: "
              f"{trainer_pokemon_object.get_health_bar()}")
        print(f"{self._player.get_trainer_name()}'s {player_pokemon.upper()}: "
              f"{player_pokemon_object.get_health_bar()}")

        while self._is_battle:
            # create separate function to display health

            if move_count % 2 != 0: # if odd

            # trainer attacks
                trainer_attack = random.choice(trainer_pokemon_object.get_moves_list())
                print(f"\nLeader {self._trainer.get_trainer_name()}'s {trainer_pokemon.upper()} used {trainer_attack}!")

                # update player's health
                trainer_damage = trainer_pokemon_object.get_attack_damage(trainer_attack)
                player_pokemon_object.lose_health(trainer_damage)
                self.still_playing(self._player)
                move_count += 1

            else:
                print(f"\n{player_pokemon.upper()}'s moves: ")

                for moves in player_pokemon_object.get_moves_list():
                    print(f"{player_pokemon_object.get_moves_list().index(moves)+1}. {moves}")

                player_attack_num = input(f"What will {player_pokemon.upper()} do? Input a number to select move: ")
                player_attack = player_pokemon_object.get_attack_from_num(player_attack_num)
                print(f"\n{self._player.get_trainer_name()}'s {player_pokemon.upper()} used {player_attack}!")

                player_damage = player_pokemon_object.get_attack_damage(player_attack)
                trainer_pokemon_object.lose_health(player_damage)
                self.still_playing(self._trainer)
                move_count += 1

            print(f"\n"*10)
            print(f"\nLeader {self._trainer.get_trainer_name()}'s {trainer_pokemon.upper()}: "
                  f"{trainer_pokemon_object.get_health_bar()}")
            print(f"{self._player.get_trainer_name()}'s {player_pokemon.upper()}: "
                  f"{player_pokemon_object.get_health_bar()}")




Charizard = Pokemon('Charizard', 'Fire', 100, {'Flamethrower': 20, 'Fly': 10, 'Blast Burn': 40, 'Fire Punch': 30})
Blastoise = Pokemon('Blastoise', 'Water', 90, {'Water Gun': 20, 'Bubblebeam': 10, 'Hydro Pump': 40, 'Surf': 30})
Venusaur = Pokemon('Venusaur', 'Grass', 120, {'Vine Wip': 20, 'Razor Leaf': 10, 'Earthquake': 40, 'Frenzy Plant': 30})

player_name = input("Player, what is your name? ")
player_object = Trainer(player_name)            # creating player
player_object.add_pokemon(Charizard)

grass_trainer = Trainer("MossHead")
grass_trainer.add_pokemon(Venusaur)
grass_trainer.add_pokemon(Blastoise)


water_trainer = Trainer("Moisty")
water_trainer.add_pokemon(Blastoise)

game = PokemonBattle(player_object, grass_trainer, 10)
game.battle()


