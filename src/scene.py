import pygame
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT



class Scene:
    def __init__(self, assets):
        self.current_scene = assets["menuscreen_art"]
        self.assets = assets
        self.scene_active = False
        self.previous_scene = None


    def load_map(self, map):
        if map not in self.assets:
            raise NotImplementedError("This map hasn't been implemented")
        self.current_scene = pygame.transform.scale(self.assets[map], (SCREEN_WIDTH, MAP_HEIGHT))

    def show_scene(self, scene):
        self.previous_scene = self.current_scene
        if scene not in self.assets:
            raise NotImplementedError("This scene hasn't been implemented")
        self.current_scene = pygame.transform.scale(self.assets[scene], (SCREEN_WIDTH, MAP_HEIGHT))
        self.scene_active = True


    def clear_scene(self):
        if self.scene_active:
            self.current_scene = self.previous_scene
            self.previous_scene = None
            self.scene_active = False


    def draw(self, screen):
        screen.blit(self.current_scene, (0, 0))


        


    
