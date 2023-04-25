import settings
import splashscreen
import pygame
from gameRunner import gameRunner
from gameObjs import settingsObj

user_settings = settingsObj()

pygame.init()
splashscreen.splashscreen(user_settings) #uncomment for splash screen to work, otherwise change gamerunner obj to test


