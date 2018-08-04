from copy import copy

class Tank(object):
    def __init__(self, armour, round_carrying_capacity, miss_chance):
        self.armour = armour
        self.living = True
        self.round_carrying_capacity = round_carrying_capacity
        self.rounds = [None]*self.round_carrying_capacity
        self.miss_chance = miss_chance

    def get_armour(self):
        return self.armour

    def take_hit(self, round):
        if self.living:
            self.armour = self.armour - round.get_damage()
            if self.armour <= 0:
                self.living = False

    def is_alive(self):
        return self.living

    def load_round(self, round):
        if None in self.rounds:
            for i in range(self.round_carrying_capacity):
                if type(self.rounds[i]) == type(None):
                    self.rounds[i] = round
        else:
            return False

    def get_rounds(self):
        return self.rounds

    def get_miss_chance(self):
        return self.miss_chance

    def fire_round(self, round_name):
        for i, a_round in enumerate(self.rounds):
            if type(a_round) != type(None):
                if a_round.name == str(round_name):
                    round_to_return = copy(a_round)
                    del self.rounds[i]
                    return round_to_return
            else:
                return None
