# https://lethain.com/genetic-algorithms-cool-name-damn-simple/
from random import randint

# Create a member of the population.
def individual(length, min, max):
    return [ randint(min,max) for x in range(length) ]
# only for test
print(individual(5,0,100))

# Create a number of individuals (i.e. a population).
# count: the number of individuals in the population
# length: the number of values per individual
# min: the min possible value in an individual's list of values
# max: the max possible value in an individual's list of values
def population(count, length, min, max):
    return [ individual(length, min, max) for x in range(count) ]
# only for test
#print(population(3,5,0,100))

# Determine the fitness of an individual. Lower is better.
# individual: the individual to evaluate
# target: the sum of numbers that individuals are aiming for
from operator import add
from functools import reduce
def fitness(individual, target):
    sum = reduce(add, individual, 0)
    return abs(target-sum)
# only for test
x = individual(5,0,100)
print(fitness(x, 200))

# Find average fitness for a population.'
def grade(pop, target):
    summed = reduce(add, (fitness(x, target) for x in pop), 0)
    return summed / (len(pop) * 1.0)
# only for test
x = population(3,5,0,100)
target = 200
print(grade(x, target))

# Create a child (example)
father = individual(6,0,100)
mother = individual(6,0,100)
child = father[:3] + mother[3:]
print(father)
print(mother)
print(child)

# Mutate
from random import random, randint
#chance_to_mutate = 0.01
#for i in population:
#    if chance_to_mutate > random():
#        place_to_modify = randint(0,len(i))
#        i[place_to_modify] = randint(min(i), max(i))

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [ (fitness(x, target), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]

    # randomly add other individuals to promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)
            
    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))
    
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = int(len(male) / 2)

            child = male[:half] + female[half:]
            children.append(child)

    parents.extend(children)
    return parents


# test code
# i_length must be even
target = 371
p_count = 100
i_length = 6
i_min = 0
i_max = 100
p = population(p_count, i_length, i_min, i_max)
fitness_history = [grade(p, target),]
for i in range(100):
    p = evolve(p, target)
    fitness_history.append(grade(p, target))

for datum in fitness_history:
   print(datum)