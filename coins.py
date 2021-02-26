import random

class Coin: 
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        for key, value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "${} coin".format(int(self.original_value))
        else:
            return "{} cent coin".format(int(self.original_value * 100))


class Loonie(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "brownish",
            "num_edges": 11,
            "diameter": 26.5,
            "thickness": 1.95,
            "mass": 6.27
        }
        super().__init__(**data)

class Penny(Coin):
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "copper",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 19.05,
            "thickness": 1.45,
            "mass": 2.35
        }
        super().__init__(**data)

class Dime(Coin):
    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 118,
            "diameter": 18.03,
            "thickness": 1.22,
            "mass": 1.75
        }
        super().__init__(**data)
        
    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Nickel(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 21.2,
            "thickness": 1.76,
            "mass": 3.95
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Quarter(Coin):
    def __init__(self):
        data = {
            "original_value": 0.25,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 119,
            "diameter": 23.88,
            "thickness": 1.58,
            "mass": 4.4
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class Toonie(Coin):
    def __init__(self):
        data = {
            "original_value": 2.00,
            "clean_colour": "gold and silver",
            "rusty_colour": "brownish and silver",
            "num_edges": "Milled and Smooth",
            "diameter": 28,
            "thickness": 1.75,
            "mass": 6.92
        }
        super().__init__(**data)

coins = [Penny(), Nickel(), Dime(), Quarter(), Loonie(), Toonie()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter,
                 coin.thickness, coin.num_edges, coin.mass]

    string = "{} - Colour: {}, value: {}, diamter(mm): {}, thickness(mm): {}, number of edges: {}, mass(g): {}".format(*arguments)
    print(string)