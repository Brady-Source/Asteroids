import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot


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
    
    
    pygame.font.init()
    game_font = pygame.font.SysFont("Arial", 24)
    
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("black") # Sets the BG to black
        updatable.update(dt)
        for shape in drawable:
            shape.draw(screen) # Re-render player
        
        text_score = str(player.score)
        game_font = pygame.font.SysFont("Arial", 24)
        while len(text_score) < 7:
            text_score = "0" + text_score
        text_surface = game_font.render(text_score, False, "white")
        screen.blit(text_surface, (SCREEN_WIDTH/2 , SCREEN_WIDTH/2))
        pygame.display.flip() #CALL THIS LAST - Refreshes the screen
        
        for obj in asteroids:
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                
        for obj in asteroids:
            for shot in shots:
                if shot.collides_with(obj):
                    log_event("asteroid_shot")
                    obj.split()
                    shot.kill()
                    player.score += 10
                    
        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()
