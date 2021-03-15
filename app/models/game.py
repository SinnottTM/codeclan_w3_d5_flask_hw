class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self, player_1, player_2):
        player_1_choice = player_1
        player_2_choice = player_2
        if player_1_choice.lower() == player_2_choice.lower():
            return "Draw"
        elif player_1_choice.lower() == "rock" and player_2_choice.lower() == "scissors":
            return "Player 2"
        elif player_1_choice.lower() == "rock" and player_2_choice.lower() == "paper":
            return "Player 2"
        elif player_1_choice.lower() == "scissors" and player_2_choice.lower() == "rock":
            return "Player 2"
        elif player_1_choice.lower() == "scissors" and player_2_choice.lower() == "paper":
            return "Player 1"
        elif player_1_choice.lower() == "paper" and player_2_choice.lower() == "scissors":
            return "Player 1"
        elif player_1_choice.lower() == "paper" and player_2_choice.lower() == "rock":
            return "Player 1"
