class Round(object):
    def __init__(self, damage, space_occupied):
        self.damage = damage
        self.space_occupied = space_occupied

    def get_damage(self):
        return self.damage

    def get_space_occupied(self):
        return self.space_occupied
