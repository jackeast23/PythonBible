import random

# Class is the template

class Dollar:

    # Constructor method
    def __init__(self, rare = False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.value = 1.00
        self.colour = "gold"
        self.num_edges = 11
        self.diameter = 26.5 # mm
        self.thickness = 1.95 # mm
        self.heads = True

    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("Coin Spent!")


# Object is an instance of the class Dollar

coin1 = Dollar()
coin1.rust()
print(coin1.colour)
coin1.clean()
print(coin1.colour)
print(coin1.heads)
coin1.flip()
print(coin1.heads)
del coin1

coin2 = Dollar()
print(coin2.colour)

