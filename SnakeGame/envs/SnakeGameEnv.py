import pygame
from pygame.locals import *

from envs.PyGame2D import Game_setup
from envs.Component import Snake, Food

class SnakeGameEnv:
    def __init__(self):
        self.game_env = Game_setup()
        self.snake = Snake([100, 60], self.game_env.BLACK)
        self.food = Food(self.game_env.WINDOW_WIDTH, self.game_env.WINDOW_HEIGHT, self.game_env.GREEN)
        self.score = 0
        self.game_over = False
        self.running = True
    
    def event_on_game_window(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT]:
                    self.snake.DIRECTION = "LEFT"
                if event.key in [K_d, K_RIGHT]:
                    self.snake.DIRECTION = "RIGHT"
                if event.key in [K_w, K_UP]:
                    self.snake.DIRECTION = "UP"
                if event.key in [K_s, K_DOWN]:
                    self.snake.DIRECTION = "DOWN"
                
    def reset(self):
        self.food = Food(self.game_env.WINDOW_WIDTH, self.game_env.WINDOW_HEIGHT, self.game_env.GREEN)
    
    def render(self):
        self.game_env.view(self.snake, self.food, self.score, self.game_over)
        
    def step(self):
        if self.snake.DIRECTION == 'UP' and self.snake.CHANGE_TO != 'DOWN':  
            self.snake.CHANGE_TO = 'UP'  
        if self.snake.DIRECTION == 'DOWN' and self.snake.CHANGE_TO != 'UP':  
            self.snake.CHANGE_TO = 'DOWN'   
        if self.snake.DIRECTION == 'LEFT' and self.snake.CHANGE_TO != 'RIGHT':  
            self.snake.CHANGE_TO = 'LEFT'   
        if self.snake.DIRECTION == 'RIGHT' and self.snake.CHANGE_TO != 'LEFT':  
            self.snake.CHANGE_TO = 'RIGHT'
        
        # action performed to move the snake
        if self.snake.CHANGE_TO == 'UP':
            self.snake.SNAKE_POSITION[1] -= 20
        elif self.snake.CHANGE_TO == 'DOWN':
            self.snake.SNAKE_POSITION[1] += 20
        elif self.snake.CHANGE_TO == 'LEFT':
            self.snake.SNAKE_POSITION[0] -= 20
        elif self.snake.CHANGE_TO == 'RIGHT':
            self.snake.SNAKE_POSITION[0] += 20
            
        self.snake.SNAKE_BODY.insert(0, list(self.snake.SNAKE_POSITION))
        if self.snake.SNAKE_POSITION[0] == self.food.FOOD_POSITION[0] and self.snake.SNAKE_POSITION[1] == self.food.FOOD_POSITION[1]:  
            # incrementing the player's score by 1  
            self.score += 10  
            self.food.FOOD_SPAWN = False  
        else:  
            self.snake.SNAKE_BODY.pop()
            
    def check_game_over(self):
        if self.snake.SNAKE_POSITION[0] < 0 or self.snake.SNAKE_POSITION[0] > self.game_env.WINDOW_WIDTH - 10:  
            self.game_over = True
        if self.snake.SNAKE_POSITION[1] < 0 or self.snake.SNAKE_POSITION[1] > self.game_env.WINDOW_HEIGHT - 10:  
            self.game_over = True
            
        for block in self.snake.SNAKE_BODY[1:]:  
            if self.snake.SNAKE_POSITION[0] == block[0] and self.snake.SNAKE_POSITION[1] == block[1]:  
                self.game_over = True
