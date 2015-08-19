#Creates a generic monster for a game
__author__ = 'Nehemiah'

class Monster:
    """Creates a plug and play monster for a game"""
    def __init__(self, name):
        self.name = name
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def reset(self):
        """resets everythign to default"""
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def in_tokyo(self):
        """Sees if the monster is in Tokyo"""
        if self.status == "In Tokyo":
            return True
        else:
            return False

    def flee(self):
        """Sees if you want to flee"""
        while True:
            intent = input("Would you like to Flee, (Y)es or (N)o: ")
            if intent.lower() == 'y':
                return True
            if intent.lower() == 'n':
                return False
            print("I don't understand.")

    def heal(self, hp):
        try:
            self.health += hp
            if self.health > 10:
                self.health = 10
        except TypeError:
            return

    def attack(self, dmg):
        """Damages the monster, checks for dealth"""
        try:
            self.health -= dmg
            if self.health <= 0:
                self.status = "K.O.'d"
                return self.health
        except TypeError:
            return self.health


    def score(self, success):
        """Monitors progress, checks for victory"""
        pass