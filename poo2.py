from random import randint

def attributs():
    list = sorted([randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)])
    a, b, c, d = list
    num = a + b + c + d - list[0]
    return num


class npc:
    def __init__(self):
        self.Force

