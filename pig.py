import random
import time
import sys

# Base Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_score = 0

    def decide_action(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def roll(self):
        roll_value = random.randint(1, 6)
        if roll_value == 1:
            self.turn_score = 0
            print(f"{self.name} rolled a 1! Turn over.")
        else:
            self.turn_score += roll_value
        return roll_value

    def hold(self):
        self.score += self.turn_score
        print(f"{self.name} holds with {self.turn_score} points. Total score: {self.score}")
        self.turn_score = 0

# Human Player class
class HumanPlayer(Player):
    def decide_action(self):
        action = input(f"{self.name}, do you want to roll or hold? (r/h): ").strip().lower()
        while action not in ['r', 'h']:
            print("Invalid input. Please enter 'r' for roll or 'h' for hold.")
            action = input(f"{self.name}, do you want to roll or hold? (r/h): ").strip().lower()
        return action

# Computer Player class with a predefined strategy
class ComputerPlayer(Player):
    def decide_action(self):
        if self.turn_score >= 25 or self.score + self.turn_score >= 100:
            return 'h'  # Hold if turn score >= 25 or the total score reaches 100
        else:
            return 'r'  # Roll if the turn score is less than 25

# Player Factory Class to instantiate correct player type
class PlayerFactory:
    @staticmethod
    def create_player(player_type, name):
        if player_type == "human":
            return HumanPlayer(name)
        elif player_type == "computer":
            return ComputerPlayer(name)
        else:
            raise ValueError("Unknown player type")

# Game Class
class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = 0

    def play_turn(self, action):
        current_player = self.players[self.current_player]
        if action == 'r':
            current_player.roll()
        elif action == 'h':
            current_player.hold()
        
        if current_player.score >= 100:
            print(f"{current_player.name} wins with {

