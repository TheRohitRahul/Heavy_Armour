from Classes.Rounds.round import Round

class Round_1(Round):
    def __init__(self):
        damage = 10
        space_occupied = 1
        super(Round_1, self).__init__(damage, space_occupied)
