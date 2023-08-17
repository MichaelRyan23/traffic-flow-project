import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ROAD = (169, 169, 169)
BUTTON_COLOR = (100, 100, 100)

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Simulation")

CLOCK = pygame.time.Clock()

CAR_SIZE = 100

class Car:
    def __init__(self, position, direction):
        self.x = position[0]
        self.y = position[1]
        # self.index = index
        self.direction = direction
        self.color = random.choice([RED, GREEN, BLUE])
        self.moving = False

    def move(self):
        # if self.moving and self.index > 0:
        #     self.index -= 1
        if self.direction == "DOWN":
            self.y += 1
        elif self.direction == "UP":
            self.y -= 1
        elif self.direction == "RIGHT":
            self.x += 1
        elif self.direction == "LEFT":
            self.x -= 1
        else:
            print (' not moving')

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, CAR_SIZE, CAR_SIZE))
        #pygame.draw.rect(screen, (0, 255, 0), (10, 10, 50, 75))

def draw_road():
    pygame.draw.rect(screen, ROAD, (WIDTH/3, 0, WIDTH/3, HEIGHT))
    pygame.draw.rect(screen, ROAD, (0, HEIGHT/3, WIDTH, HEIGHT/3))

def draw_play_button():
    pygame.draw.rect(screen, BUTTON_COLOR, (10, 10, 60, 30))
    font = pygame.font.Font(None, 24)
    text = font.render('Play', True, WHITE)
    screen.blit(text, (20, 15))

def traffic_logic(cars):
    # Here, you can implement the traffic logic
    pass

def main():
    cars = []
    game_state = "STOPPED"
    
    running = True

    while running:

        screen.fill(WHITE)

        draw_road()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if game_state == "STOPPED" and 10 < x < 70 and 10 < y < 40:  # Check if play button was pressed
                    game_state = "RUNNING"
                    for car in cars:
                        car.moving = True
                else:
                    # Logic to add cars when user clicks on the road
                    if WIDTH/3 < x < 2*WIDTH/3 and y < HEIGHT/3:
                        cars.append(Car((x, y), "DOWN"))
                    elif WIDTH/3 < x < 2*WIDTH/3 and y > 2*HEIGHT/3:
                        cars.append(Car((x, y), "UP"))
                    elif x < WIDTH/3 and HEIGHT/3 < y < 2*HEIGHT/3:
                        cars.append(Car((x, y), "RIGHT"))
                    elif x > 2*WIDTH/3 and HEIGHT/3 < y < 2*HEIGHT/3:
                        cars.append(Car((x, y), "LEFT"))

        if game_state == "RUNNING":
            traffic_logic(cars)

        for car in cars:
            car.move()
            car.draw()
        
        if game_state == "STOPPED":
            draw_play_button()

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()