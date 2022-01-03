import random
from dictionaries import field_markings


class Player():
    """Represents a player"""

    def __init__(self, team):
        if team != 'empty':
            self.team = team
        else:
            # random.randbytes(1)
            pass
        # in else it should get random byte and choose team depending on the result
