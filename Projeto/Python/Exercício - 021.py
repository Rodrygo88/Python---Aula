print("====== DESAFIO 021 ======")
import pygame

file = 'musica.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
input()
pygame.event.wait()