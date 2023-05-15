import numpy as np

# Set the number of trials (i.e., the number of times the die is thrown)
n = 2

# Set the number we're interested in (i.e., the number 5)
k = 5

# Set the probability of getting a 5 on a single throw of the die
p = 1/6

# Set the number of simulations
num_simulations = 100000

# Simulate rolling the die n times
rolls = np.random.randint(1, 7, size=(num_simulations, n))

# Calculate the number of times the number of interest appears in each simulation
counts = np.sum(rolls == 5, axis=1)

# Calculate the probability of getting zero or one 5 in two throws of the die
p_not_k_sim = np.mean(counts == 0)
p_at_least_k_sim = np.mean(counts >= 1)

# Print the simulated probabilities and compare to the theoretical ones
print("Simulated probability of not getting {} on any of the {} throws: {:.4f}".format(k, n, p_not_k_sim))
print("Simulated probability of getting {} on at least one of the {} throws: {:.4f}".format(k, n, p_at_least_k_sim))

