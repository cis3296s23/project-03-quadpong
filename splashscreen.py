import pygame
import settings
from gameRunner import gameRunner

def splashscreen(user_settings):

    # set window size
    info = pygame.display.Info()
    win_width = info.current_w
    win_height = info.current_h

    window = pygame.display.set_mode((win_width, win_height))

    # set font for text
    big_font = pygame.font.Font(None, 300)
    medium_font = pygame.font.Font(None, 128)
    small_font = pygame.font.Font(None, 64)

    # set text for splash screen
    title_text = big_font.render("Quad Pong", True, (255, 255, 255))


    #2 Player Options
    option1_text = medium_font.render("2 Player", True, (255, 255, 255))

    twoPlayerClassic_text = small_font.render("Classic", True, (255, 255, 255))
    twoPlayerRally_text = small_font.render("Rally", True, (255, 255, 255))


    #4 Player Options
    option2_text = medium_font.render("4 Player", True, (255, 255, 255))

    fourPlayerClassic_text = small_font.render("Classic", True, (255, 255, 255))
    fourPlayerRally_text = small_font.render("Rally", True, (255, 255, 255))
    fourPlayerFFA_text = small_font.render("FFA", True, (255, 255, 255))

    #Extra Options
    settings_text = small_font.render("Settings", True, (255, 255, 255))
    button_text = small_font.render("Exit", True, (255, 255, 255))

    # set position for text
    title_pos = title_text.get_rect()
    title_pos.centerx = window.get_rect().centerx
    title_pos.top = 100


    #set position for Two Player Modes
    option1_pos = option1_text.get_rect()
    option1_pos.center = (window.get_rect().centerx, window.get_rect().centery - 80)

    twoPlayerClassic_pos = twoPlayerClassic_text.get_rect()
    twoPlayerClassic_pos.center = (window.get_rect().centerx - 100, window.get_rect().centery)

    twoPlayerRally_pos = twoPlayerClassic_text.get_rect()
    twoPlayerRally_pos.center = (window.get_rect().centerx + 150, window.get_rect().centery)


    #set position for Four Player Modes
    option2_pos = option2_text.get_rect()
    option2_pos.center = (window.get_rect().centerx, window.get_rect().centery + 100)

    fourPlayerClassic_pos = fourPlayerClassic_text.get_rect()
    fourPlayerClassic_pos.center = (window.get_rect().centerx - 200, window.get_rect().centery + 180)

    fourPlayerFFA_pos = fourPlayerFFA_text.get_rect()
    fourPlayerFFA_pos.center = (window.get_rect().centerx, window.get_rect().centery + 180)

    fourPlayerRally_pos = fourPlayerRally_text.get_rect()
    fourPlayerRally_pos.center = (window.get_rect().centerx + 200, window.get_rect().centery + 180)


    #set position for other options
    settings_pos = settings_text.get_rect()
    settings_pos.bottomleft = (50, win_height - 50)

    button_pos = button_text.get_rect()
    button_pos.bottomright = (win_width - 50, win_height - 50)



    # display splash screen until user clicks exit button or closes the window
    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # check for mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_pos.collidepoint(event.pos):  # if user clicks exit button
                    pygame.quit()
                    quit()

                elif twoPlayerClassic_pos.collidepoint(event.pos): # if user clicks two player classic
                    pygame.quit()
                    game = gameRunner("twoplayer", user_settings.points_to_win, user_settings.ball_count, user_settings.ball_speed)
                    game = None
                    
                elif twoPlayerRally_pos.collidepoint(event.pos): # if user clicks 2p rally
                    pygame.quit()
                    game = gameRunner("2pRally", user_settings.points_to_win, user_settings.ball_count, user_settings.ball_speed)
                    game = None

                elif fourPlayerClassic_pos.collidepoint(event.pos): # if user clicks 4p classic
                    pygame.quit()

                    game = gameRunner("fourplayer", user_settings.points_to_win, user_settings.ball_count, user_settings.ball_speed)
                    game = None
                    
                elif fourPlayerFFA_pos.collidepoint(event.pos): # if user clicks 4p FFA
                    pygame.quit()
                    game = gameRunner("4pFFA", user_settings.points_to_win, user_settings.ball_count, user_settings.ball_speed)
                    game = None
                    
                elif fourPlayerRally_pos.collidepoint(event.pos): # if user clicks Rally
                    pygame.quit()
                    game = gameRunner("4pRally", user_settings.points_to_win, user_settings.ball_count, user_settings.ball_speed)
                    game = None
                    
                elif settings_pos.collidepoint(event.pos): # if user clicks settings button
                    settings.settings(user_settings)
                    print("Settings Selected(Add code for settings window later)")

        # display text and button
        window.blit(title_text, title_pos)

        window.blit(option1_text, option1_pos)
        window.blit(twoPlayerClassic_text, twoPlayerClassic_pos)
        window.blit(twoPlayerRally_text, twoPlayerRally_pos)

        window.blit(option2_text, option2_pos)
        window.blit(fourPlayerClassic_text, fourPlayerClassic_pos)
        window.blit(fourPlayerRally_text, fourPlayerRally_pos)
        window.blit(fourPlayerFFA_text, fourPlayerFFA_pos)

        window.blit(settings_text, settings_pos)
        window.blit(button_text, button_pos)

        # update display
        pygame.display.update()