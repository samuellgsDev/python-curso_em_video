# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# Make a Python program that opens and plays the audio from an MP3 file.
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
