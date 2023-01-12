import pygame
import random

pygame.init()
def game():
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0,255,0)
    global dis
    dis = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snake Game by Makhovskyi')

    process(dis, black, white, green)


    pygame.quit()
    quit()
display_style = pygame.font.SysFont("arial", 30, "bold")
score_font = pygame.font.SysFont("arial", 45, "bold")
def final_score(score):
    value = score_font.render("The score is: " + str(score), True, (0,255,0))
    dis.blit(value, [0,0])

def process(dis, black, white, green):
    a = 10 # стартовий розмір змії
    b = 10
    game_over = False
    x1 = 300 # стартові координати
    y1 = 300

    x1_change = 0
    y1_change = 0
    fb = False # прапорці для того шоб не можна було змінювати напрямок руху на протилежний
    lr = False
    prev = None
    clock = pygame.time.Clock()
    x_food = random.randint(10, 790)  # генерує межі в яких може з'явитись їжа
    y_food = random.randint(10, 590)
    length_snake = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if x1 >= 800 or y1 >= 600 or x1<=0 or y1<=0:
                game_over = True


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and prev!= pygame.K_RIGHT:
                    x1_change = -10
                    y1_change = 0
                    prev = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and prev!= pygame.K_LEFT:
                    x1_change = 10
                    y1_change = 0
                    prev = pygame.K_RIGHT
                elif event.key == pygame.K_UP and prev!= pygame.K_DOWN:
                    y1_change = -10
                    x1_change = 0
                    prev = pygame.K_UP
                elif event.key == pygame.K_DOWN and prev!= pygame.K_UP:
                    y1_change = 10
                    x1_change = 0
                    prev = pygame.K_DOWN


        x1 += x1_change #можна збільшити швидкість змії збільшивши х1 або у1
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, a, b])
        food = pygame.draw.rect(dis, green, [x_food, y_food, 10, 10])

        # Умова коли співпадають координати голови змії з координатами їжі
        if abs(x1-x_food) <= 10 and abs(y1-y_food) <= 10:
            x_food = random.randint(10, 790)
            y_food = random.randint(10, 590)
            food = pygame.draw.rect(dis, white, [x_food, y_food,0, 0])
            length_snake += 1
        final_score(length_snake)
        pygame.display.update()

        clock.tick(20)

game()