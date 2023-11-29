import nltk
nltk.download('punkt')
from nltk.util import ngrams

sentence = "Loola nikee. Aloka bibi vo. Vo bibi loola. Loola nikee bibi vo. Vo. Vo. Aloka bibi loola. Loola aloka aloka. Loola loola. Nikee nikee nikee. Bibi vo. Bibi vo. Vo Vo. Nikee loola."
n = 2  # for bigrams

#ignore the punctuation
sentence = sentence.replace('.', '')
#ignore the capitalization
sentence = sentence.lower()
# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# genetate unigrams

unigrams = list(ngrams(tokens, 1))

print(unigrams)

# Count the number of times each unigram occurs
from collections import Counter
unigram_counts = Counter(unigrams)
print(unigram_counts)
# Generate n-grams
bigrams = list(ngrams(tokens, n))
# print(bigrams)

# Count the number of times each bigram occurs
from collections import Counter
bigram_counts = Counter(bigrams)
# print(bigram_counts)

#sort the bigrams by lexical order
bigrams_sorted = sorted(bigram_counts.items(), key=lambda item: item[0])
print(bigrams_sorted)


