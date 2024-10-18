import random

target = [1, 1, 1]
generation_size = 2
chromo_length = 3


def fitness(num):
    return sum([1 if num[i] == target[i] else 0 for i in range(chromo_length)])

def generate_solutions():
    solutions = []
    for i in range(generation_size):
        chromo = [random.randint(0, 1),random.randint(0, 1),random.randint(0, 1)]
        solutions.append(chromo)
    return solutions

def select_parents(solutions):
    fitness_score = [fitness(chromo) for chromo in solutions]
    parents = random.choices(solutions, weights=fitness_score, k=2)
    return parents

def crossover(parent1, parent2):
    crossover_point = random.randint(1, chromo_length-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromo):
    for i in range(chromo_length):
        if random.random() < .1:
            chromo[i] = 1 - chromo[i]
    return chromo


def genetic_algo():
    population = generate_solutions()

    for i in range(20):
        new_solution = []
        while len(new_solution) < generation_size:
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_solution.extend([child1, child2])

        population = new_solution[:generation_size]

        best_chromo = max(population, key=fitness)
        print(f"gen {i+1}: peak fitness = {fitness(best_chromo)}, Chromosome = {best_chromo}")

        if fitness(best_chromo) == chromo_length:
            print("solution found")
            break

genetic_algo()
