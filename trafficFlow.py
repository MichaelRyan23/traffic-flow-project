import pygame
import random

# Initialize pygame
pygame.init()

# Colors for cars
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

CAR_SIZE = 75

class Car:
    def __init__(self, position, direction):
        self.x = position[0]
        self.y = position[1]
        # self.index = index
        self.direction = direction
        self.color = random.choice([RED, GREEN, BLUE])
        self.moving = False

    def stop_buffer(self):
        buffer_positions = {
            "DOWN": 110,
            "UP": 405,
            "LEFT": 540,
            "RIGHT": 180
        }
        
        buffer_position = buffer_positions.get(self.direction)

        if self.direction in ["UP", "DOWN"] and self.y == buffer_position:
            return True
        elif self.direction in ["LEFT", "RIGHT"] and self.x == buffer_position:
            return True
        return False

    def move(self):
        # if self.moving and self.index > 0:
        #     self.index -= 1
        if not self.stop_buffer():

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

# TEST COMMIT
#
#def draw_play_button():
#    pygame.draw.rect(screen, BUTTON_COLOR, (10, 10, 60, 30))
#    font = pygame.font.Font(None, 24)
#    text = font.render('Play', True, WHITE)
#    screen.blit(text, (20, 15))
#
    
def draw_mouse_position():
    font = pygame.font.Font(None, 24)
    x, y = pygame.mouse.get_pos()
    text = font.render(f'Mouse Position: {x}, {y}', True, ROAD)
    screen.blit(text, (WIDTH - 200, 10))

def traffic_logic(cars):
    # Here, you can implement the traffic logic
    pass

def main():
    cars = []
    
    running = True

    while running:

        screen.fill(WHITE)

        draw_road()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Logic to add cars when user clicks on the road
                if (WIDTH/3 < x < 2*WIDTH/3 and y < HEIGHT/3) & (y < 110):
                    cars.append(Car((x, y), "DOWN"))

                elif (WIDTH/3 < x < 2*WIDTH/3 and y > 2*HEIGHT/3) & (y > 405):
                    cars.append(Car((x, y), "UP"))
                elif (x < WIDTH/3 and HEIGHT/3 < y < 2*HEIGHT/3) & (x < 180):
                    cars.append(Car((x, y), "RIGHT"))
                elif (x > 2*WIDTH/3 and HEIGHT/3 < y < 2*HEIGHT/3) & (x > 540):
                    cars.append(Car((x, y), "LEFT"))

        traffic_logic(cars)

        for car in cars:
            car.move()
            car.draw()

        draw_mouse_position()

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

