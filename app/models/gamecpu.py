# importing random to allow the cpu to (appear to) make a choice
import random

# Game class for player versus computer, takes one parameter for the player
class Gamecpu():
    def __init__(self, player_1):
        self.player_1 = player_1
        
    # # function to allow for game logic between two players
    def play_game_cpu(self, player_1):
        player_1_choice = player_1.lower()
        cpu_choices_list = ["rock", "paper", "scissors"]
        cpu_choice = random.choice(cpu_choices_list)
        if player_1_choice == cpu_choice:
            return "Draw"
        elif player_1_choice == "rock" and cpu_choice == "scissors":
            return "Cpu"
        elif player_1_choice == "rock" and cpu_choice == "paper":
            return "Cpu"
        elif player_1_choice == "scissors" and cpu_choice == "rock":
            return "Cpu"
        elif player_1_choice == "scissors" and cpu_choice == "paper":
            return "Player 1"
        elif player_1_choice == "paper" and cpu_choice == "scissors":
            return "Player 1"
        elif player_1_choice == "paper" and cpu_choice == "rock":
            return "Player 1"
