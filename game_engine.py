import components
import logging

def attack(coordinates, board, ships):
    """Takes coords and attacks ships, returning true if hit (removing ship from coords), and returning false if no hit."""

    try:
        x = coordinates[0]
        y = coordinates[1]

        if board[x][y] != None:

            ships[board[x][y]] -= 1

            if ships[board[x][y]] == 0:
                del ships[board[x][y]]
                
            board[x][y] = None

            return True
        else:
            return False
        
    except IndexError as e:
            print(f"Error, list/dictionary index out of range: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error('An error occurred: %s', str(e))

def cli_coordinates_input():
    """Returns user input coordinates"""

    letter_to_number = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
    'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26}

    try:
        coords = str(input("Enter Coordinates (e.g. B4): "))
        x, y = int(letter_to_number[coords[0]]), int(coords[1])
    except ValueError:
            print("Invalid input. Please enter valid numerical coordinates.")
    else:
        return (x - 1, y - 1)

def simple_game_loop():
    """Runs the game through the console for testing"""

    print("----- WELCOME TO BATTLESHIP -----")

    board = components.initialise_board()
    ships = components.create_battleships()
    components.place_battleships(board, ships, "custom")

    print_board(board)

    while len(ships) != 0: # CHANGE

        coords = cli_coordinates_input()
        fire = attack(coords, board, ships)

        if fire:
            print("Hit!")
        elif fire == False:
            print("Miss!")
        
    print("You sunk all the ships. YOU WIN!")

def print_board(board):
    for row in board:
        print(" ".join(cell if cell is not None else "-" for cell in row))

if __name__ == "__main__":
    simple_game_loop()

