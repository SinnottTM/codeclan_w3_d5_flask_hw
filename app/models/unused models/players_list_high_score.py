from app.models.player import Player

player1 = Player("Tim", "Rock")
player2 = Player("Stuart", "Paper")
player3 = Player("Scott", "Scissors")
players = [player1, player2, player3]

def add_new_player(player):
    players.append(player)

def remove_player(player):
    players.remove(player)
