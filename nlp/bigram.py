# Corpus sentences
corpus_sentences = [
    "<s> I am Sam </s>",
    "<s> Sam I am </s>",
    "<s> I do not like green eggs and ham </s>"
]

# Tokenize the corpus
tokens = [word for sentence in corpus_sentences for word in sentence.split()]
# print("Tokens:" + str(tokens))

# Function to calculate the count of a single token
def count_token(token, tokens):
    print("token:" + str(token))
    print("tokens.count(token):" + str(tokens.count(token)))
    return tokens.count(token)

# Function to calculate the count of bigrams
def count_bigram(bigram, tokens):
    bigram_as_str = ' '.join(bigram)
    print("bigram_as_str:" + str(bigram_as_str))
    print(' '.join(tokens).count(bigram_as_str))
    return ' '.join(tokens).count(bigram_as_str)

# Function to calculate bigram probability
def bigram_prob(bigram, tokens):
    return count_bigram(bigram, tokens) / count_token(bigram[0], tokens)

# Define bigrams
bigrams_to_compute = [
    ("I", "<s>"),
    ("</s>", "Sam"),
    ("<s>", "Sam"),
    ("am", "I"),
    ("Sam", "I"),
    ("do", "I")
]

# Calculate probabilities
bigram_probs = {}
for bigram in bigrams_to_compute:
    probability = bigram_prob(bigram, tokens)
    bigram_probs[bigram] = probability

print("Bigram probabilities:" + str(bigram_probs))
