# M17 Lesson 5 - Activity 4: Rain Expectation (Poisson)
import scipy.stats as stats

prob1 = stats.poisson.pmf(6, 10)
print("probability of raining for exactly 6 days :", prob1)

prob2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10)
print("probability of raining for 12-14 days :", prob2)
