import pygame

pygame.init()
print('=' * 12 + 'Desafio 21' + '=' * 12)
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
pygame.event.wait()