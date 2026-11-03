# M17 Lesson 5 - Activity 2: Coin PMF
import scipy.stats as stats

x = 3    # number of heads of interest
n = 10   # number of flips

prob_1 = stats.binom.pmf(x, n, 0.5)
print("Probability of getting 3 heads")
print(prob_1)

# P(more than 2 heads) = 1 - P(0) - P(1) - P(2)
prob_2 = 1 - stats.binom.pmf(0, n=10, p=.5) - stats.binom.pmf(1, n=10, p=.5) - stats.binom.pmf(2, n=10, p=.5)
print("Probability of getting more than 2 heads")
print(prob_2)
