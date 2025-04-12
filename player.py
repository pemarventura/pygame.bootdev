import circleshape
import constants
import pygame

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        circleshape.CircleShape.__init__(self, x, y, constants.PLAYER_RADIUS)
    
    rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    
    
