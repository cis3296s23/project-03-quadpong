import pygame
def SETTINGS():

    # initialize pygame
    pygame.init()

    # set window size
    info = pygame.display.Info()
    win_width = info.current_w
    win_height = info.current_h

    # set small window size
    small_win_width = int(win_width / 3.2)
    small_win_height = int(win_height / 3.2)

    # create small window
    small_window = pygame.display.set_mode((small_win_width, small_win_height))

    # set font for text
    medium_font = pygame.font.Font(None, 100)
    small_font = pygame.font.Font(None, 64)

    # set text for small window
    option1_text = medium_font.render("Ball Speed", True, (255, 255, 255))
    option2_text = medium_font.render("Points to Win", True, (255, 255, 255))
    quit_text = small_font.render("Quit", True, (255, 255, 255))

    # set position for small window text
    option1_pos = option1_text.get_rect()
    option1_pos.center = (small_window.get_rect().centerx, small_window.get_rect().centery - 50)

    option2_pos = option2_text.get_rect()
    option2_pos.center = (small_window.get_rect().centerx, small_window.get_rect().centery + 50)

    quit_pos = quit_text.get_rect()
    quit_pos.bottomleft = (10, small_win_height - 10)

    # display small window until user clicks quit button or closes the window
    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # check for mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_pos.collidepoint(event.pos):  # if user clicks quit button
                    pygame.quit()
                    quit() # some python code needs to be replaced, so it takes you back to the main menu
                    # after quitting any settings need to be updated
                elif option1_pos.collidepoint(event.pos): # if user clicks option 1
                    print("Ball Speed selected(Add feature later")
                elif option2_pos.collidepoint(event.pos): # if user clicks option 2
                    print("Point To Win selected(Add feature later")

        # fill small window with background color
        small_window.fill((0, 0, 0))

        # display small window text
        small_window.blit(option1_text, option1_pos)
        small_window.blit(option2_text, option2_pos)
        small_window.blit(quit_text, quit_pos)

        # update display for small window
        pygame.display.update()
