import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up game variables and constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
OBSTACLE_BLOCK_SIZE = random.randint(BLOCK_SIZE, BLOCK_SIZE * random.randint(2, 9))
SPEED = 10

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize score
score = 0

# Initialize obstacles
obstacles = []

# Set up display and font
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)


for _ in range(10):
    x = random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
    y = random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
    obstacles.append((x, y))

class Snake:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.body = [(self.x, self.y)]
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.x += BLOCK_SIZE
        elif self.direction == "left":
            self.x -= BLOCK_SIZE
        elif self.direction == "up":
            self.y -= BLOCK_SIZE
        elif self.direction == "down":
            self.y += BLOCK_SIZE

        self.body.append((self.x, self.y))
        self.body.pop(0)

    def draw(self):
        for pos in self.body:
            pygame.draw.rect(screen, WHITE, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

class Food:
    def __init__(self):
        self.x = random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
        self.y = random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

def main():
    global score
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction!= "down":
                    snake.direction = "up"
                elif event.key == pygame.K_DOWN and snake.direction!= "up":
                    snake.direction = "down"
                elif event.key == pygame.K_LEFT and snake.direction!= "right":
                    snake.direction = "left"
                elif event.key == pygame.K_RIGHT and snake.direction!= "left":
                    snake.direction = "right"

        snake.move()
        screen.fill(BLACK)
        snake.draw()
        food.draw()
        
        # Draw obstacles
        for obstacle in obstacles:
            pygame.draw.rect(screen, GREEN, (obstacle[0], obstacle[1], OBSTACLE_BLOCK_SIZE, BLOCK_SIZE))
        
        # Check for collision with obstacles
        for obstacle in obstacles:
            if (snake.x, snake.y) == obstacle:
                print("Game Over")
                print("Final Score:", score)
                pygame.quit()
                sys.exit()

        # check for collision with self and boundaries
        if (snake.x < 0 or snake.x >= WIDTH or
            snake.y < 0 or snake.y >= HEIGHT or
            (snake.x, snake.y) in snake.body[:-1]):
            print("game over")
            print("final score:", score)
            pygame.quit()
            sys.exit()

        if snake.x == food.x and snake.y == food.y:
            food = Food()
            snake.body.append((snake.x, snake.y))

            score += 1

        elif (snake.x < 0 or snake.x >= WIDTH or snake.y < 0 or snake.y >= HEIGHT or (snake.x, snake.y) in snake.body[:-1]):
            print("Game Over")
            print("Final Score:", score)
            pygame.quit()
            sys.exit()

        
        # Display score
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(SPEED)

if __name__ == "__main__":
    main()
