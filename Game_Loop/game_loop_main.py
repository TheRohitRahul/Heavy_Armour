import sys
import os
from random import randint
sys.path.append(".")

from Classes.Tanks.panzer import Panzer
from Classes.Rounds.round_1 import Round_1

def attack(attacker, target, round):
    miss_chance = attacker.get_miss_chance()
    if randint(0, miss_chance) == 0:
        target.take_hit(round)
        return True
    else:
        return False

def player_attack(player_tank, enemy_tank):
    if player_tank.is_alive():
        print "\nYou launched a missile"
        if attack(player_tank, enemy_tank, player_tank.get_rounds()[0]):
            print "Enemy tank took hit"
        else:
            print "You missed"

def enemy_attack(player_tank, enemy_tank):
    if enemy_tank.is_alive():
        print "\nenemy tank launched a missile"
        if attack(enemy_tank, player_tank, enemy_tank.get_rounds()[0]):
            print "You were hit"
        else:
            print "Enemy tank missed"

def start_game():
    player_tank = Panzer()
    enemy_tank = Panzer()

    player_tank.load_round(Round_1())
    player_tank.load_round(Round_1())

    enemy_tank.load_round(Round_1())
    enemy_tank.load_round(Round_1())

    while(player_tank.is_alive() and enemy_tank.is_alive()):
        print "\nYour Armour : {}".format(player_tank.get_armour())
        print "Enemy Armour : {}\n".format(enemy_tank.get_armour())
        action = raw_input("press c to attack : ")
        if action == "c":
            if randint(0,1) == 1:
                player_attack(player_tank, enemy_tank)
                enemy_attack(player_tank, enemy_tank)
            else:
                enemy_attack(player_tank, enemy_tank)
                player_attack(player_tank, enemy_tank)
        else:
            print "not a valid move"
            continue

    if player_tank.is_alive():
        print "\nYou Won\n"

    else:
        print "\nYou Lost\n"

if __name__ == "__main__":
    start_game()
