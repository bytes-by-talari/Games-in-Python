


import pygame
import sys

# color definitions

white = (255,255,255)
black = (0,0,0)
green =(50,205,50)


# define window size and line thickness
window_x = 500
window_y = 500
line_thickness = 3

# open pygame window
def open_window():
    screen = pygame.display.set_mode((window_x,window_y))
    pygame.display.set_caption('Abhinav\'s TicTacToe')
    return screen

# create game board
def create_board(screen):
    screen.fill(white)
    pygame.draw.rect(screen, black, (0, 0, window_x, window_y), line_thickness*3)
    pygame.draw.rect(screen, black, (0, 0, window_x, window_y/3), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, window_x, window_y*2/3), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, window_x/3, window_y), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, window_x*2/3, window_y), line_thickness)
    pygame.display.update()

# map mouse click to grid
def map_to_grid(pos):
    x = pos[0]
    y = pos[1]
    #print("x: " + str(x) )
    #print("y: " + str(y) )
    if x < window_x / 3:
        if y < window_y / 3:
            region = 0
        elif (window_y/3 < y) and (y < window_y*2/3):
            region = 3
        else:
            region = 6
    elif (window_x/3 < x) and (x < window_x * 2 / 3):
        if y < window_y / 3:
            region = 1
        elif (window_y/3 < y) and (y < window_y*2/3):
            region = 4
        else:
            region = 7
    else:
        if y < window_y / 3:
            region = 2
        elif (window_y/3 < y) and (y < window_y*2/3):
            region = 5
        else:
            region = 8
    return region
    
# place marker on grid
def place_on_grid(screen, region, player):
    
    font_size = 180
    font_family = 'Calibri'
    
    if player == "X":
        color = black
        offset_x = 55
        offset_y = 20
    if player == "O":
        color = green
        offset_x = 45
        offset_y = 20
    
    myfont = pygame.font.SysFont(font_family, font_size)
    textsurface = myfont.render(player, True, color) 
    
    if region == 0:
        pass
    if region == 1:
        offset_x = offset_x + window_x / 3
    if region == 2:
        offset_x = offset_x + ( window_x * 2 / 3 )
    if region == 3:
        offset_y = offset_y + window_y / 3
    if region == 4:
        offset_x = offset_x + window_x / 3
        offset_y = offset_y + window_y / 3
    if region == 5:
        offset_x = offset_x + ( window_x * 2 / 3 )
        offset_y = offset_y + window_y / 3
    if region == 6:
        offset_y = offset_y + ( window_y * 2 / 3 )
    if region == 7:
        offset_x = offset_x + window_x / 3
        offset_y = offset_y + ( window_y * 2 / 3 )
    if region == 8:
        offset_x = offset_x + ( window_x * 2 / 3 )
        offset_y = offset_y + ( window_y * 2 / 3 )

    screen.blit(textsurface,(offset_x, offset_y))
    pygame.display.update() 


def get_opponent(player):
    if player == "X":
        return "O"
    else:
        return "X"


def find_empty_regions(state):
    empty_regions = []
    for i in range(0, len(state)):
        if (state[i] != "X") and (state[i] != "O"):
            empty_regions.append(state[i])
    return empty_regions

def terminal_test(state, player):
    empty_regions = find_empty_regions(state)
    if (state[0] == player and state[1] == player and state[2] == player) or \
            (state[3] == player and state[4] == player and state[5] == player) or \
            (state[6] == player and state[7] == player and state[8] == player) or \
            (state[0] == player and state[3] == player and state[6] == player) or \
            (state[1] == player and state[4] == player and state[7] == player) or \
            (state[2] == player and state[5] == player and state[8] == player) or \
            (state[0] == player and state[4] == player and state[8] == player) or \
            (state[2] == player and state[4] == player and state[6] == player):
        print("Game over! " + player + " wins!")
        return True
    elif len(empty_regions) == 0:
        print("Game over! Draw!")
        return True

def choose_ai():
    while True:
        sys.stdout.write("Choose AI. [1/2/3/4]\n1. Random\n2. Minimax\n3. Full Alpha-Beta\n4. Alpha-Beta with Cutoff\n> ")
        answer = input().lower()
        if answer == "1":
            return 1
        elif answer == "2":
            return 2
        elif answer == "3":
            return 3
        elif answer == "4":
            return 4
        else:
            sys.stdout.write("Please respond with '1', '2', '3', or '4'.\n")


def play_again():
    while True:
        pygame.display.update()
        sys.stdout.write("Play again? [Y/N]\n> ")
        answer = input().lower()
        if (answer == "y"):
            terminal_state = True
            return terminal_state
        elif (answer == "n"):
            sys.exit(0)
        else:
            sys.stdout.write("Please respond with 'Y' or 'N'.\n")

