import sys, pygame
import math

pygame.init()

color_eye   = (255, 255, 255)
color_pupil = (  0,   0, 100)

size = (400, 200)
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("The eyes follow the cursor.")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    
    def draw_eye_and_pupil(eye_x, eye_y):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        distance_x = mouse_x - eye_x
        distance_y = mouse_y - eye_y

        distance = min(math.sqrt(distance_x ** 2 + distance_y ** 2), 30)
        angle = math.atan2(distance_y, distance_x)

        pupil_x = eye_x + (math.cos(angle) * distance)
        pupil_y = eye_y + (math.sin(angle) * distance)

        pygame.draw.circle(screen, color_eye, (eye_x, eye_y), 50)
        pygame.draw.circle(screen, color_pupil, (pupil_x, pupil_y), 15)

    draw_eye_and_pupil(130, 100)
    draw_eye_and_pupil(270, 100)
    
    pygame.display.flip()


