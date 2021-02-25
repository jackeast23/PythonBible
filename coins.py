# Class is the template

class Dollar:

    value = 1.00
    colour = "gold"
    num_edges = 11
    diameter = 26.5 # mm
    thickness = 1.95 # mm
    heads = True

# Object is an instance of the class Dollar

coin1 = Dollar()
coin1.colour = "greenish"
print(coin1.colour)

coin2 = Dollar()
print(coin2.colour)

coin1.value = 1.25