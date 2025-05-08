# ner_spacy_example.py

import spacy
from spacy import displacy

# Load model
nlp = spacy.load("en_core_web_sm")

# Example 1: Basic NER
text1 = "Apple is looking at buying U.K. startup for $1 billion"
doc1 = nlp(text1)
print("\n--- Example 1: Basic NER ---")
for ent in doc1.ents:
    print(ent.text, ent.label_)

# Example 2: From news article
text2 = "Google and Microsoft are competing in the AI market in 2025."
doc2 = nlp(text2)
print("\n--- Example 2: News Article ---")
for ent in doc2.ents:
    print(ent.text, ent.label_)

# Example 3: From job posting
text3 = "We're hiring at Amazon for data scientists in Seattle."
doc3 = nlp(text3)
print("\n--- Example 3: Job Posting ---")
for ent in doc3.ents:
    print(ent.text, ent.label_)
