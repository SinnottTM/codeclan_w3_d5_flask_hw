class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self, player_1, player_2):
        player_1_choice = player_1.lower()
        player_2_choice = player_2.lower()
        if player_1_choice == player_2_choice:
            return "Draw"
        elif player_1_choice == "rock" and player_2_choice == "scissors":
            return "Player 2"
        elif player_1_choice == "rock" and player_2_choice == "paper":
            return "Player 2"
        elif player_1_choice == "scissors" and player_2_choice == "rock":
            return "Player 2"
        elif player_1_choice == "scissors" and player_2_choice == "paper":
            return "Player 1"
        elif player_1_choice == "paper" and player_2_choice == "scissors":
            return "Player 1"
        elif player_1_choice == "paper" and player_2_choice == "rock":
            return "Player 1"
