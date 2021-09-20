from random import *


def random_usernames():
    Data = ["Ace", "King", "Jack", "Queen", "Joker"]

    # for i in range(5):
    #     print(choice(Data))

    adjectives = ["good", "fantastic", "adorable", "cute", "nice", "brilliant"]

    print("random usernames :")

    return choice(adjectives) + "_" + choice(Data)
