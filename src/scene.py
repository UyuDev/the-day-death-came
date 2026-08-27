import pygame
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT



class Scene:
    def __init__(self, assets):
        self.current_scene = assets["menuscreen_art"]
        self.assets = assets



    def load_map(self, map):
        # instead checks assets for the respective image
        if map not in self.assets:
            raise NotImplementedError("This map hasn't been implemented")
        self.current_scene = pygame.transform.scale(self.assets[map], (SCREEN_WIDTH, MAP_HEIGHT))


                    

    def draw(self, screen):
        screen.blit(self.current_scene, (0, 0))




    
