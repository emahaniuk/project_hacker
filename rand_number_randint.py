# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice (Use randint() with the appropriate arguments to randomly generate the integer
# 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out.)
sim_dice = np.random.randint(1, 7)
print(sim_dice)

# Use randint() again
sim_dice = np.random.randint(1, 7)
print(sim_dice)