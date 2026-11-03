# M17 Lesson 2 - Activity 3: Addition Rule
# P(A or B) = P(A) + P(B) - P(A and B)

def prob_a_or_b(a, b, all_possible_outcomes):
    prob_a = len(a) / len(all_possible_outcomes)
    prob_b = len(b) / len(all_possible_outcomes)
    inter = a.intersection(b)
    prob_inter = len(inter) / len(all_possible_outcomes)
    return prob_a + prob_b - prob_inter

evens = {2, 4, 6}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

print('Probability of Getting an even number or a number greater than 2')
print(prob_a_or_b(evens, greater_than_two, all_possible_rolls))
