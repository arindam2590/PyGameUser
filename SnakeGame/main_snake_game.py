from envs.SnakeGameEnv import SnakeGameEnv

def main():
    SnakeGame = SnakeGameEnv()
    while SnakeGame.running:
        SnakeGame.event_on_game_window()
        SnakeGame.step()
        
        if not SnakeGame.food.FOOD_SPAWN:
            SnakeGame.reset()
        
        SnakeGame.check_game_over()    
        SnakeGame.render()
    
    quit()
    
if __name__ == '__main__':
    main()
