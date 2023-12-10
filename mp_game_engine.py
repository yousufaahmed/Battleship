import random
import components
from game_engine import cli_coordinates_input, attack, print_board

players = {}
picked_coords=[]

def generate_attack(board): # CHANGE TO HAVE REAL AI
    """Generates coordinates via an AI to attack players ship."""

    while True:
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board[0]) - 1)  # RANDOM IS NOT AI!!!!!
        if [x,y] not in picked_coords:
            picked_coords.append([x,y])
            break
    
    return (x,y)

def ai_opponent_game_loop():
    """Runs a Player vs AI battleship game in the command line for testing."""

    print("----- WELCOME TO BATTLESHIP MULTIPLAYER -----")

    username = str(input("Enter username: "))

    # INITIALISE PLAYER BOARD AND SHIPS
    player_board = components.initialise_board()
    player_ships = components.create_battleships()
    components.place_battleships(player_board, player_ships)

    # INITIALISE AI BOARD AND SHIPS
    ai_board = components.initialise_board()
    ai_ships = components.create_battleships()
    components.place_battleships(ai_board, ai_ships, "random")

    players[username] = {'board': player_board, 'battleships': player_ships}
    players["AI Opponent"] = {'board': ai_board, 'battleships': ai_ships}

    while len(player_ships) and len(ai_ships) != 0:
        
        player_coords = cli_coordinates_input()
        fire_player = attack(player_coords, ai_board, ai_ships)
        
        if fire_player:
            print("Player Hit!")
        elif fire_player == False:
            print("Player Miss!")

        ai_coords = generate_attack(player_board)
        fire_ai = attack(ai_coords, player_board, player_ships)

        if fire_ai:
            print("AI Hit!")
        elif fire_ai == False:
            print("AI Missed!")

        print_board(player_board)

    # WIN OR LOSE TEXT OUTPUT
    if len(player_ships) == 0:
        print("YOU LOST!!! BETTER LUCK NEXT TIME!")
    elif len(ai_ships) == 0:
        print("YOU WON!!! CONGRATULATIONS!")

if __name__ == "__main__":
    ai_opponent_game_loop()