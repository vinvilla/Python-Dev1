
import random

random.seed(1)

print('Generating a random sequence of 4 numbers...')
print([random.randint(1, 100) for i in range(5)])

# Reset the seed to 1 again
random.seed(1)

# We now get the same sequence
print([random.randint(1, 100) for i in range(5)])
