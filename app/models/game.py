class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self, player_1, player_2):
        player_1_choice = player_1
        player_2_choice = player_2
        if player_1_choice == player_2_choice:
            return "D"
        elif player_1_choice == "rock" and player_2_choice == "scissors":
            return "P1R"
        elif player_1_choice == "rock" and player_2_choice == "paper":
            return "P2P"
        elif player_1_choice == "scissors" and player_2_choice == "rock":
            return "P2R"
        elif player_1_choice == "scissors" and player_2_choice == "paper":
            return "P1S"
        elif player_1_choice == "paper" and player_2_choice == "scissors":
            return "P2S"
        elif player_1_choice == "paper" and player_2_choice == "rock":
            return "P1P"
