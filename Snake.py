import random
import time
import math
from tqdm import tqdm
import numpy as np
import pygame

def snake(snake_head, snake_position, random_apple_position, button, score):
    # Движение змеи
    if button == 0:
        snake_head[0] -= 10
    elif button == 1:
        snake_head[0] += 10
    elif button == 2:
        snake_head[1] += 10
    else:
        snake_head[1] -= 10
    # Проверяем, столкнулся ли змея с яблоком
    if snake_head != random_apple_position:
        # Если столкновения не было, добавляем новую голову змеи в начало списка позиций и удаляем последний элемент (хвост змеи)
        snake_position.insert(0, list(snake_head))
        snake_position.pop()
    else:
        # Если столкновение произошло, обновляем позицию яблока и счет
        random_apple_position = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        score += 1
        # Добавляем новую голову змеи в начало списка позиций змеи
        snake_position.insert(0, list(snake_head))

    return snake_position, random_apple_position, score
# Столкновение с границей
def with_border(snake_head):
    if snake_head[0] >= 400 or snake_head[0] < 0 or snake_head[1] >= 400 or snake_head[1] < 0: return 1
    else: return 0
# Столкновение с телом змеи
def with_snake_body(snake_head, snake_body):
    if snake_head in snake_body[1:]: return 1
    else: return 0
# Столкновение с препятствием при движении(с телом и границей)
def move_is_blocked(snake_body, current_direction_vector):
    next_step = snake_body[0] + current_direction_vector
    snake_head = snake_body[0]
    if with_border(snake_head) == 1 or with_snake_body(next_step.tolist(), snake_body) == 1: return 1
    else: return 0

def start():
    # Начальную позиция головы змеи
    start_snake_head = [100, 100]
    # Создаем список позиций тела змеи, включая голову
    start_snake_head_with_body = [[100, 100], [90, 100], [80, 100]]
    # Случайная позиция яблока на поле
    random_apple_position = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
    # Начальный счет игрока
    score = 0
    return start_snake_head,  start_snake_head_with_body, random_apple_position, score

def play_game(snake_start, snake_position, apple_position, button_direction, score, display, clock):
    exit = False
    while exit is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        display.fill((255, 255, 255))
        pygame.draw.rect(display, (51, 153, 255), pygame.Rect(apple_position[0], apple_position[1], 10, 10))
        for position in snake_position:
            pygame.draw.rect(display, (0, 0, 0), pygame.Rect(position[0], position[1], 10, 10))
        snake_position, apple_position, score = snake(snake_start, snake_position, apple_position,
                                                               button_direction, score)
        pygame.display.set_caption("Змейка"+"  "+" Очки: " + str(score))
        pygame.display.update()
        clock.tick(60000)

        return snake_position, apple_position, score

display_width = 400
display_height = 400
pygame.init()
display=pygame.display.set_mode((display_width,display_height))
clock=pygame.time.Clock()