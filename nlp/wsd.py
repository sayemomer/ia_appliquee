import math

# Given probabilities from the training corpus with add 0.5 smoothing
prob_the_bank1 = (5 + 0.5) / (30 + 0.5 * 50)
prob_the_bank2 = (3 + 0.5) / (12 + 0.5 * 50)
prob_potomac_bank1 = (0 + 0.5) / (55 + 0.5 * 50)
prob_potomac_bank2 = (1 + 0.5) / (37 + 0.5 * 50)

# P(BANK1) and P(BANK2) given
p_bank1 = 5 / 7
p_bank2 = 2 / 7

# Using logs to avoid underflow
score_bank1 = math.log(p_bank1) + math.log(prob_the_bank1) + math.log(prob_potomac_bank1)
score_bank2 = math.log(p_bank2) + math.log(prob_the_bank2) + math.log(prob_potomac_bank2)

score_bank1, score_bank2
