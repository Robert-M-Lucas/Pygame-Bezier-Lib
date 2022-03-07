import pygame
from .BezierCurve import Handle

class Handle:
    def __init__(self, color: tuple = (255, 255, 255), pos: tuple = (100, 100)):
        self.r = 10
        self.color = color
        self.pos = pos

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, self.color, self.pos, self.r)


class LerpHandle:
    def __init__(self, h1: Handle, h2: Handle, color: tuple = (0, 255, 0)):
        self.h1, self.h2 = h1, h2
        self.color = color
        self.r = 5
        self.progress = 0
        self.pos = (0, 0)

    def update(self):
        self.pos = (self.h1.pos[0] + ((self.h2.pos[0] - self.h1.pos[0]) * self.progress),
                    self.h1.pos[1] + ((self.h2.pos[1] - self.h1.pos[1]) * self.progress))

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, self.color, self.pos, self.r)
