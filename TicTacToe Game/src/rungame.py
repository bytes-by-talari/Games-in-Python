
# run_tic_tac_toe.py

import pygame
import sys
from tic_tac_toe import *
from algos import *
# import time

pygame.init()

print("\nWelcome to Abhinav's\'s TicTacToe!\n")

while True:
    
    window = open_window() # open window
    create_board(window) # create board
    state = ["0", "1", "2", "3", "4", "5", "6", "7", "8"] # initialize board state
    terminal_state = False # initialize terminal state

    ai = choose_ai() # choose algo: random, minimax, full alpha-beta
    
    
    while not terminal_state:
        
        for event in pygame.event.get():
            
            # if quit event
            if event.type == pygame.QUIT: 
                 sys.exit(0) # close window     
                 
            # if mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN: 
                
                # human player goes
                player = "X"

                pos = pygame.mouse.get_pos() 
                region = map_to_grid(pos)  
                empty_regions = find_empty_regions(state) # find empty regions
                                
                  
                if str(region) in empty_regions:
                    place_on_grid(window, region, player)
                    state[region] = player # update board state
                    empty_regions = find_empty_regions(state) 
                    game_over = terminal_test(state, player) # check for terminal state
  
                    if game_over:
                        pygame.event.get()
                        terminal_state = play_again()
                        
               
                    player = "O"
    
                    if len(empty_regions) != 0:

                       
                        if ai == 1:
                            ai_region = random_ai(empty_regions) 

                 
                        if ai == 2:
                            my_state = state[:] 
                            best = minimax(my_state, player)
                            ai_region = int(best[0])

  
                        if ai == 3:
                            my_state = state[:] 
                            best = alphabeta(my_state, -float("inf"), float("inf"), player)
                            ai_region = int(best[0])

                        if ai == 4:
                            my_state = state[:]  
                            best = alphabeta_cutoff(my_state, -float("inf"), float("inf"), 0, player)
                            ai_region = int(best[0])


                        place_on_grid(window, ai_region, player) 
                        state[ai_region] = player

                       

                        game_over = terminal_test(state,player) 

                       
                        if game_over:
                            pygame.event.get()
                            terminal_state = play_again()

    
      
pygame.quit()