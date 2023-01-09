import random


class Pokemon:
    def __init__(self, name, type, level, attack, defense):
        self.name = name
        self.type = type
        self.level = level
        self.attack = attack
        self.defense = defense


def simulate_battle(pokemon1, pokemon2):
    # calculate damage done by each attack
    damage1 = pokemon1.attack - pokemon2.defense
    damage2 = pokemon2.attack - pokemon1.defense

    # apply damage to each Pokemon's hit points
    pokemon1.hit_points -= damage1
    pokemon2.hit_points -= damage2

    # check if either Pokemon has fainted (hit points <= 0)
    if pokemon1.hit_points <= 0:
        print(pokemon1.name + " has fainted!")
    if pokemon2.hit_points <= 0:
        print(pokemon2.name + " has fainted!")


def choose_pokemon(player_pokemon):
    # print the names of the player's Pokemon
    for i in range(len(player_pokemon)):
        print(str(i+1) + ". " + player_pokemon[i].name)

    # prompt the user to choose a Pokemon
    choice = input("Choose a Pokemon: ")
    chosen_pokemon = player_pokemon[int(choice) - 1]

    # return the chosen Pokemon
    return chosen_pokemon


# create some Pokemon
pikachu = Pokemon("Pikachu", "electric", 10, 55, 30)
charmander = Pokemon("Charmander", "fire", 10, 52, 43)
bulbasaur = Pokemon("Bulbasaur", "grass", 10, 49, 49)

# create a list of the player's Pokemon
player_pokemon = [pikachu, charmander, bulbasaur]

# choose a Pokemon for the player
player_chosen = choose_pokemon(player_pokemon)

# choose a random Pokemon for the opponent
opponent_pokemon = random.choice(player_pokemon)

# simulate the battle
simulate_battle(player_chosen, opponent_pokemon)
