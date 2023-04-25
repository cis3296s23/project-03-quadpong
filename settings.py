import pygame
import os
import splashscreen
import gameObjs

def settings(user_settings):
    # initialize pygame
    #pygame.init()

    # set window size
    info = pygame.display.Info()
    win_width = info.current_w
    win_height = info.current_h

    # set small window size
    small_win_width = int(win_width)
    small_win_height = int(win_height)

    # center window
    os.environ['SDL_VIDEO_CENTERED'] = '0'

    # create small window
    small_window = pygame.display.set_mode((small_win_width, small_win_height))

    # set font for text
    medium_font = pygame.font.Font(None, 100)
    small_font = pygame.font.Font(None, 64)

    # set text for small window
    option1_text = medium_font.render("Ball Speed", True, (255, 255, 255))
    option1_value = medium_font.render(f"{user_settings.ball_speed}", True, (255, 255, 255))
    option1_left = medium_font.render("<", True, (255, 255, 255))
    option1_right = medium_font.render(">", True, (255, 255, 255))

    option2_text = medium_font.render("Ball Count", True, (255, 255, 255))
    option2_value = medium_font.render(f"{user_settings.ball_count}", True, (255, 255, 255))
    option2_left = medium_font.render("<", True, (255, 255, 255))
    option2_right = medium_font.render(">", True, (255, 255, 255))

    option3_text = medium_font.render("Points to Win", True, (255, 255, 255))
    option3_value = medium_font.render(f"{user_settings.points_to_win}", True, (255, 255, 255))
    option3_left = medium_font.render("<", True, (255, 255, 255))
    option3_right = medium_font.render(">", True, (255, 255, 255))

    quit_text = small_font.render("Back", True, (255, 255, 255))

    # set position for small window text
    option1_pos = option1_text.get_rect()
    option1_pos.center = (small_window.get_rect().centerx, small_window.get_rect().centery - 200)
    
    option1_left_pos = option1_left.get_rect()
    option1_left_pos.center = (small_window.get_rect().centerx - 100, small_window.get_rect().centery - 125)
    
    option1_right_pos = option1_right.get_rect()
    option1_right_pos.center = (small_window.get_rect().centerx + 100, small_window.get_rect().centery - 125)
    
    option1_value_pos = option1_value.get_rect()
    option1_value_pos.center = (small_window.get_rect().centerx, small_window.get_rect().centery - 125)

    option2_pos = option2_text.get_rect()
    option2_pos.center = (small_window.get_rect().centerx, small_window.get_rect().centery)
    
    option2_left_pos = option2_left.get_rect()
    option2_left_pos.center = (small_window.get_rect().centerx - 100, small_window.get_rect().centery + 75)
    
    option2_right_pos = option2_right.get_rect()
    option2_right_pos.center = (small_window.get_rect().centerx + 100, small_window.get_rect().centery + 75)
    
    option2_value_pos = option2_value.get_rect()
    option2_value_pos.center = (small_window.get_rect().centerx, small_window.get_rect().centery + 75)

    option3_pos = option3_text.get_rect()
    option3_pos.center = (small_window.get_rect().centerx, small_window.get_rect().centery + 200 )

    option3_left_pos = option3_left.get_rect()
    option3_left_pos.center = (small_window.get_rect().centerx - 100, small_window.get_rect().centery + 275)
    
    option3_right_pos = option3_right.get_rect()
    option3_right_pos.center = (small_window.get_rect().centerx + 100, small_window.get_rect().centery + 275)
    
    option3_value_pos = option3_value.get_rect()
    option3_value_pos.center = (small_window.get_rect().centerx, small_window.get_rect().centery + 275)

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
                    splashscreen.splashscreen(user_settings)
                    return user_settings
                
                elif option1_left_pos.collidepoint(event.pos): # if user clicks option 1 decrement
                    if(user_settings.ball_speed > 1):
                        user_settings.ball_speed-=1
                    option1_value = medium_font.render(f"{user_settings.ball_speed}", True, (255, 255, 255))
                    small_window.blit(option1_value, option1_value_pos)

                elif option1_right_pos.collidepoint(event.pos): # if user clicks option 1 increment
                    user_settings.ball_speed+=1   
                    option1_value = medium_font.render(f"{user_settings.ball_speed}", True, (255, 255, 255))
                    small_window.blit(option1_value, option1_value_pos)

                elif option2_left_pos.collidepoint(event.pos): # if user clicks option 1 decrement
                    if(user_settings.ball_count > 1):
                        user_settings.ball_count-=1
                    option2_value = medium_font.render(f"{user_settings.ball_count}", True, (255, 255, 255))
                    small_window.blit(option2_value, option2_value_pos)

                elif option2_right_pos.collidepoint(event.pos): # if user clicks option 1 increment
                    if(user_settings.ball_count <= 9):  
                        user_settings.ball_count+=1   
                    option2_value = medium_font.render(f"{user_settings.ball_count}", True, (255, 255, 255))
                    small_window.blit(option2_value, option2_value_pos)

                elif option3_left_pos.collidepoint(event.pos): # if user clicks option 2 decrement
                    if(user_settings.points_to_win > 1):
                        user_settings.points_to_win-=1
                    option3_value = medium_font.render(f"{user_settings.points_to_win}", True, (255, 255, 255))
                    small_window.blit(option3_value, option3_value_pos)

                elif option3_right_pos.collidepoint(event.pos): # if user clicks option 2 increment
                    user_settings.points_to_win+=1
                    option3_value = medium_font.render(f"{user_settings.points_to_win}", True, (255, 255, 255))
                    small_window.blit(option3_value, option3_value_pos)

        # fill small window with background color
        small_window.fill((0, 0, 0))

        # display small window text
        small_window.blit(option1_text, option1_pos)
        small_window.blit(option1_right, option1_right_pos)
        small_window.blit(option1_left, option1_left_pos)
        small_window.blit(option1_value, option1_value_pos)
        small_window.blit(option2_text, option2_pos)
        small_window.blit(option2_right, option2_right_pos)
        small_window.blit(option2_left, option2_left_pos)
        small_window.blit(option2_value, option2_value_pos)
        small_window.blit(option3_text, option3_pos)
        small_window.blit(option3_right, option3_right_pos)
        small_window.blit(option3_left, option3_left_pos)
        small_window.blit(option3_value, option3_value_pos)
        small_window.blit(quit_text, quit_pos)

        # update display for small window
        pygame.display.update()
