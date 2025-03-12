from Snake import *

def random_direction(snake_head, angle_to_apple):
    # Определяем направление движения в зависимости от угла до яблока
    movement_direction = 0
    if angle_to_apple > 0: movement_direction = 1  # Если угол положительный, двигаемся вправо
    elif angle_to_apple < 0: movement_direction = -1  # Если угол отрицательный, двигаемся влево
    else: movement_direction = 0  # Если угол равен нулю, остаёмся на месте

    # Возвращаем вектор направления с учётом текущего положения змеи, угла до яблока и выбранного направления
    return direction_vector(snake_head, angle_to_apple, movement_direction)

def blocked_directions(snake_head):
    # Вычисляем вектор текущего направления движения змеи
    vector_snake_move = np.array(snake_head[0]) - np.array(snake_head[1])
    # Проверяем, заблокировано ли движение вправо
    move_in_right_blocked = move_is_blocked(snake_head, np.array([-vector_snake_move [1], vector_snake_move [0]]))
    # Проверяем, заблокировано ли движение влево
    move_in_left_blocked = move_is_blocked(snake_head,  np.array([vector_snake_move[1], -vector_snake_move[0]]))
    # Проверяем, заблокировано ли движение вверх
    move_in_front_blocked = move_is_blocked(snake_head,  vector_snake_move)
    return  vector_snake_move, move_in_front_blocked, move_in_left_blocked, move_in_right_blocked


def direction_vector(snake_head, angle_to_apple, direction):
    # Вычисляем вектор текущего направления движения змеи
    vector_snake_move = np.array(snake_head[0]) - np.array(snake_head[1])
    # Инициализируем новый вектор направления текущим направлением
    new_direction = vector_snake_move 
    # Если направление равно 1, то меняем направление на правое
    if direction == 1:
        new_direction = np.array([-vector_snake_move [1], vector_snake_move [0]])
    # Если направление равно -1, то меняем направление на левое
    if direction == -1:
        new_direction = np.array([vector_snake_move [1], -vector_snake_move [0]])
    # Генерируем направление на основе нового вектора направления
    new_generate_direction = 0
    # Если новый вектор направления равен [0, 10], то новое сгенерированное направление вниз
    if new_direction.tolist() == [0, 10]:
        new_generate_direction = 2
    # Если новый вектор направления равен [10, 0],то новое сгенерированное направление вправо
    if new_direction.tolist() == [10, 0]:
        new_generate_direction = 1
    # Если новый вектор направления равен [-10, 0], то новое сгенерированное направление влево
    elif new_direction.tolist() == [-10, 0]:
        new_generate_direction = 0
    # В противном случае, новое сгенерированное направление вверх
    else:
        new_generate_direction = 3
    return direction, new_generate_direction
def generate_button_direction(new_direction):
    # Инициализируем направление кнопки как 0
    button_direction = 0

    # Если новый вектор направления равен [10, 0], то направление кнопки - 1 (вправо)
    if new_direction.tolist() == [10, 0]:
        button_direction = 1
    # Если новый вектор направления равен [-10, 0], то направление кнопки - 0 (влево)
    elif new_direction.tolist() == [-10, 0]:
        button_direction = 0
    # Если новый вектор направления равен [0, 10], то направление кнопки - 2 (вниз)
    elif new_direction.tolist() == [0, 10]:
        button_direction = 2
    # В противном случае, направление кнопки - 3 (вверх)
    else:
        button_direction = 3
    return button_direction

# Вычисляет угол между направлением змеи и направлением на яблоко
def angle_to_apple(snake_head, apple_position):
    #Вычисляются длины векторов направления к яблоку и к голове змеи
    lenght_vector_to_apple = np.linalg.norm(np.array(apple_position) - np.array(snake_head[0]))
    lenght_vector_to_snake = np.linalg.norm(np.array(snake_head[0]) - np.array(snake_head[1]))
    #Если норма вектора равна нулю (что может произойти, если змея и яблоко находятся в одной точке или если змея стоит на месте), 
    #то норма устанавливается равной 10. Это делается для избежания деления на ноль при нормализации векторов.
    if lenght_vector_to_apple == 0: lenght_vector_to_apple = 10
    if lenght_vector_to_snake == 0: lenght_vector_to_snake = 10
    # Векторы направления к яблоку и направления движения змеи нормализуются, то есть их длины приводятся к единице. 
    # Это необходимо для корректного вычисления угла между векторами.
    normalized_apple_vector = (np.array(apple_position) - np.array(snake_head[0])) / lenght_vector_to_apple
    normalized_snake_vector = (np.array(snake_head[0]) - np.array(snake_head[1])) / lenght_vector_to_snake
    # Вычисляется угол между двумя векторами с помощью функции atan2, которая возвращает угол в радианах. 
    # Формула использует координаты нормализованных векторов для вычисления синуса и косинуса угла. Результат делится на math.pi, чтобы привести угол к диапазону от -1 до 1.
    angle_between_vectors = math.atan2(
        normalized_apple_vector[1] * normalized_snake_vector[0] - normalized_apple_vector[0] * normalized_snake_vector[1],
        normalized_apple_vector[1] * normalized_snake_vector[1] + normalized_apple_vector[0] * normalized_snake_vector[0]) / math.pi
    return angle_between_vectors, normalized_apple_vector, normalized_snake_vector
