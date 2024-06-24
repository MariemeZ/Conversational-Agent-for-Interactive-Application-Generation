import spacy
from spacy.training import Example
from spacy.training.iob_utils import offsets_to_biluo_tags

from changement_entites import data_changement



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
ner.add_label("new_valeur")
ner.add_label("delete")
ner.add_label("add")
ner.add_label("None")




# Entraînement du modèle
optimizer = nlp.initialize()
for i in range(10):  # Nombre d'itérations d'entraînement
    for text, annotations in data_changement:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], sgd=optimizer)



output_dir = "C:/Users/USER/Desktop/ST2I/modele_changement"
nlp.to_disk(output_dir)