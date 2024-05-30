import pygame
from obstacle import Obstacle

pygame.init()

#screen
screen_width = 1250
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird ;)")

#physics variables:
speed = 0
object_x = screen_width//2
object_y = screen_height//2
gravity = 10
dt = 0.2 #measure of the time interval between each update of the simulation's state
jump_force = -45

#obstacles
obstacle_x = screen_width
obstacle_y = screen_height
obstacle_one = Obstacle (obstacle_x, obstacle_y, 20)

done = False

clock = pygame.time.Clock() #to control how fast the display refreshes

while not done:
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT:#quit the game
            
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed = jump_force

    #Game logic
    speed = speed + gravity*dt
    object_y = object_y + speed*dt

    if object_y > screen_height:
        object_y = screen_height

    #Drawing logic
    screen.fill((255,255,255)) #just white color
    pygame.draw.circle(screen,(0,0,255),(object_x,int(object_y)), 50)
    pygame.draw.rect(screen, (0,255,0),(obstacle_x, obstacle_y),)

    #update the screen
    pygame.display.flip()

    clock.tick(60) #fps

pygame.quit()