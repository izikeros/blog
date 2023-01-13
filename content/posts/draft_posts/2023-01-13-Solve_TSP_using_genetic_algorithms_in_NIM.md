---
Title: Solve TSP problem using genetic algorithms in NIM
Slug: solve-tsp-problem-using-genetic-algorithms-in-nim
Date: 2023-01-13
modified: 2023-01-13
Start: 2023-01-13
Tags: nim, programming, tsp, genetic-algorithms 
Category: Howto
Image: /images/zsh/inside-work-tree.jpg
Summary: 
Status: draft
prompt1:Can you give me implementation of solution to TSP problem using genetic algorithm using NIM programming language?
---

Let's start with the outline of a solution for the Traveling Salesman Problem (TSP) using a genetic algorithm in the NIM programming language. Here is an example:

1.  Define a representation for TSP tours (i.e. a list of cities in order) as a sequence of integers, where each integer represents a city.
    
2.  Create an initial population of TSP tours using a random number generator.
    
3.  Use a fitness function to evaluate the quality of each tour in the population. The fitness function should take into account the total distance traveled by the tour.
    
4.  Use genetic operators such as selection, crossover, and mutation to create a new population of tours.
    
5.  Repeat steps 3 and 4 for a certain number of generations or until a satisfactory solution is found.
    
6.  Return the best tour found as the solution to the TSP.
    

Here is a basic example of how this could be implemented in NIM:

```nim
import random

type
  Tour = seq[int]

var
  population: seq[Tour]

proc createInitialPopulation(n: int, numCities: int):
  population = newSeq(n)
  for i in 0..<n:
    population[i] = randomPermutation(numCities)

proc evaluateFitness(tour: Tour): float =
  # calculate total distance traveled by tour
  # return as a float
  return distance

proc select(population: seq[Tour]): Tour =
  # implement selection operator (e.g. roulette wheel selection)

proc crossover(a: Tour, b: Tour): Tour =
  # implement crossover operator (e.g. two-point crossover)

proc mutate(tour: Tour):
  # implement mutation operator (e.g. swap mutation)

proc solveTSP(numCities: int, populationSize: int, numGenerations: int):
  createInitialPopulation(populationSize, numCities)
  for i in 0..<numGenerations:
    for tour in population:
      evaluateFitness(tour)
    # sort population by fitness
    for j in 0..<populationSize/2:
      a = select(population)
      b = select(population)
      c = crossover(a, b)
      mutate(c)
      population[j] = c
  # return the best tour in the final population

```


Here is an example implementation of the `select` procedure using roulette wheel selection in NIM:
```
proc select(population: seq[Tour]): Tour =
  var
    totalFitness, randNum: float
    runningSum: float
    i: int
  totalFitness = 0.0
  for tour in population:
    totalFitness += evaluateFitness(tour)
  randNum = random() * totalFitness
  runningSum = 0.0
  for i in 0..<len(population):
    runningSum += evaluateFitness(population[i])
    if runningSum >= randNum:
      return population[i]

```

This implementation uses the `random()` function to generate a random number between 0 and 1, and then uses that number to select a tour from the population. The `evaluateFitness(tour: Tour)` function is used to calculate the fitness of each tour, and the roulette wheel selection is implemented by iterating through the population, adding the fitness of each tour to a running sum, and returning the tour when the running sum exceeds the randomly generated number.

Please note that this is just an example, and that there are many different ways to implement roulette wheel selection. Also in this example I am assuming that evaluateFitness(tour: Tour) returns a value between 0 and 1 as fitness of a tour.


Here is an example implementation of the `evaluateFitness` procedure in NIM:
```
import math

proc evaluateFitness(tour: Tour): float =
  var
    distance: float
    i: int
  distance = 0.0
  for i in 0..<len(tour)-1:
    city1 = tour[i]
    city2 = tour[i+1]
    distance += euclideanDistance(city1, city2)
  return distance

proc euclideanDistance(city1: int, city2: int): float =
  var
    xd: float
    yd: float
  xd = x[city1] - x[city2]
  yd = y[city1] - y[city2]
  return math.sqrt(xd * xd + yd * yd)

```

In this example, `euclideanDistance(city1: int, city2: int)` calculates the euclidean distance between two cities using the coordinates of the cities. The `evaluateFitness` procedure iterates through the tour, calculating the total distance traveled by adding up the euclidean distance between each consecutive city in the tour.

Please note that this is just an example, and that there are many different ways to calculate the distance between cities. Also, this example assumes that the x and y coordinates of each city are stored in arrays `x` and `y` respectively and also the tour is a list of integers where each integer represents a city.

```nim
proc crossover(a: Tour, b: Tour): Tour =
  var
    i: int
    r1, r2: int
    offspring: Tour
  r1 = randint(0, len(a)-1)
  r2 = randint(r1, len(a)-1)
  offspring = a[0..r1]
  for i in r1..r2:
    if b[i] notin offspring:
      offspring.add(b[i])
  for i in 0..<len(a):
    if a[i] notin offspring:
      offspring.add(a[i])
  return offspring

proc mutate(tour: Tour):
  var
    i, j: int
    r1, r2: int
  r1 = randint(0, len(tour)-1)
  r2 = randint(0, len(tour)-1)
  tour[r1], tour[r2] = tour[r2], tour[r1]

```

The `crossover` procedure implements a two-point crossover operator. It takes two tours, `a` and `b`, as input and creates an offspring tour by taking the sub-tour from `a` between two randomly selected points and adding any missing cities from `b` to the offspring.

The `mutate` procedure implements a swap mutation operator. It takes a tour as input and randomly selects two positions in the tour and swap the elements at those positions.

Please note that this is just an example, and that there are many different ways to implement crossover and mutation operators. Also, in this example I am using `randint(a:int, b:int)` function which returns random integer between a and b (inclusive)

> How to visualize convergence of the this algorithm in NIM?

There are several ways to visualize the convergence of a genetic algorithm in NIM. Here are a few examples:

1.  Plotting the best fitness of the population over time: This can be done by keeping track of the best fitness value at each generation and plotting that data over time.
    
2.  Plotting the average fitness of the population over time: Similar to the best fitness, but instead of keeping track of the best fitness, we keep track of average fitness of the population at each generation.
    
3.  Plotting the standard deviation of the fitness of the population over time: This can give an idea of how much the fitness values are varying within the population.
    
4.  Plotting the distribution of the fitness of the population over time: This can give a visual representation of how the population's fitness is changing over time.
    
5.  Plotting the best solution found at each generation: This can give a visual representation of how the algorithm is approaching an optimal solution
    

To implement this visualization in NIM, you would need to use a library such as matplotlib, or gnuplot. There are also other libraries which you can use to plot. You would also need to store the best, average, standard deviation and population's fitness values in arrays at each generation and then use the plotting libraries to generate the graph.

Please note that, visualization of convergence is not only important for understanding the behavior of the algorithm but also for debugging and fine-tuning the algorithm.