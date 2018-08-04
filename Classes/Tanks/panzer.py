from Classes.Tanks.Tank import Tank

class Panzer(Tank):
    def __init__(self):
        armour = 50
        round_carrying_capacity = 100
        miss_chance = 2
        super(Panzer, self).__init__(armour, round_carrying_capacity, miss_chance)
