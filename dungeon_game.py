# To add:
## Change your player to a dictionary with a key that holds onto where the player has been. Then, when drawing the map, show . for every cell they've been in.
## Add more cells
## Move the monster randomly after the player moves
## Show the monster
## Keep a scoreboard for multiple plays
## Add a second or third monster
## Add a debug mode to show were the monster (s) and door are all the time

import random
import os

CELLS = [
    (0,0), (1,0), (2,0), (3,0), (4,0),
    (0,1), (1,1), (2,1), (3,1), (4,1),
    (0,2), (1,2), (2,2), (3,2), (4,2),
    (0,3), (1,3), (2,3), (3,3), (4,3),
    (0,4), (1,4), (2,4), (3,4), (4,4)
]

def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    # move is string: LEFT = x-1, RIGHT = x+1, UP = y-1, DOWN = y+1
    x, y = player
    if move == "LEFT":
        x -= 1
    elif move == "RIGHT":
        x += 1
    elif move == "UP":
        y -= 1
    elif move == "DOWN":
        y += 1
    return (x, y)

def get_moves(player):
    # can't move: up if y==0, down if y==4, left x==0, right x==4
    avail_moves = ["LEFT","RIGHT","UP","DOWN"]
    x, y = player
    if y == 0:
        avail_moves.remove("UP")
    if y == 4:
        avail_moves.remove("DOWN")
    if x == 0:
        avail_moves.remove("LEFT")
    if x == 4:
        avail_moves.remove("RIGHT")
    return avail_moves

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def draw_grid(player):
    print(" _"*5)
    tile = "|{}"
    
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)
    
def game_loop():
    player, door, monster = get_locations()
    playing = True
    
    while playing:
        clear_screen()
        valid_moves = get_moves(player)
        
        draw_grid(player)
        print("You are currently in room {}".format(player))
        print("You can move: {}".format(', '.join(valid_moves)))
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()

        if move == "QUIT":
            print("\n **THanks for playing!**\n")
            break
        elif move in valid_moves:
            player = move_player(player, move)
            
            if player == monster:
                print("\n **You found the monster! You lose...**\n")
                playing = False
            if player == door:
                print("\n **You found the door! You win!**\n")
                playing = False
        else:
            input("That is an invalid move, try again.\n")
    else:
        if input("Play again? [Y/N]").lower() != "n":
            game_loop()
        else:
            print("\n **Thanks for playing!**\n")

#Run game!
clear_screen()
print("**Welcome to the dungeon!**")
input("Press enter to start...")
clear_screen()

game_loop()