
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Landscape")

cloud_x = 150

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cloud_x += 0.07
    
    if cloud_x >= 700:
        cloud_x = -60


    screen.fill((135, 206, 235))

    # sun
    pygame.draw.circle(screen, (255, 255, 0), (640, 0), 120)

    # clouds
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x, 100), 45)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 30, 85), 55)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 50, 100), 45)

    # ground
    pygame.draw.rect(screen, (34, 139, 34), (0, 400, 640, 200))

    # path 
    pygame.draw.polygon(screen, (60, 82, 45),
     [(300, 480), (150, 480), (320,380)])

    # mountains
    pygame.draw.polygon(screen, (139, 69, 19),
     [(0, 400), (200, 200), (400, 400)])

    pygame.draw.polygon(screen, (160, 82, 45),
     [(300, 400), (500, 250), (700, 400)])

    #stick man person
    pygame.draw.circle(screen, (0, 0, 0), (320, 385), 10)

    pygame.draw.line(screen, (0, 0, 0), (320, 395), (320, 430), 4)

    pygame.draw.line(screen, (0, 0, 0), (320, 405), (300, 420), 4)
    pygame.draw.line(screen, (0, 0, 0), (320, 405), (340, 420), 4)

    pygame.draw.line(screen, (0, 0, 0), (320, 430), (305, 450), 4)
    pygame.draw.line(screen, (0, 0, 0), (320, 430), (335, 450), 4)
    
    pygame.display.flip()

pygame.quit()

