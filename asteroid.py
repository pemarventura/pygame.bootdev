import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        circleshape.CircleShape.__init__(self, x, y , radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        random_angle = random.uniform(20,50)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        vector_one = self.velocity.rotate(random_angle)

        vector_two = self.velocity.rotate(-(random_angle))

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector_one * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector_two * 1.2

        self.kill()








        