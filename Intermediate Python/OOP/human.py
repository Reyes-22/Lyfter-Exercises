class Head:
    def __init__(self):
        pass


class Arms:
    def __init__(self, hand):
        self.hand = hand


class Hands:
    def __init__(self):
        pass


class Legs:
    def __init__(self, feet):
        self.feet = feet


class Feet:
    def __init__(self):
        pass


class Torso:
    def __init__(self, head, right_arm, right_hand, left_arm, left_hand, right_leg, right_foot, left_leg, left_foot):
        self.head = head
        self.right_arm = right_arm
        self.right_hand = right_hand
        self.left_arm = left_arm
        self.left_hand = left_hand
        self.right_leg = right_leg
        self.right_foot = right_foot
        self.left_leg = left_leg
        self.left_foot = left_foot


class Human:
    def __init__(self, torso):
        self.torso = torso


head = Head()
right_hand = Hands()
left_hand = Hands()
right_arm = Arms(right_hand)
left_arm = Arms(left_hand)
right_foot = Feet()
left_foot = Feet()
right_leg = Legs(right_foot)
left_leg = Legs(left_foot)
torso = Torso(head, right_arm, right_hand, left_arm, left_hand,
              right_leg, right_foot, left_leg, left_foot)
my_human = Human(torso)

print(my_human)
