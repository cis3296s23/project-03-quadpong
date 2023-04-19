import pygame
import splashscreenSETTINGS

def splashscreen():

    # initialize pygame
    pygame.init()

    # set window size
    #win_width = 1920
    #win_height = 1080
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
    option1_text = medium_font.render("2 Player", True, (255, 255, 255))
    option2_text = medium_font.render("4 Player", True, (255, 255, 255))
    settings_text = small_font.render("Settings", True, (255, 255, 255))
    button_text = small_font.render("Exit", True, (255, 255, 255))

    # set position for text
    title_pos = title_text.get_rect()
    title_pos.centerx = window.get_rect().centerx
    title_pos.top = 100

    option1_pos = option1_text.get_rect()
    option1_pos.center = (window.get_rect().centerx, window.get_rect().centery - 50)

    option2_pos = option2_text.get_rect()
    option2_pos.center = (window.get_rect().centerx, window.get_rect().centery + 50)

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
                elif option1_pos.collidepoint(event.pos): # if user clicks option 1
                    print("2 Player Selected(Add path for game later)")
                elif option2_pos.collidepoint(event.pos): # if user clicks option 2
                    print("4 Player Selected(Add path for game later)")
                elif settings_pos.collidepoint(event.pos): # if user clicks settings button
                    splashscreenSETTINGS.SETTINGS()
                    print("Settings Selected(Add code for settings window later)")

        # display text and button
        window.blit(title_text, title_pos)
        window.blit(option1_text, option1_pos)
        window.blit(option2_text, option2_pos)
        window.blit(settings_text, settings_pos)
        window.blit(button_text, button_pos)

        # update display
        pygame.display.update()
