# importing random to allow the cpu to (appear to) make a choice
import random

# Game class for player versus computer, takes two parameters for the player and cpu
class Gamecpu():
    def __init__(self, player_1):
        self.player_1 = player_1

    # function to allow for game logic between between player and cpu
    def play_game_cpu_choice(self):
        cpu_choices_list = ["rock", "paper", "scissors"]
        cpu_choice = random.choice(cpu_choices_list)
        return cpu_choice

    # function to allow for game logic between player and cpu.
    # Issue: Seems to return random answer each time, can't separate infomation effectively
    def play_game_cpu(self, player_1):
        gamecpu = Gamecpu(player_1)
        cpu_choice = gamecpu.play_game_cpu_choice
        player_1_choice = player_1.lower()
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
