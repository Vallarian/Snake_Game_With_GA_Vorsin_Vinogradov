from Run_Game_With_ML import *
from random import choice, randint

# Функция для расчёта приспособленности популяции
def fitness_function(population):
    # fitness — список, в котором будут храниться значения приспособленности для каждой особи популяции
    fitness_population = []
    # Проходим по каждой особи в популяции
    for i in range(population.shape[0]):
        # Запускаем игру с использованием весов из хромосомы текущей особи и получаем значение приспособленности
        fit = game_with_GA(display, clock, population[i])
        # Выводим значение приспособленности для текущей особи
        print('Значение приспособления для текущей особи' + str(i) + ' : ', fit)
        # Добавляем значение приспособленности в список
        fitness_population.append(fit)
    # Возвращаем массив значений приспособленности для всей популяции
    return np.array(fitness_population)


# Функция для выбора родительского пула
def selection_function(population, fitness_population, parents):
    # Массив, в котором будут храниться выбранные родительские особи
    selected_parents = np.empty((parents, population.shape[1]))
    # Проходим по родителям, которых нужно выбрать
    for parent in range(parents):
        # Находим индекс особи с максимальным значением приспособленности
        max_fitness_idx = np.where(fitness_population == np.max(fitness_population))
        max_fitness_idx = max_fitness_idx[0][0]
        # Добавляем выбранную родительскую особь в массив родителей
        selected_parents[parent, :] = population[max_fitness_idx, :]
        # Устанавливаем значение приспособленности выбранной особи на очень маленькое число, чтобы исключить её повторное выбор
        fitness_population[max_fitness_idx] = -99999999
    # Возвращаем массив родительских особей
    return selected_parents

# Функция для выполнения кроссовера (скрещивания) родительских особей и создания потомства
def crossover_function(parents, child_size):
    # массив, в котором будут храниться созданные потомки
    childs = np.empty(child_size)
    # Проходим по количеству потомков, которые нужно создать
    for x in range(child_size[0]):
        # Входим в цикл для выбора двух разных родительских особей
        while True:
            # Выбираем  первую родительскую особь случайным образом
            parent1 = random.randint(0, parents.shape[0] - 1)
            # Выбираем вторую родительскую особь случайным образом
            parent2 = random.randint(0, parents.shape[0] - 1)
            # Если выбранные родительские особи разные, то создаём потомка
            if parent1 != parent2:
                for y in range(child_size[1]):
                    # С вероятностью 50% выбираем ген от первого или второго родителя
                    if random.uniform(0, 1) < 0.5: childs[x, y] = parents[parent1, y]
                    else: childs[x, y] = parents[parent2, y]
                # Выходим из цикла после создания потомка
                break
    # Возвращаем массив потомков
    return childs

# Функция для выполнения мутации потомства, полученного в результате кроссовера
def mutation_function(child_crossover):
    # Проходим по каждому потомку в массиве потомства
    for child in range(child_crossover.shape[0]):
        # Выполняем мутацию 25 раз для каждого потомка
        for _ in range(25):
            # Выбираем случайный индекс гена для мутации
            i = randint(0, child_crossover.shape[1] - 1)
        # Генерируем случайное значение для мутации в диапазоне от -1 до 1 с шагом 0.001
        random_value = np.random.choice(np.arange(-1, 1, step=0.001), size=(1), replace=False)
        # Применяем мутацию к выбранному гену
        child_crossover[child, i] = child_crossover[child, i] + random_value
    # Возвращаем массив потомства с мутациями
    return child_crossover