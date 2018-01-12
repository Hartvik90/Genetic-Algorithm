#!/usr/bin/env python
'''
    File name: GenAlg.py
    Author: Hartvik Line
    Date created: 12/1/2018
    Date last modified: 12/1/2018
    Python Version: 3.6
'''

import string
import random
import math
import numpy

## ----- Tuning parameters -----
# The soluton to guess (Only large characters, no space)
Solution = 'IAMSMARTERTHANYOU'
Size_Population = 50
MutationRate = 0.03  # 0 to 1

## ----- Initalize parameters -----
SolList = list(Solution)
Population = ['A' for x in range(Size_Population)]
RunCounter = 0
# Initial random population
for i in range(0, Size_Population):
    for j in range(0, len(Solution)):
        if j == 0:
            Population[i] = random.choice(string.ascii_uppercase)
        else:
            Population[i] += random.choice(string.ascii_uppercase)

## ----- Genetic algorithm loop -----
exit = False
while exit == False:

    Performance = [0 for x in range(Size_Population)]
    # Measure success rate:
    for i in range(0, Size_Population):
        for j in range(0, len(Solution)):
            if (Population[i].__getitem__(j) == Solution.__getitem__(j)):
                Performance[i] += 1

    # Sort list by performance
    SortedPop = [x for _, x in sorted(zip(Performance, Population))]

    # Add only the "best" 50 % in the mating pool
    matingPool = SortedPop[math.floor(len(SortedPop) / 2):len(SortedPop)]

    # Crossover
    for i in range(0, Size_Population):
        # Pick random from mating pool
        Father = random.choice(matingPool)
        Mother = random.choice(matingPool)
        Son = ['I' for x in range(len(Solution))]
        for j in range(0, len(Solution)):
            if random.choice([1, 2]) == 1:
                Son[j] = Mother[j]
            else:
                Son[j] = Father[j]

            # Mutation
            if random.choice(list(range(1, math.floor((1 / MutationRate))))) == 1:
                Son[j] = random.choice(string.ascii_uppercase)
        print(Son)

        Population[i] = ''.join(Son)
        RunCounter += 1

    print(['Average sucsessrate:',(numpy.mean(Performance)/len(Solution))*100,'%'])
    print(['Best sucsessrate:',(numpy.max(Performance)/len(Solution))*100,'%'])
    input("Press Enter to continue...")

    # Exit if one of the population have guessed the correct word
    if (numpy.max(Performance) / len(Solution)) * 100 == 100:
        exit = True

## ----- Plot final data -----
GenAlg_Variation = len(string.ascii_uppercase)
BruteForceTries = math.pow(len(string.ascii_uppercase), len(Solution))
print('Nr of evaluations if brute force method: Up to ' + str(BruteForceTries))
print('Number of evaluations with Gen.Alg.: ' + str(RunCounter))
print('Method efficiency: Gen. Alg. up to ' + str(
    math.floor(BruteForceTries / RunCounter)) + ' times better than brute force search')
