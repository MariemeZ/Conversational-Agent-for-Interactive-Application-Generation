import spacy
import json
import re
import numpy as np
from Levenshtein import ratio
from training_data import test_data
from fuzzysearch import find_near_matches
from gerer_fournir_infos import extract_entities
from training_data import training_data
from spacy.training import offsets_to_biluo_tags
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MultiLabelBinarizer
from analyse_intentions import classifier,vectorizer

# Chargement du modèle entraîné
model_path = "C:/Users/USER/Desktop/ST2I/modele"
nlp = spacy.load(model_path)

# Ajouter le composant sentencizer au pipeline
if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer")


ner = nlp.get_pipe("ner")
labels = list(ner.labels)

microservices_par_defaut=["Gateway","Eureka"]
microservices_predefinis=["GED","Administration","Reporting"]


#text = "Je souhaite développer une nouvelle application sous le nom de MyApp,qui peut etre traduite en Francais ou en Anglais, et je veux que l'espace de travail pour la partie frontend soit dans le dossier TestFront et celui de la partie back dans TestBack.En ce qui concerne les profils de la partie back, je veux les configurer en mode test et prod. j'ai besoin de l'assistance dans l'etape de definition des microservices "

# resultat=extract_entities(text)
# print(json.dumps(resultat, indent=4))


new_texts = [
    "je veux creer une application SIMep dont le nom du frontend est front-workspace et le back est workspace du backend"
    
    # "J'ai besoin d'aide pour cette etape.",
    # "j'aimerai changer des details pour le microservice "
]

# Assurez-vous que le vectorizer et le classifier ont été créés et entraînés comme dans l'exemple précédent.

# Transformation des nouveaux textes en caractéristiques
new_features = vectorizer.transform(new_texts)

# Prédiction des catégories des nouveaux textes
new_predictions = classifier.predict(new_features)
print(new_predictions)
if new_predictions=="fournir_infos":
    resultat=extract_entities(new_texts[0])
    print(json.dumps(resultat, indent=4))

# Affichage des prédictions
#print(new_predictions)