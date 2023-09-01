import pygame
import time

class Game_setup:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 720, 480
        self.WINDOW = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.CAPTION = pygame.display.set_caption("Snake Game")
        
        # Set up colors
        self.BLACK = pygame.Color(0, 0, 0)
        self.WHITE = pygame.Color(255, 255, 255)
        self.RED = pygame.Color(255, 0, 0)
        self.GREEN = pygame.Color(0, 255, 0)
        self.BLUE = pygame.Color(0, 0, 255)
        
        self.FPS = pygame.time.Clock()
        self.GAME_SPEED = 10
        
    def view(self, snake, food, score, game_over):
        self.WINDOW.fill(self.WHITE)
        
        for pos in snake.SNAKE_BODY:
            pygame.draw.rect(self.WINDOW, snake.SNAKE_COLOR, pygame.Rect(pos[0], pos[1], 20, 20))
            
        pygame.draw.rect(self.WINDOW, food.FOOD_COLOR, pygame.Rect(food.FOOD_POSITION[0], food.FOOD_POSITION[1], 20, 20))
        
        if not game_over:
            font_style = pygame.font.SysFont('times new roman', 20)
            surface = font_style.render('Score : ' + str(score), True, self.BLUE)
            surf_rect = surface.get_rect()
        else:
            font_style = pygame.font.SysFont('times new roman', 50)
            surface = font_style.render('Your Score : ' + str(score), True, self.RED)
            surf_rect = surface.get_rect()
            surf_rect.midtop = (self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/4)
            time.sleep(1)
            
        self.WINDOW.blit(surface, surf_rect)
        
        pygame.display.update()
        self.FPS.tick(self.GAME_SPEED)
