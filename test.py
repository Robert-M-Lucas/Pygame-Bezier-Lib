from PygameBezierLib import BezierCurve
import pygame

screen_size = (1000, 1000)
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

bezier = BezierCurve(3)
bezier.ControlHandles[0].pos = (100, 100)
bezier.ControlHandles[1].pos = (100, 500)
bezier.ControlHandles[2].pos = (500, 100)


held_handle = None

progress = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and held_handle is None:
            for i, h in enumerate(bezier.ControlHandles):
                if h.pos[0] - h.r <= pygame.mouse.get_pos()[0] <= h.pos[0] + h.r and h.pos[1] - h.r <= \
                        pygame.mouse.get_pos()[1] <= h.pos[1] + h.r:
                    held_handle = i
        elif event.type == pygame.MOUSEBUTTONUP:
            held_handle = None

    if held_handle is not None:
        bezier.ControlHandles[held_handle].pos = pygame.mouse.get_pos()

    progress += 0.001
    if progress > 1:
        progress = 0

    screen.fill((0, 0, 0))

    points = bezier.GetFullCurve(200)

    for p in range(len(points) - 1):
        pygame.draw.line(screen, (255, 255, 255), points[p], points[p+1])

    for h in bezier.ControlHandles:
        h.draw(screen)

    pygame.display.update()

    clock.tick(120)