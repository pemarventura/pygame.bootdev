#import the library

import pygame
import player
import asteroid
import asteroidField
import shot

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    time = pygame.time.Clock()  # Set the frame rate to 60 FPS

    dt  = 0

    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)

    asteroidField.AsteroidField.containers = updatable

    asteroidfieldRender = asteroidField.AsteroidField()
    
    playerRender = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    shotable = pygame.sprite.Group()

    shot.Shot.containers = (shotable, drawable, updatable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        updatable.update(dt)
        for ast in asteroids:
            if ast.checkCollision(playerRender):
                print("Game over!")
                pygame.quit()
            for sht in shotable:
                if sht.checkCollision(ast):
                    ast.split()
                    sht.kill()

        screen.fill((0, 0, 0))
        for drw in drawable:
            drw.draw(screen)
        pygame.display.flip()
        delta = time.tick(60)
        dt = delta / 1000.0
        

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
   main()