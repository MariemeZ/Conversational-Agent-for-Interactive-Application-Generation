import spacy
from spacy.training import Example
from spacy.training.iob_utils import offsets_to_biluo_tags

from aide_entites import data_aide



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
ner.add_label("etape")
ner.add_label("sous-etape")
ner.add_label("explication")
ner.add_label("specification")
ner.add_label("None")



# Entraînement du modèle
optimizer = nlp.initialize()
for i in range(10):  # Nombre d'itérations d'entraînement
    for text, annotations in data_aide:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], sgd=optimizer)


# new_text = "Je souhaite spécifier les langues que mon application doit prendre en charge."
# doc = nlp(new_text)
# for ent in doc.ents:
#     print(ent.text, ent.label_)


output_dir = "C:/Users/USER/Desktop/ST2I/modele_aide"
nlp.to_disk(output_dir)