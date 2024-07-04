import pygame
import sys
from button import ImageButton
import random
import time

# Инициализация pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 700, 600
MAX_FPS = 60
start_time = pygame.time.get_ticks()
elapsed_time = 0
game_over = False
x = 0
y = 500
backet_bought = 0
bg = pygame.image.load('assets/bg.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey friuts")
clock = pygame.time.Clock()



def main_menu():
    # Создание кнопок
    start_button = ImageButton(WIDTH/2-(252/2), 150, 252, 74, "Новая игра", "assets\green_button2.jpg",
                               "assets\green_button2_hover.jpg")
    shop_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "Магазин", "assets\green_button2.jpg",
                              "assets\green_button2_hover.jpg")
    exit_button = ImageButton(WIDTH/2-(252/2), 350, 252, 74, "Выйти", "assets\green_button2.jpg",
                              "assets\green_button2_hover.jpg")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg,  (0,  0))
        font = pygame.font.Font(None, 72)
        text_surface = font.render("Меллстрой фрутс", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                print("Кнопка 'Старт' была нажата!")
                fade()
                levels()

            if event.type == pygame.USEREVENT and event.button == shop_button:
                fade()
                shop()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, shop_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, shop_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)


        pygame.display.flip()

def levels():
    back_menu_button = ImageButton(20, 20, 74, 74, "<--", "assets\green_button2.jpg",
                                   "assets\green_button2_hover.jpg")
    lvl1_button = ImageButton(WIDTH/2-(452/2), 200,  174,  74,  "1",  "assets\green_button2.jpg",
                              "assets\green_button2_hover.jpg")
    lvl2_button = ImageButton(WIDTH / 2 - (452 / 2), 280, 174, 74, "2", "assets\green_button2.jpg",
                              "assets\green_button2_hover.jpg")
    lvl3_button = ImageButton(WIDTH / 2 - (452 / 2), 360, 174, 74, "3", "assets\green_button2.jpg",
                              "assets\green_button2_hover.jpg")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        font = pygame.font.Font(None, 72)
        text_surface = font.render("Выберете уровень", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT and event.button == lvl1_button:
                print("Кнопка 'Старт1' была нажата!")
                fade()
                lvl1()
            if event.type == pygame.USEREVENT and event.button == lvl2_button:
                print("Кнопка 'Старт2' была нажата!")
                fade()
                lvl2()
            if event.type == pygame.USEREVENT and event.button == lvl3_button:
                print("Кнопка 'Старт3' была нажата!")
                fade()
                lvl3()
            if event.type == pygame.USEREVENT and event.button == back_menu_button:
                running = False
                main_menu()
            for btn in [lvl1_button, lvl2_button, lvl3_button, back_menu_button]:
                btn.handle_event(event)
        for btn in [lvl1_button, lvl2_button, lvl3_button, back_menu_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        pygame.display.flip()

def shop():
    global backet_bought
    back_menu_button = ImageButton(20, 20, 74, 74, "<--", "assets\green_button2.jpg",
                                   "assets\green_button2_hover.jpg")
    buy_button = ImageButton(320, 450, 200, 100, "купить", "assets\green_button2.jpg",
                             "assets\green_button2_hover.jpg")
    running = True
    backet = pygame.image.load('assets/backet.png')
    backet = pygame.transform.scale(backet,  (200,  200))
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        screen.blit(backet, (300, 200))
        font = pygame.font.Font(None, 72)
        font1 = pygame.font.Font(None, 36)
        text1 = font.render("Магазин", True, (255, 255, 255))
        text2 = font1.render("Лукошко", True, (255, 255, 255))
        screen.blit(text1, (300,  100))
        screen.blit(text2, (320, 400))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()

            if i.type == pygame.USEREVENT and i.button == back_menu_button:
                running = False
                main_menu()

            if i.type == pygame.USEREVENT and i.button == buy_button:
                backet_bought = 1
                print("test button")

            for btn in [back_menu_button, buy_button]:
                btn.handle_event(i)

        for btn in [back_menu_button, buy_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        pygame.display.flip()

def lvl1():
    fruits = 0
    x_plum = random.randint(60, WIDTH - 100)
    y_plum = 50
    x_banana = random.randint(40, WIDTH - 100)
    y_banana = 0
    x_grape = random.randint(10, WIDTH - 100)
    y_grape = 30
    x_apple = random.randint(20, WIDTH - 100)
    y_apple = 60
    x = 0
    y = 500
    monkey = pygame.image.load('assets\monkey.jpg')
    monkey = pygame.transform.scale(monkey, (100, 100))
    plum = pygame.image.load('assets\plum.jpg')
    plum = pygame.transform.scale(plum, (100, 100))
    banana = pygame.image.load('assets/banana.jpg')
    banana = pygame.transform.scale(banana, (100, 100))
    grape = pygame.image.load('assets\grape.jpg')
    grape = pygame.transform.scale(grape, (100, 100))
    apple = pygame.image.load('assets/apple.jpg')
    apple = pygame.transform.scale(apple, (100, 100))
    start_time = time.time()
    global backet_bought  # Ensure this variable is accessible and properly managed in your code
    running = True
    square_pos = (100, 100)  # Initial position for the first square
    square_size = (50, 50)  # Size of the square
    square_color = (255, 0, 0)  # Color of the square (Red)
    follow_square = False
    square_pos = [WIDTH // 2, HEIGHT // 2]
    square_size = [50, 50]
    plum_hitbox = pygame.Rect(x_plum, y_plum, 100, 100)
    banana_hitbox = pygame.Rect(x_banana, y_banana, 100, 100)
    grape_hitbox = pygame.Rect(x_grape, y_grape, 100, 100)
    apple_hitbox = pygame.Rect(x_apple, y_apple, 100, 100)
    square_rect = pygame.Rect(square_pos[0], square_pos[1], square_size[0], square_size[1])
    dragging = False
    running = True
    while running:
        current_time = time.time()
        if current_time - start_time >= 30:
            font1 = pygame.font.Font(None, 36)
            final_text = font1.render(f"Игра окончена! Фруктов собрано: {fruits}", True, (0, 0, 0))
            screen.blit(final_text, (150, 250))
            pygame.display.flip()
            pygame.time.wait(4000)
            running = False
            main_menu()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if square_rect.collidepoint(event.pos):
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = square_rect.x - mouse_x
                    offset_y = square_rect.y - mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    square_rect.x = mouse_x + offset_x
                    square_rect.y = mouse_y + offset_y
        screen.fill((255, 255, 255))
        if backet_bought == 1:
            pygame.draw.rect(screen, square_color, square_rect)
        if backet_bought == 1:
            if square_rect.colliderect(plum_hitbox):
                x_plum = random.randint(0, WIDTH - 100)
                y_plum = 0
                fruits += 1
            if square_rect.colliderect(banana_hitbox):
                x_banana = random.randint(0, WIDTH - 100)
                y_banana = 0
                fruits += 1
            if square_rect.colliderect(apple_hitbox):
                x_apple = random.randint(0, WIDTH - 100)
                y_apple = 0
                fruits += 1
            if square_rect.colliderect(grape_hitbox):
                x_grape = random.randint(0, WIDTH - 100)
                y_grape = 0
                fruits += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x -= 1
        if keys[pygame.K_d]:
            x += 1
        screen.blit(monkey, (x, y))
        screen.blit(plum, (x_plum, y_plum))
        y_plum += 0.8
        screen.blit(banana, (x_banana, y_banana))
        y_banana += 0.8
        screen.blit(grape, (x_grape, y_grape))
        y_grape += 0.8
        screen.blit(apple, (x_apple, y_apple))
        y_apple += 0.8
        plum_hitbox = pygame.Rect(x_plum, y_plum, 100, 100)
        banana_hitbox = pygame.Rect(x_banana, y_banana, 100, 100)
        grape_hitbox = pygame.Rect(x_grape, y_grape, 100, 100)
        apple_hitbox = pygame.Rect(x_apple, y_apple, 100, 100)
        if y_plum > HEIGHT:
            y_plum = 0
            x_plum = random.randint(0, WIDTH - 100)
        if y_banana > HEIGHT:
            y_banana = 0
            x_banana = random.randint(0, WIDTH - 100)
        if y_grape > HEIGHT:
            y_grape = 0
            x_grape = random.randint(0, WIDTH - 100)
        if y_apple > HEIGHT:
            y_apple = 0
            x_apple = random.randint(0, WIDTH - 100)
        if x < 0:
            x = 0
        if x > WIDTH - 100:
            x = WIDTH - 100
        if x < x_grape + 100 and x + 100 > x_grape and y < y_grape + 100 and y + 100 > y_grape:
            y_grape = 0
            x_grape = random.randint(0, WIDTH - 100)
            fruits += 1

        if x < x_plum + 100 and x + 100 > x_plum and y < y_plum + 100 and y + 100 > y_plum:
            y_plum = 0
            x_plum = random.randint(0, WIDTH - 100)
            fruits += 1

        if x < x_banana + 100 and x + 100 > x_banana and y < y_banana + 100 and y + 100 > y_banana:
            y_banana = 0
            x_banana = random.randint(0, WIDTH - 100)
            fruits += 1
        if x < x_apple + 100 and x + 100 > x_apple and y < y_apple + 100 and y + 100 > y_apple:
            y_apple = 0
            x_apple = random.randint(0, WIDTH - 100)
            fruits += 1
        font = pygame.font.Font(None, 36)
        text = font.render("Фруктов собрано: " + str(fruits), True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()

def lvl2():
    fruits = 0
    x_plum = random.randint(60, WIDTH - 100)
    y_plum = 50
    x_banana = random.randint(40, WIDTH - 100)
    y_banana = 0
    x_grape = random.randint(10, WIDTH - 100)
    y_grape = 30
    x_apple = random.randint(20, WIDTH - 100)
    y_apple = 60
    x = 0
    y = 500
    monkey = pygame.image.load('assets\monkey.jpg')
    monkey = pygame.transform.scale(monkey, (100, 100))
    plum = pygame.image.load('assets\plum.jpg')
    plum = pygame.transform.scale(plum, (100, 100))
    banana = pygame.image.load('assets/banana.jpg')
    banana = pygame.transform.scale(banana, (100, 100))
    grape = pygame.image.load('assets\grape.jpg')
    grape = pygame.transform.scale(grape, (100, 100))
    apple = pygame.image.load('assets/apple.jpg')
    apple = pygame.transform.scale(apple, (100, 100))
    start_time = time.time()
    global backet_bought  # Ensure this variable is accessible and properly managed in your code
    running = True
    square_pos = (100, 100)  # Initial position for the first square
    square_size = (50, 50)  # Size of the square
    square_color = (255, 0, 0)  # Color of the square (Red)
    follow_square = False
    square_pos = [WIDTH // 2, HEIGHT // 2]
    square_size = [50, 50]
    plum_hitbox = pygame.Rect(x_plum, y_plum, 100, 100)
    banana_hitbox = pygame.Rect(x_banana, y_banana, 100, 100)
    grape_hitbox = pygame.Rect(x_grape, y_grape, 100, 100)
    apple_hitbox = pygame.Rect(x_apple, y_apple, 100, 100)
    square_rect = pygame.Rect(square_pos[0], square_pos[1], square_size[0], square_size[1])
    dragging = False
    running = True
    while running:
        current_time = time.time()
        if current_time - start_time >= 30:
            font1 = pygame.font.Font(None, 36)
            final_text = font1.render(f"Игра окончена! Фруктов собрано: {fruits}", True, (0, 0, 0))
            screen.blit(final_text, (150, 250))
            pygame.display.flip()
            pygame.time.wait(4000)
            running = False
            main_menu()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if square_rect.collidepoint(event.pos):
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = square_rect.x - mouse_x
                    offset_y = square_rect.y - mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    square_rect.x = mouse_x + offset_x
                    square_rect.y = mouse_y + offset_y
        screen.fill((255, 255, 255))
        if backet_bought == 1:
            pygame.draw.rect(screen, square_color, square_rect)
        if backet_bought == 1:
            if square_rect.colliderect(plum_hitbox):
                x_plum = random.randint(0, WIDTH - 100)
                y_plum = 0
                fruits += 1
            if square_rect.colliderect(banana_hitbox):
                x_banana = random.randint(0, WIDTH - 100)
                y_banana = 0
                fruits += 1
            if square_rect.colliderect(apple_hitbox):
                x_apple = random.randint(0, WIDTH - 100)
                y_apple = 0
                fruits += 1
            if square_rect.colliderect(grape_hitbox):
                x_grape = random.randint(0, WIDTH - 100)
                y_grape = 0
                fruits += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x -= 1
        if keys[pygame.K_d]:
            x += 1
        screen.blit(monkey, (x, y))
        screen.blit(plum, (x_plum, y_plum))
        y_plum += 1
        screen.blit(banana, (x_banana, y_banana))
        y_banana += 1
        screen.blit(grape, (x_grape, y_grape))
        y_grape += 1
        screen.blit(apple, (x_apple, y_apple))
        y_apple += 1
        plum_hitbox = pygame.Rect(x_plum, y_plum, 100, 100)
        banana_hitbox = pygame.Rect(x_banana, y_banana, 100, 100)
        grape_hitbox = pygame.Rect(x_grape, y_grape, 100, 100)
        apple_hitbox = pygame.Rect(x_apple, y_apple, 100, 100)
        if y_plum > HEIGHT:
            y_plum = 0
            x_plum = random.randint(0, WIDTH - 100)
        if y_banana > HEIGHT:
            y_banana = 0
            x_banana = random.randint(0, WIDTH - 100)
        if y_grape > HEIGHT:
            y_grape = 0
            x_grape = random.randint(0, WIDTH - 100)
        if y_apple > HEIGHT:
            y_apple = 0
            x_apple = random.randint(0, WIDTH - 100)
        if x < 0:
            x = 0
        if x > WIDTH - 100:
            x = WIDTH - 100
        if x < x_grape + 100 and x + 100 > x_grape and y < y_grape + 100 and y + 100 > y_grape:
            y_grape = 0
            x_grape = random.randint(0, WIDTH - 100)
            fruits += 1

        if x < x_plum + 100 and x + 100 > x_plum and y < y_plum + 100 and y + 100 > y_plum:
            y_plum = 0
            x_plum = random.randint(0, WIDTH - 100)
            fruits += 1

        if x < x_banana + 100 and x + 100 > x_banana and y < y_banana + 100 and y + 100 > y_banana:
            y_banana = 0
            x_banana = random.randint(0, WIDTH - 100)
            fruits += 1
        if x < x_apple + 100 and x + 100 > x_apple and y < y_apple + 100 and y + 100 > y_apple:
            y_apple = 0
            x_apple = random.randint(0, WIDTH - 100)
            fruits += 1
        font = pygame.font.Font(None, 36)
        text = font.render("Фруктов собрано: " + str(fruits), True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()

def lvl3():
    fruits = 0
    x_plum = random.randint(60, WIDTH - 100)
    y_plum = 50
    x_banana = random.randint(40, WIDTH - 100)
    y_banana = 0
    x_grape = random.randint(10, WIDTH - 100)
    y_grape = 30
    x_apple = random.randint(20, WIDTH - 100)
    y_apple = 60
    x = 0
    y = 500
    monkey = pygame.image.load('assets\monkey.jpg')
    monkey = pygame.transform.scale(monkey, (100, 100))
    plum = pygame.image.load('assets\plum.jpg')
    plum = pygame.transform.scale(plum, (100, 100))
    banana = pygame.image.load('assets/banana.jpg')
    banana = pygame.transform.scale(banana, (100, 100))
    grape = pygame.image.load('assets\grape.jpg')
    grape = pygame.transform.scale(grape, (100, 100))
    apple = pygame.image.load('assets/apple.jpg')
    apple = pygame.transform.scale(apple, (100, 100))
    start_time = time.time()
    global backet_bought  # Ensure this variable is accessible and properly managed in your code
    running = True
    square_pos = (100, 100)  # Initial position for the first square
    square_size = (50, 50)  # Size of the square
    square_color = (255, 0, 0)  # Color of the square (Red)
    follow_square = False
    square_pos = [WIDTH // 2, HEIGHT // 2]
    square_size = [50, 50]
    plum_hitbox = pygame.Rect(x_plum, y_plum, 100, 100)
    banana_hitbox = pygame.Rect(x_banana, y_banana, 100, 100)
    grape_hitbox = pygame.Rect(x_grape, y_grape, 100, 100)
    apple_hitbox = pygame.Rect(x_apple, y_apple, 100, 100)
    square_rect = pygame.Rect(square_pos[0], square_pos[1], square_size[0], square_size[1])
    dragging = False
    running = True
    while running:
        current_time = time.time()
        if current_time - start_time >= 30:
            font1 = pygame.font.Font(None, 36)
            final_text = font1.render(f"Игра окончена! Фруктов собрано: {fruits}", True, (0, 0, 0))
            screen.blit(final_text, (150, 250))
            pygame.display.flip()
            pygame.time.wait(4000)
            running = False
            main_menu()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if square_rect.collidepoint(event.pos):
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = square_rect.x - mouse_x
                    offset_y = square_rect.y - mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = event.pos
                    square_rect.x = mouse_x + offset_x
                    square_rect.y = mouse_y + offset_y
        screen.fill((255, 255, 255))
        if backet_bought == 1:
            pygame.draw.rect(screen, square_color, square_rect)
        if backet_bought == 1:
            if square_rect.colliderect(plum_hitbox):
                x_plum = random.randint(0, WIDTH - 100)
                y_plum = 0
                fruits += 1
            if square_rect.colliderect(banana_hitbox):
                x_banana = random.randint(0, WIDTH - 100)
                y_banana = 0
                fruits += 1
            if square_rect.colliderect(apple_hitbox):
                x_apple = random.randint(0, WIDTH - 100)
                y_apple = 0
                fruits += 1
            if square_rect.colliderect(grape_hitbox):
                x_grape = random.randint(0, WIDTH - 100)
                y_grape = 0
                fruits += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x -= 1
        if keys[pygame.K_d]:
            x += 1
        screen.blit(monkey, (x, y))
        screen.blit(plum, (x_plum, y_plum))
        y_plum += 1.2
        screen.blit(banana, (x_banana, y_banana))
        y_banana += 1.2
        screen.blit(grape, (x_grape, y_grape))
        y_grape += 1.2
        screen.blit(apple, (x_apple, y_apple))
        y_apple += 1.2
        plum_hitbox = pygame.Rect(x_plum, y_plum, 100, 100)
        banana_hitbox = pygame.Rect(x_banana, y_banana, 100, 100)
        grape_hitbox = pygame.Rect(x_grape, y_grape, 100, 100)
        apple_hitbox = pygame.Rect(x_apple, y_apple, 100, 100)
        if y_plum > HEIGHT:
            y_plum = 0
            x_plum = random.randint(0, WIDTH - 100)
        if y_banana > HEIGHT:
            y_banana = 0
            x_banana = random.randint(0, WIDTH - 100)
        if y_grape > HEIGHT:
            y_grape = 0
            x_grape = random.randint(0, WIDTH - 100)
        if y_apple > HEIGHT:
            y_apple = 0
            x_apple = random.randint(0, WIDTH - 100)
        if x < 0:
            x = 0
        if x > WIDTH - 100:
            x = WIDTH - 100
        if x < x_grape + 100 and x + 100 > x_grape and y < y_grape + 100 and y + 100 > y_grape:
            y_grape = 0
            x_grape = random.randint(0, WIDTH - 100)
            fruits += 1

        if x < x_plum + 100 and x + 100 > x_plum and y < y_plum + 100 and y + 100 > y_plum:
            y_plum = 0
            x_plum = random.randint(0, WIDTH - 100)
            fruits += 1

        if x < x_banana + 100 and x + 100 > x_banana and y < y_banana + 100 and y + 100 > y_banana:
            y_banana = 0
            x_banana = random.randint(0, WIDTH - 100)
            fruits += 1
        if x < x_apple + 100 and x + 100 > x_apple and y < y_apple + 100 and y + 100 > y_apple:
            y_apple = 0
            x_apple = random.randint(0, WIDTH - 100)
            fruits += 1
        font = pygame.font.Font(None, 36)
        text = font.render("Фруктов собрано: " + str(fruits), True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()

def fade():
    running = True
    fade_alpha = 0  # Уровень прозрачности для анимации

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Анимация затухания текущего экрана
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        # Увеличение уровня прозрачности
        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)  # Ограничение FPS

if __name__ == "__main__":
    main_menu()