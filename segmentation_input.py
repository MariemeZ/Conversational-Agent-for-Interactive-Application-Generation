import spacy
from analyse_intentions import classifier,vectorizer

def segment_text(text):
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    intents = vectorizer.transform(sentences)
    new_predictions = classifier.predict(intents)

    return list(zip(sentences, new_predictions))

# Example usage
# input_text = "Je souhaite développer une nouvelle application sous le nom de MyApp,qui peut etre traduite en Francais ou en Anglais, et je veux que l'espace de travail pour la partie frontend soit dans le dossier TestFront et celui de la partie back dans TestBack.En ce qui concerne les profils de la partie back, je veux les configurer en mode test et prod. j'ai besoin de l'assistance dans l'etape de definition des microservices "

# result = segment_text(input_text)
# print(result)

