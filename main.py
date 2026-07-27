import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import game_state
from game_state import GamePhase
from game_over_screen import GameOverScreen


def main():
    pygame.init()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, drawable, updatable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0)
    
    game_over_screen = GameOverScreen(player)
    
    pygame.font.init()
    game_font = pygame.font.SysFont("Arial", 24)
    
    running = True
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if game_state.current_phase == GamePhase.GAME_OVER:
                if game_over_screen.handle_event(event):
                    game_state.reset()
                    player.position.update(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    player.score = 0
                    updatable.empty()
                    drawable.empty()
        
        if game_state.current_phase == GamePhase.RUNNING:
            screen.fill("black")
            updatable.update(dt)
            for shape in drawable:
                shape.draw(screen)
        elif game_state.current_phase == GamePhase.GAME_OVER:
            screen.fill("black")
            game_over_screen.draw(screen)

        
        if game_state.current_phase == GamePhase.RUNNING:
            for obj in asteroids:
                if player.collides_with(obj):
                    log_event("player_hit")
                    game_state.current_phase = GamePhase.GAME_OVER
                    
            for obj in asteroids:
                for shot in shots:
                    if shot.collides_with(obj):
                        log_event("asteroid_shot")
                        obj.split()
                        shot.kill()
                        player.score += 10
                    
        dt = clock.tick(60) /1000
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
