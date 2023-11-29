# Define the bigram probabilities given in the problem
bigram_probabilities = {
    ('<s>', 'I'): 0.25,
    ('I', 'want'): 0.65,
    ('want', 'to'): 0.32,
    ('to', 'eat'): 0.26,
    ('eat', 'British'): 0.001,
    ('British', 'food'): 0.6,
    ('food', '</s>'): 0.25
}

# Define the sentence
sentence = '<s> I want to eat British food </s>'.split()

# Function to calculate sentence probability
def calculate_sentence_probability(sentence, bigram_probabilities):
    probability = 1.0
    for i in range(len(sentence)-1):
        bigram = (sentence[i], sentence[i+1])
        probability *= bigram_probabilities.get(bigram, 0) # get the probability or return 0 if not found
    return probability

# Calculate the sentence probability
sentence_probability = calculate_sentence_probability(sentence, bigram_probabilities)
print("Probability of the sentence: " + str(sentence_probability))
