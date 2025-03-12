from Neural_Network import *
from Snake import *
from Generation_Move_Snake_From_GA import *

def game_with_GA(display, clock, weights):
    maximum_score = 0  # максимальная оценка, достигнутая в тестовых играх
    test_games = 1  # количество тестовых игр
    # Переменные для отслеживания текущей и предыдущей оценки
    score1 = 0
    score2 = 0
    # Количество шагов в каждой игре
    steps_per_game = 2500

    # Проходим по каждой тестовой игре
    for _ in range(test_games):
    # Запускаем игру и получаем начальные позиции змеи и яблока, а также начальную оценку
        start_snake_head,  start_snake_head_with_body, random_apple_position, score = start()
    # Инициализируем счётчик количества шагов в одном направлении и предыдущее направление движения
        count_step= 0  # счётчик количества шагов в одном направлении
        previous_move = 0  # предыдущее направление движения змеи
    # Проходим по каждому шагу в игре
        for _ in range(steps_per_game):
        # Определяем, заблокированы ли направления движения вперёд, влево и вправо
            vector_snake_move, move_in_front_blocked, move_in_left_blocked, move_in_right_blocked = blocked_directions(start_snake_head_with_body)
        # Вычисляем угол между направлением движения змеи и направлением на яблоко
            angle_between_vectors, normalized_apple_vector, normalized_snake_vector = angle_to_apple(
                start_snake_head_with_body, random_apple_position)
            # Прогнозируем направление движения змеи с помощью нейронной сети
            predicted_move = np.argmax(np.array(forward_propagation(np.array(
                [move_in_left_blocked, move_in_front_blocked, move_in_right_blocked, normalized_apple_vector[0],
                 normalized_snake_vector[0], normalized_apple_vector[1],
                 normalized_snake_vector[1]]).reshape(-1, 7), weights))) - 1
            # Проверяем, совпадает ли прогнозируемое направление с предыдущим ходом змеи
            if predicted_move == previous_move: count_step += 1 # Если совпадает, увеличиваем счётчик шагов в одном направлении
            else:
                # Если не совпадает, сбрасываем счётчик и обновляем предыдущий ход
                count_step = 0
                previous_move = predicted_move
            # Определяем новое направление движения змеи на основе текущей позиции головы змеи и её тела
            new_move = np.array(start_snake_head_with_body[0]) - np.array(start_snake_head_with_body[1])
            # Если прогнозируемое направление влево (-1), поворачиваем текущее направление налево
            if predicted_move == -1:
                new_move = np.array([new_move[1], - new_move[0]])
            # Если прогнозируемое направление вправо (1), поворачиваем текущее направление направо
            if predicted_move == 1:
                new_move = np.array([-new_move[1], new_move[0]])
            # Направление движения змеи на основе нового хода, сгенерированного функцией 
            button_direction = generate_button_direction(new_move)
            # Вычисляется следующая позиция головы змеи путём добавления вектора движения к текущей позиции головы змеи.
            next_step = start_snake_head_with_body[0] + vector_snake_move
            # Проверяется, не вышла ли змея за границы поля или не столкнулась ли со своим телом.
            # Если это произошло, то назначается штраф в размере 150 баллов и происходит выход из цикла с помощью оператора break.
            if with_border(start_snake_head_with_body[0]) == 1 or with_snake_body(next_step.tolist(),
                                                                                        start_snake_head_with_body) == 1:
                score1 += -150
                break
            else: score1 += 0
            # Игра продолжается с обновлёнными параметрами: новой позицией головы змеи, позицией яблока и направлением движения. 
            # Функция play_game возвращает обновлённые значения этих параметров.
            start_snake_head_with_body, random_apple_position, score = play_game(start_snake_head, start_snake_head_with_body, random_apple_position,
                                                              button_direction, score, display, clock)
            # Обновляется максимальный счёт, если текущий счёт больше максимального.
            if score > maximum_score: maximum_score = score
            # Если количество шагов больше 8 и предсказанное движение не равно нулю, то из текущего счёта вычитается 1 балл. 
            # В противном случае к счёту добавляется 2 балла.
            if count_step > 8 and predicted_move != 0: score2 -= 1
            else: score2 += 2
    # Возвращаем значение умноженное на 5000 для поощрения правильных потомков     
    return score1 + score2 + maximum_score * 5000