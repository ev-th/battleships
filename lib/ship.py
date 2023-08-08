class Ship:
    def __init__(self, length):
        self.health = length
        self.length = length
        
    def take_damage(self):
        self.health -= 1

    def is_sunk(self):
        return self.health == 0