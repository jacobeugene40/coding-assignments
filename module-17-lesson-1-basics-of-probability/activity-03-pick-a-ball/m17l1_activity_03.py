# M17 Lesson 1 - Activity 3: Pick a Ball
import random

def pick_ball_experiment():
    balls = ['Blue', 'Red', 'Green']
    result = random.choice(balls)

    pro = balls.count('Red') / len(balls)
    print("Probability of Picking Red Ball is:", round(pro, 3))

    if result == 'Red':
        return 'Red Ball was Picked'
    else:
        return 'Better Luck Next Time'

res = pick_ball_experiment()
print(res)
