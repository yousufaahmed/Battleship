import random, json
import logging

# ADD ERROR HANDLING FOR EVERY PAGE

def initialise_board(size = 10):
    """Initialises the board and returns an array containing the state of the board.""" # MODIFY THIS 

    board = []

    try:
        for _ in range(size):
            row = [None for _ in range(size)]
            board.append(row) # CREATES A NONE VALUE 2D ARRAY OF SIZE i * j
    except TypeError as e:
        raise TypeError(f"Error initialising board: {e}") # RAISING AN ERROR HAULTS THE PROGRAM
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 
        logging.error('An error occurred: %s', str(e))
    else:
        return board

def create_battleships(filename = "battleships.txt"):
    """Creates a dictionary using a txt file containing ships and their sizes"""

    battleships = {}

    try:
        with open(filename, mode="r") as file: # READS THE FILE AND AUTO CLOSES AFTER USING IT
                
            contents = file.readlines()

            # .STRIP REMOVES ANY WHITESPACES BEFORE OR AFTER THE KEY VALUE PAIR, .SPLIT SPLITS THE KEY VALUE PAIR SEPARATED BY THE COLON INTO 2 VARIABLES
            for line in contents:
                key, value = str(line).strip().split(":") 
                battleships[key] = int(value)

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except IndexError:
        print("Invalid data format in the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error('An error occurred: %s', str(e))
    else:
        return battleships

def place_battleships(board, ships, algorithm = "simple"):
    """Places battleships onto the board according to a placement algorithm (simple, random, custom)"""

    keys = []
    for ship in ships:
        keys.append(ship)
    
    # PLACES THE SHIPS ON SEPARATE LINES NEXT TO EACHOTHER FOR TESTING
    if algorithm == "simple":
        try:
            for i in range(len(ships)):
                for j in range(ships[keys[i]]):
                    board[i][j] = keys[i]
        except IndexError as e:
            print(f"Error placing battleship {ship}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logging.error('An error occurred: %s', str(e))

    # PLACES SHIPS ONTO THE BOARD RANDOMLY
    elif algorithm == "random":
        try:
            for ship_name, ship_size in ships.items():
                placed = False
                while not placed:
                    x = random.randint(0, len(board) - 1)
                    y = random.randint(0, len(board[0]) - ship_size)
                    orientation = random.choice(["horizontal", "vertical"])
                    if orientation == "horizontal" and x + ship_size <= len(board[0]): # CHECKS IF SHIP IS GOING OVER THE GRID
                        if all(board[y][x + i] == None for i in range(ship_size)):
                            for i in range(ship_size):
                                board[y][x + i] = ship_name
                                placed = True
                    elif orientation == "vertical" and y + ship_size <= len(board):
                        if all(board[y + i][x] == None for i in range(ship_size)):
                            for i in range(ship_size):
                                board[y + i][x] = ship_name
                                placed = True
        except IndexError as e:
            print(f"Error placing battleship {ship_name}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logging.error('An error occurred: %s', str(e))

    # TAKES A JSON PLACEMENT FILE AND USES THAT TO PLACE THE SHIPS ONTO THE BOARD
    elif algorithm == "custom":

        placements = {}

        try:
            with open("placement.json", mode="r") as file:
                contents = json.load(file)

                for key, value in contents.items():
                    placements[key] = value

            # REPLACES THE EXISTING BOARD WITH THE BOARD CONFIGURATION FROM THE PLACEMENT.JSON FILE
            for ship, position in placements.items():
                x, y, orientation = position
                x, y = int(x), int(y)
                ship_size = ships[ship]

                if orientation == "h":
                    for i in range(ship_size):
                        board[y][x + i] = ship
                elif orientation == "v":
                    for i in range(ship_size):
                        board[y + i][x] = ship
                        
        except FileNotFoundError:
            print(f"The file 'placement.json' was not found.")
        except IndexError:
            print("Invalid data format in the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logging.error('An error occurred: %s', str(e))
    
    return board
