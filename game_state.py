import pygame
from enum import Enum

class GamePhase(Enum):
    RUNNING = 1
    GAME_OVER = 2

current_phase = GamePhase.RUNNING
current_score = 0

def reset():
    global current_phase, current_score
    current_phase = GamePhase.RUNNING
    current_phase = 0