import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPEED_UP_RATE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_angles = (self.velocity.rotate(angle), self.velocity.rotate(-angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroids = (
            Asteroid(self.position[0], self.position[1], new_radius),
            Asteroid(self.position[0], self.position[1], new_radius),
        )
        new_asteroids[0].velocity = new_angles[0] * ASTEROID_SPEED_UP_RATE
        new_asteroids[1].velocity = new_angles[1] * ASTEROID_SPEED_UP_RATE
