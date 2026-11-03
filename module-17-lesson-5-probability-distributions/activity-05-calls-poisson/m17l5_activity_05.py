# M17 Lesson 5 - Activity 5: Calls Poisson
import scipy.stats as stats

## Checkpoint 1: more than 20 calls
prob1 = 1 - stats.poisson.cdf(20, 15)
print(prob1)

## Checkpoint 2: between 17 and 21 calls
prob2 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)
print(prob2)
