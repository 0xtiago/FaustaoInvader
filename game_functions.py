import sys
import pygame

def check_events():
    '''Responde aos eventos de pressionamento de teclas e de mouse'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()