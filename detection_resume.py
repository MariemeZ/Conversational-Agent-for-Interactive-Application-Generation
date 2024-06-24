import spacy
from spacy.training import Example
from spacy.training.iob_utils import offsets_to_biluo_tags

from resume_entites import data_resume


# Chargement du modèle vide
nlp = spacy.blank("fr")

# Ajout du composant NER au pipeline
ner = nlp.add_pipe("ner")

# Ajout des entités personnalisées
ner.add_label("nomApplication")
ner.add_label("frontendWorkspace")
ner.add_label("backendWorkspace")
ner.add_label("langue")
ner.add_label("profilsPartieServeur")
ner.add_label("microservices")
# ner.add_label("none")




# Entraînement du modèle
optimizer = nlp.initialize()
for i in range(10):  # Nombre d'itérations d'entraînement
    for text, annotations in data_resume:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], sgd=optimizer)




output_dir = "C:/Users/USER/Desktop/ST2I/modele_resume"
nlp.to_disk(output_dir)