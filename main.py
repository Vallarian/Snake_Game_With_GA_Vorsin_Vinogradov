from GA import *
from Snake import *

# Определяем количество нейронов в каждом слое нейронной сети
n_x = 7  # количество нейронов во входном слое
n_h = 9  # количество нейронов в первом скрытом слое
n_h2 = 15  # количество нейронов во втором скрытом слое
n_y = 3  # количество нейронов в выходном слое
# Определяем количество хромосом в популяции и общее количество генов в каждой хромосоме
chromosomes_in_population = 50  # количество хромосом в популяции
number_genes = n_x * n_h + n_h * n_h2 + n_h2 * n_y  # общее количество генов в каждой хромосоме
# Определяем размер популяции
population_size = (chromosomes_in_population, number_genes)
# Создаём начальную популяцию, выбирая случайные значения для генов в диапазоне от -1 до 1 с шагом 0.01
population = np.random.choice(np.arange(-1, 1, step=0.01), size=population_size, replace=True)
# Определяем количество поколений для эволюции
number_generation = 100
# Определяем количество родителей, которые будут выбраны для скрещивания
number_parents = 12

# Проходим по каждому поколению
for generation in range(number_generation):
    print(' Генерация №' + str(generation))
    # Измеряем приспособленность каждой хромосомы в популяции
    fitness = fitness_function(population)
    # Выводим значение приспособленности самой приспособленной хромосомы в текущем поколении
    print('Самая приспособленная хромосома' + str(generation) + ' в текущем поколение имет значение приспособления =:  ', np.max(fitness))
    # Выбираем лучших родителей в популяции для скрещивания
    selection_parents = selection_function(population, fitness, number_parents)
    # Генерация следующего поколения с использованием crossover.
    crossover_childs = crossover_function(selection_parents , child_size=(population_size[0] - selection_parents.shape[0], number_genes))
    # Добавление некоторых вариаций к потомству с помощью мутации.
    mutation_childs = mutation_function(crossover_childs)
    # Создание новой популяции на основе родителей и потомства.
    population[0:selection_parents.shape[0], :] = selection_parents
    population[selection_parents.shape[0]:, :] = mutation_childs
