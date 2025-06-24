import pygame 
W = 750 
H = 750 
window = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()











while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()














    pygame.display.update()
    clock.tick(24)

