import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Класс дял управления ресурсами и поведением игры"""
    
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode ((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """Запуск основоного цикла инры"""
        while True:
            #Отслеживание событий клавиатуры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.settings.bg_color)    
            #Отображение последнего проресованного экрана
            pygame.display.flip()
            
if __name__ == '__main__':
    #Создание экземплара и запуск игры
    ai = AlienInvasion()
    ai.run_game()
