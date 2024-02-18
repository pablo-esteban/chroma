import random


# TODO: make choice strategy configurable linear/random/statistical-distribution
# TODO: remember previous choices
def choose_one(data, seed=None):
    random.seed(a=seed)
    colour = random.choice(data)
    return colour
