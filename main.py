from flask import Flask, render_template, request, jsonify, json
import components
from game_engine import print_board, attack
from mp_game_engine import generate_attack
app = Flask(__name__)

player_board = components.initialise_board()
player_ships = components.create_battleships()

player_attack_coords = []

ai_board = components.initialise_board()
ai_ships = components.create_battleships()
components.place_battleships(ai_board, ai_ships, "random")

if __name__ == "__main__":
    app.run()

@app.route("/", methods=['GET'])
def root():
    return render_template("main.html", player_board=player_board)

@app.route("/placement", methods=['GET', 'POST'])
def placement_interface():
    if request.method == 'POST':
        data = request.get_json()
        with open("placement.json", mode="w") as json_file:
            json.dump(data, json_file)
        components.place_battleships(player_board, player_ships, "custom")
        return jsonify({'message': 'Received'}), 200
    elif request.method == 'GET':
        return render_template("placement.html", ships=player_ships, board_size=len(player_board))

@app.route("/attack", methods=['GET'])
def process_attack():

    while True:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        player_coords = (x,y)
        if [x,y] in player_attack_coords:
            raise() # BLOCKS PLAYER FROM PRESSING THE SAME COORDINATE MULTIPLE TIMES BUT SENDS A TYPEERROR
        else:
            player_attack_coords.append([x,y])
            break

    fire_player = attack(player_coords, ai_board, ai_ships)
    
    ai_coords = generate_attack(player_board)
    attack(ai_coords, player_board, player_ships)

    if len(player_ships) == 0:
        return jsonify({'hit': fire_player, 'AI_Turn': ai_coords, 'finished': "Game Over AI wins"})
    elif len(ai_ships) == 0:
        return jsonify({'hit': fire_player, 'AI_Turn': ai_coords, 'finished': "Game Over Player wins"})
    else:
        return jsonify({'hit': fire_player,'AI_Turn': ai_coords})


    

