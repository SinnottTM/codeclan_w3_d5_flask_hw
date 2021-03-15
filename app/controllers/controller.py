# imports for app
from app import app
from flask import render_template, request, redirect
from app.models.player import Player
from app.models.game import Game

# Import for potential high scores list, unused
# from app.models.players_list_high_score import players, add_new_player, remove_player

# default route for GET, event page
@app.route('/')
def index():
    return render_template('gamestart.html', title='Rock Paper Scissors')

# game logic, player 1 versus player 2
@app.route('/<choice_1>/<choice_2>')
def game(choice_1, choice_2):
    contest = Game(choice_1, choice_2)
    victor = contest.play_game(choice_1, choice_2)
    
    return render_template(
        "gameend.html", title="Rock Paper Scissors",
        victor=victor, player_1_choice=choice_1, player_2_choice=choice_2,
    )

#################################################################################

# Game logic, get result using different HTML pages. Abandoned as it didn't work
# Also added a lot of extra HTML pages but would have been useful for unique splash pages etc.

# app.route('/<choice_1>/<choice_2>')
# def run_game(choice_1, choice_2):
#     player_1 = Player("Player 1", choice_1)
#     player_2 = Player("Player 2", choice_2)
#     game = Game(player_1, player_2)
#     result = game.play_game(choice_1, choice_2)
    
#     # Draw condition
#     if result == "D":
#         return render_template("gameenddraw.html",title="The Results")

#         # Player 1 via rock
#     elif result == "P1R":
#         return render_template("gameendp1rock.html", title="The Results")


#         # Player 2 via paper
#     elif result == "P2P":
#         return render_template("gameendp2paper.html",title="The Results")


#         # Player 2 via rock
#     elif result == "P2R":
#         return render_template("gameendp2rock.html",title="The Results")


#         # Player 1 via scissors
#     elif result == "P1S":
#         return render_template("gameendp1scissors.html",title="The Results")

#         # Player 2 via scissors
#     elif result == "P2S":
#         return render_template("gameendp2scissors.html",title="The Results")

#         # Player 1 via paper
#     elif result == "P1P":
#         return render_template("gameendp1paper.html",title="The Results")

#################################################################################
# Logic to add/remove player choices (maybe for previous scores etc?) Might need a new HTML page
# # logic to add new event, POST
# @app.route('/add', methods=['POST'])
# def create():
#     player_name = request.form['name']
#     player_choice = request.form['choice']
#     new_player = Player(player=player_name, choice=player_choice)
#     add_new_player(new_player)
#     return redirect('/')

# # default route for GET, remove high score
# @app.route('/remove')
# def index_2():
#     return render_template('gamestart.html', title='Rock Paper Scissors', players=players)

# # Logic to remove event, POST
# @app.route('/remove', methods=['POST'])
# def remove():
#     player_to_delete = None
#     player_name = request.form['name']
#     for player in players:
#         if player.name == player_name:
#             player_to_delete = player
#             break
#         remove_player(player_to_delete)
#     return redirect('/')
#################################################################################
