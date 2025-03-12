from Snake import *
# Столкновение с границей
def with_border(snake_head):
    if snake_head[0] >= 400 or snake_head[0] < 0 or snake_head[1] >= 400 or snake_head[1] < 0: return 1
    else: return 0
# Столкновение с телом змеи
def with_snake_body(snake_head):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]: return 1
    else: return 0
# Столкновение с препятствием при движении(с телом и границей)
def move_is_blocked_no_ml(snake_body):
    snake_head = snake_body[0]
    if with_border(snake_head) == 1 or with_snake_body(snake_body) == 1: return 1
    else: return 0
# Запуск игры
def play_game(snake_head, snake_position, apple_position, button, score):
    # Предыдущие и текущее движение змеи, exit для отслеживания состояние игры и для выхода из нее
    previous_button = 1
    button = 1
    exit = False
    # Цикл игры
    while exit is not True:
        for event in pygame.event.get():
            # Если пользователь закрыл окно, устанавливаем exit в True, чтобы завершить игру.
            if event.type == pygame.QUIT: exit = True
            # Если пользователь нажал клавишу, проверяем, какая клавиша была нажата, и обновляем направление движения змеи.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and previous_button != 0: button = 1
                elif event.key == pygame.K_LEFT and previous_button != 1: button = 0
                elif event.key == pygame.K_UP and previous_button != 2: button = 3
                elif event.key == pygame.K_DOWN and previous_button != 3: button = 2
                else: button = button
        # Заполняем экран цветом окна.
        display.fill(window_color)
        # Рисуем яблоко на экране в позиции apple_position.
        pygame.draw.rect(display, (51, 153, 255), pygame.Rect(apple_position[0], apple_position[1], 10, 10))
        # Рисуем змею на экране, используя список позиций snake_position.
        for position in snake_position:
            pygame.draw.rect(display, red, pygame.Rect(position[0], position[1], 10, 10))

        # Вызываем функцию snake, передавая ей текущие позиции головы змеи, тела змеи, яблока и текущее направление движения.
        # Функция возвращает обновлённые позиции змеи и яблока, а также текущий счёт.
        snake_position, apple_position, score = snake(snake_head, snake_position, apple_position, button, score)
        # Устанавливаем заголовок окна с текущим счётом.
        pygame.display.set_caption("Змейка"+"  "+"Очки: "+ str(score))
        # Обновляем отображение, чтобы отразить изменения на экране.
        pygame.display.update()
        # Сохраняем текущее направление движения в переменную previous_button.
        previous_button  = button
        # Проверяем, не заблокирована ли следующая клетка для движения змеи.
        # Если заблокирована, устанавливаем exit в True, что приведёт к завершению игры.
        if move_is_blocked_no_ml(snake_position) == 1: exit = True
        # Ограничиваем частоту кадров в игре до 10 кадров в секунду влияет на скорость игры
        clock.tick(10)
    #Возвращаем счет
    return score

# Функция final_score отображает финальный счёт на экране.
def final_score(text, final_score):
    # Создаём шрифт для отображения текста.
    font= pygame.font.Font('freesansbold.ttf', 35)
    # Рендерим текст с финальным счётом.
    TextSurf = font.render(text + str(final_score), True, black)
    # Получаем прямоугольник для текста.
    TextRect = TextSurf.get_rect()
    # Центрируем текст на экране.
    TextRect.center = ((display_width / 2), (display_height / 2))
    # Отрисовываем текст на экране.
    display.blit(TextSurf, TextRect)
    # Обновляем отображение, чтобы показать текст.
    pygame.display.update()
    # Ждём 5 секунды перед закрытием игры.
    time.sleep(5)
# Запуск игры без ML    
if __name__ == "__main__":
    display_width = 400
    display_height = 400
    green = (0,0,0)
    red = (0,0,0)
    black = (0,0,0)
    window_color = (255,255,255)
    clock=pygame.time.Clock() 
    
    snake_head, snake_position, apple_position, score = start()
    
    pygame.init()   

    display = pygame.display.set_mode((display_width,display_height))
    display.fill(window_color)
    pygame.display.update()
    
    game = play_game(snake_head, snake_position, apple_position, 1, score)
    display = pygame.display.set_mode((display_width,display_height))
    display.fill(window_color)
    pygame.display.update()

    display_text = 'Результат: ' + str(score)
    final_score(display_text, game)

    pygame.quit()