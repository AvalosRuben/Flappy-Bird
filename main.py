import pygame

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Flappy Bird ;)")

done = False

clock = pygame.time.Clock() #to control how fast the display refreshes

while not done:
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT:
            
            done = True

    #Game logic

    #Drawing logic
    screen.fill((255,255,255)) #just white color
    pygame.draw.circle(screen,(0,0,255),(400,300), 50)

        #update the screen
    pygame.display.flip()

    clock.tick(60) #fps

pygame.quit()