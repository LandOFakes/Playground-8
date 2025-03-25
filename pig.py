class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def decide_action(self):
        while True:
            action = input(f"{self.name}, do you want to roll or hold? (r/h): ").strip().lower()
            if action in ['r', 'h']:
                return action
            else:
                print("Invalid input! Please enter 'r' for roll or 'h' for hold.")

def main():
    player1_type = sys.argv[1]  
    player2_type = sys.argv[2]  
    is_timed = '--timed' in sys.argv  
    
    player1 = PlayerFactory.create_player(player1_type, "Player 1")
    player2 = PlayerFactory.create_player(player2_type, "Player 2")
    
    game = TimedGameProxy(player1, player2) if is_timed else Game(player1, player2)
    
    game_over = False
    while not game_over:
        current_player = game.players[game.current_player]
        action = current_player.decide_action() 
        game_over = game.play_turn(action)
        if not game_over:
            game.next_player()

if __name__ == "__main__":
    main()

