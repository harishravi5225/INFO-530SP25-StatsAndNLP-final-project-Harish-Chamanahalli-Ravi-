# Named Entity Recognition (NER) with spaCy

Welcome! This tutorial project explores **Named Entity Recognition (NER)** using the open-source NLP library [spaCy](https://spacy.io/).

## 👋 About the Author

My name is **Harish Chamanahalli Ravi**, and this tutorial is part of my exploration into Natural Language Processing (NLP). The project focuses on leveraging spaCy's capabilities for recognizing and extracting meaningful named entities from text.

---

## 📌 Project Overview

**Named Entity Recognition (NER)** is the process of identifying and categorizing key elements in text such as:

- **People**
- **Organizations**
- **Locations**
- **Dates**
- **Monetary values**

This tutorial covers:

- Performing NER using a pre-trained spaCy model
- Visualizing entities using `displaCy`
- Customizing and fine-tuning the NER model with new entity labels
- Real-world use cases like parsing job postings and news articles

---

## 🔧 Installation & Setup

### 1. Create a Virtual Environment (Recommended)

```bash
# macOS/Linux
python3 -m venv ner_env
source ner_env/bin/activate

# Windows
python -m venv ner_env
ner_env\Scripts\activate
```

### 2. Install Required Packages

```bash
pip install -U spacy
python -m spacy download en_core_web_sm
```

### 3. (Optional) For Notebooks & Visualization

```bash
pip install notebook
pip install matplotlib
```

---

## 🧪 Run Your First NER Example

```python
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple was founded by Steve Jobs in California."

# Process and extract entities
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
```

---

## 🎨 Visualizing Named Entities

spaCy provides a built-in visualizer tool:

```python
from spacy import displacy

doc = nlp("Google was founded in Mountain View.")
displacy.serve(doc, style="ent")
```

Or in a Jupyter Notebook:

```python
displacy.render(doc, style="ent", jupyter=True)
```

---

## 🛠️ Customizing & Fine-Tuning the NER Model

You can train spaCy to recognize new entity types (like `PRODUCT`):

```python
TRAIN_DATA = [
    ("I bought a new iPhone 13", {"entities": [(16, 26, "PRODUCT")]}),
    ("She uses a MacBook Air", {"entities": [(12, 23, "PRODUCT")]}),
]
```

Then use the `Example` and `update` method to fine-tune the model.

---

## 🧠 Real-World Use Cases

- 📄 Resume parsing
- 📰 Extracting names and companies from news articles
- 📈 Job post analysis
- 📦 Product name recognition

---

## ✅ Conclusion

With spaCy, you can:

- Quickly get started with pre-trained NER
- Build production-ready NLP pipelines
- Extend models to support your custom entities

---

## 📚 Resources

- [spaCy 101](https://spacy.io/usage/spacy-101)
- [NER Visualizer (displaCy)](https://spacy.io/usage/visualizers)
- [Free spaCy Course](https://course.spacy.io)

---

## 📁 Project Files

- `ner_spacy_tutorial.html` – Full HTML tutorial
- `README.md` – You're reading it!
- `examples/` – Python files demonstrating NER usage (optional if added)

Happy NLP-ing! 🤖
