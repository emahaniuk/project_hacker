# NumPy is imported, seed is set
import numpy as np
sd = np.random.seed(123)

# Starting step
step = 50

# Roll the dice (Roll the dice. Use randint() to create the variable dice.)
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step = step - 1

# if dice is 3, 4 or 5, you go one step up.
elif dice <= 5:
    step = step + 1

# Else, you throw the dice again. The number of eyes is the number of steps you go up.
else :
    step = step + dice

# Print out dice and step
print(dice)
print(step)