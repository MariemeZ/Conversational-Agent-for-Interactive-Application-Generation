from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from data_intentions import data

# 1. Collecte et préparation des données
texts = [sentence for sentence, _ in data]  # Liste des textes d'entraînement
labels = [intent for _, intent in data]  # Liste des étiquettes correspondantes

# 2. Création d'un ensemble d'entraînement et d'un ensemble de test
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

# 3. Extraction des caractéristiques des textes
vectorizer = TfidfVectorizer()
train_features = vectorizer.fit_transform(train_texts)
test_features = vectorizer.transform(test_texts)

# 4. Entraînement du modèle
classifier = MultinomialNB()
classifier.fit(train_features, train_labels)

# 5. Évaluation du modèle
predictions = classifier.predict(test_features)
#print(classification_report(test_labels, predictions))

# 6. Prédiction sur de nouvelles données
# new_texts = [...]  # Liste des nouveaux textes à prédire
# new_features = vectorizer.transform(new_texts)
# new_predictions = classifier.predict(new_features)
# print(new_predictions)
