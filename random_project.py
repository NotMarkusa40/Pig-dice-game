import random
from collections.abc import MutableSequence


class player_scores(MutableSequence):
    """Mutable sequence containing each player's non-negative score."""

    def __init__(self, player_count):
        if not isinstance(player_count, int) or player_count < 1:
            raise ValueError("player_count must be a positive integer")
        self._scores = [0] * player_count

    def __getitem__(self, index):
        return self._scores[index]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            values = list(value)
            for score in values:
                self._validate_score(score)
            self._scores[index] = values
            return

        self._validate_score(value)
        self._scores[index] = value

    def __delitem__(self, index):
        del self._scores[index]

    def __len__(self):
        return len(self._scores)

    def insert(self, index, value):
        self._validate_score(value)
        self._scores.insert(index, value)

    @staticmethod
    def _validate_score(value):
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("scores must be non-negative integers")

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

Value = roll()
print(Value)

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
    else:
        print("Invalid input. Enter a number between 2 and 4.")

print(players)
max_score = 30
scores: player_scores = player_scores(players)

print(scores)

while max(scores) < max_score:

    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}, your turn has just started!")
        current_score = 0

        while True:
            should_roll = input(f"Player {player_idx + 1}, do you want to roll the dice? (y): ")
            if should_roll.lower() == 'y':
                value = roll()
                if value == 1:
                    print("You rolled a 1! You lose your turn.")
                    current_score = 0
                    break

                current_score += value
                print("You rolled a", value)
                print("Your current score is:", current_score)
            else:
                break

        scores[player_idx] += current_score
        print("Your total score is:", scores[player_idx])

        if scores[player_idx] >= max_score:
            print(f"Player {player_idx + 1} wins with a score of {scores[player_idx]}!")
            
