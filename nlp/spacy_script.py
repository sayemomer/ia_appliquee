import spacy
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")
doc = nlp("I prefer a direct flight to Chicago.")
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)