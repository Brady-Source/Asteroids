import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class GameOverScreen:
    def __init__(self, player: "Player"):
        self.player = player
        self.font_large = pygame.font.SysFont(None, 72)
        self.font_small = pygame.font.SysFont(None, 36)
        
        self.button_width = 200
        self.button_height = 60
        self.button_rect = pygame.Rect(
            (SCREEN_WIDTH - self.button_width) // 2,
            SCREEN_HEIGHT // 2+ 40,
            self.button_width,
            self.button_height,
        )
        
    def draw(self, screen: pygame.Surface):
        #Game over text
        game_over_text = self.font_large.render("Game Over", True, (255, 255, 255))
        go_rect = game_over_text.get_rect(center=(SCREEN_WIDTH //2, SCREEN_HEIGHT //2-60))
        screen.blit(game_over_text, go_rect)
        
        #Score Text
        score_value = getattr(self.player, "score", 0)
        score_text = self.font_small.render(f"Score: {score_value}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH //2, SCREEN_HEIGHT // 2))
        screen.blit(score_text, score_rect)
        
        #Restart button
        pygame.draw.rect(screen, (100, 100, 100), self.button_rect)
        restart_text = self.font_small.render("Restart", True, (255, 255, 255))
        rt_rect = restart_text.get_rect(center=self.button_rect.center)
        screen.blit(restart_text, rt_rect)
        
    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button_rect.collidepoint(event.pos):
                return True
        return False