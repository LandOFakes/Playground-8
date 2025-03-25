import random
import time
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def roll_dice(self):
        return random.randint(1, 6)
    
    def reset(self):
        self.score = 0

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def decide_action(self):
        action = input(f"{self.name}, do you want to roll or hold? (r/h): ")
        return action.lower()


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def decide_action(self):
        if self.score >= 100:
            return 'h'  
        hold_threshold = min(25, 100 - self.score)
        if self.score >= hold_threshold:
            return 'h'  
        else:
            return 'r' 

class PlayerFactory:
    @staticmethod
    def create_player(player_type, name):
        if player_type == "human":
            return HumanPlayer(name)
        elif player_type == "computer":
            return ComputerPlayer(name)
        else:
            raise ValueError(f"Unknown player type: {player_type}")

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = 0
        self.turn_score = 0
    
    def roll_dice(self):
        return random.randint(1, 6)
    
    def play_turn(self, action):
        if action == 'r':  # roll
            roll = self.roll_dice()
            print(f"{self.players[self.current_player].name} rolled a {roll}")
            if roll == 1:
                print(f"{self.players[self.current_player].name} loses turn.")
                self.turn_score = 0
            else:
                self.turn_score += roll
        elif action == 'h':  # hold
            print(f"{self.players[self.current_player].name} holds.")
            self.players[self.current_player].score += self.turn_score
            self.turn_score = 0
        
        if self.players[self.current_player].score >= 100:
            print(f"{self.players[self.current_player].name} wins!")
            return True
        return False
    
    def next_player(self):
        self.current_player = (self.current_player + 1) % 2

class TimedGameProxy(Game):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.start_time = time.time()
    
    def play_turn(self, action):
        current_time = time.time()
        if current_time - self.start_time > 60:
            print("Game time exceeded 1 minute!")
           
            if self.players[0].score > self.players[1].score:
                print(f"{self.players[0].name} wins!")
            elif self.players[0].score < self.players[1].score:
                print(f"{self.players[1].name} wins!")
            else:
                print("It's a tie!")
            return True
        
        return super().play_turn(action)

def main():
    
    player1_type = sys.argv[1]
    player2_type = sys.argv[2]
    is_timed = '--timed' in sys.argv
    
    player1 = PlayerFactory.create_player(player1_type, "Player 1")
    player2 = PlayerFactory.create_player(player2_type, "Player 2")
    
    if is_timed:
        game = TimedGameProxy(player1, player2)
    else:
        game = Game(player1, player2)

    game_over = False
    while not game_over:
        current_player = game.players[game.current_player]
        action = current_player.decide_action()
        game_over = game.play_turn(action)
        if not game_over:
            game.next_player()

if __name__ == "__main__":
    main()
