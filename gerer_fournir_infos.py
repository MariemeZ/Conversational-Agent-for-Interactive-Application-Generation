import spacy
import json
import re
import numpy as np
from Levenshtein import ratio
from training_data import test_data
from fuzzysearch import find_near_matches

from training_data import training_data
from spacy.training import offsets_to_biluo_tags
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MultiLabelBinarizer

# Chargement du modèle entraîné
model_path = "C:/Users/USER/Desktop/ST2I/modele"
nlp = spacy.load(model_path)

# Ajouter le composant sentencizer au pipeline
if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer")


def detecter_entites_personnalisees(message):
    doc = nlp(message)
    entites_personnalisees = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ["nomApplication", "frontendWorkspace", "backendWorkspace"]]
    return entites_personnalisees

def gerer_message(message):
    rep=""
    entites_personnalisees = detecter_entites_personnalisees(message)
    if entites_personnalisees:
        for entite, type_entite in entites_personnalisees:
            if type_entite == "nomApplication":
                # Exécuter l'action correspondant à la création d'une application avec le nom 'entite'
                rep+="Nom de l'application: {}.\n".format(entite)
            if type_entite == "frontendWorkspace":
                # Exécuter l'action correspondant à l'entité 'frontendWorkspace'
                rep+= "Frontend Workspace: {}.\n".format(entite)
            if type_entite == "backendWorkspace":
                # Exécuter l'action correspondant à l'entité 'backendWorkspace'
                rep+="Backend Workspace: {}.\n".format(entite)
    else:
        # Gérer le cas où aucune entité n'a été détectée
        rep= "Je ne comprends pas votre demande."
    return rep
# text="Je souhaite développer une nouvelle application sous le nom de MyApp et je veux que l'espace de travail pour la parite frontend soit dans le dossier TestFront et celui de la partie back dans TestBack."
# print(gerer_message(text))



#*********prediction des entites *********

def predict_entities(text):
    doc = nlp(text)
    predicted_entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    return predicted_entities

# for text, true_entities in test_data:
#     predicted_entities = predict_entities(text)
#     print("Phrase :", text)
#     print("Entités prédites :", predicted_entities)
#     print("Entités réelles :", true_entities)
#     print()



#********* evaluation du modele *********

# evaluate_model(test_data)
def evaluate_model(test_data):
    # Extraction des entités réelles de l'ensemble de test
    true_entities = [entities["entities"] for _, entities in test_data]

    # Prédiction des entités pour l'ensemble de test
    predicted_entities = [predict_entities(text) for text, _ in test_data]
    # Obtention de toutes les entités réelles et prédites
    all_true_entities = [entity for entities in true_entities for entity in entities]
    all_predicted_entities = [entity for entities in predicted_entities for entity in entities]


    # Obtention des classes détectées
    true_classes = list(set([entity[2] for entity in all_true_entities]))
    predicted_classes = list(set(entity[2] for entity in all_predicted_entities))
    classes = sorted(list(set(true_classes + predicted_classes)))

    # Conversion en matrice binaire
    mlb = MultiLabelBinarizer(classes=classes)
    true_entities_bin = mlb.fit_transform(true_entities)
    predicted_entities_bin = mlb.transform(predicted_entities)

    # Obtention des étiquettes des classes
    labels = mlb.classes_

    # Affichage du rapport d'évaluation
    print("Rapport d'évaluation :")
    print(classification_report(true_entities_bin, predicted_entities_bin, labels=range(len(labels)), target_names=labels, zero_division=1))

    # Génération de la matrice de confusion
    true_indices = np.where(np.isin(labels, [entity[2] for entity in all_true_entities]))[0]
    predicted_indices = np.where(np.isin(labels, all_predicted_entities))[0]
    confusion_mat = confusion_matrix(true_indices, predicted_indices)
    print("Matrice de confusion :")
    print(confusion_mat)


#evaluate_model(test_data)

#============================================
#****fin d'evaluation du modele ************
#============================================
def check_microservice_match(input_string, microservices):
    input_string = input_string.lower()  # Convertir la chaîne en minuscules pour la correspondance
    input_string = re.sub(r'\W', '', input_string)  # Supprimer les caractères non alphabétiques

    for microservice in microservices:
        microservice = microservice.lower()
        microservice = re.sub(r'\W', '', microservice)

        # Vérifier la correspondance exacte
        if input_string == microservice:
            return True,microservice

        # Vérifier la correspondance de l'acronyme
        if input_string == ''.join([w[0] for w in microservice.split()]):
            return True,microservice

        # Vérifier la correspondance de la première lettre de chaque mot
        if input_string == ''.join([w[0] for w in microservice.split()]):
            return True,microservice
        if input_string == ''.join([w[0] for w in microservice.split()]) or input_string in microservice:
            return True,microservice
        
    return False,microservice


def separate_words(string):
    separated_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
    return separated_string

def check_etape_in_doc(etape, doc, threshold=0.6):
    nlp1 = spacy.load("fr_core_news_sm")
    nlp1.add_pipe('sentencizer')
    etape = separate_words(etape)
    doc=nlp1(doc)
    for sentence in doc.sents:
        matches = find_near_matches(etape, sentence.text, max_l_dist=int(len(etape) * (1 - threshold)))
        print(matches)
        if len(matches) > 0:
            return True
    return False



ner = nlp.get_pipe("ner")
labels = list(ner.labels)

# if "aide" in labels:
#     labels.remove("aide")


microservices_par_defaut=["Gateway","Eureka"]
microservices_predefinis=["GED","Administration","Reporting"]

def extract_entities(text):
    
    entities = {}
    current_step=None
    help_intent=False
    doc = nlp(text)
    with open("C:\\Users\\USER\\Desktop\ST2I\\data_aide_reponse.json", 'r', encoding='utf-8') as file:
        data_file = json.load(file)
        for cle in labels:
            for rule in data_file["rules"]:
                if rule["pattern"] == cle:
                    entities[cle] = {"max": rule["max_value"], "value": []}


  
    for ent in doc.ents:
        print(ent.text,"->")
        print(ent.label_)
        if ent.label_ in entities:
                if ent.label_ =="microservices":
                    #print(check_microservice_match(ent.text,microservices_par_defaut))
                    value_bool_default, value_entity_default= check_microservice_match(ent.text,microservices_par_defaut)
                    value_bool_predefini, value_entity_predefini= check_microservice_match(ent.text,microservices_predefinis)
                    if value_bool_default :
                        entities[ent.label_]["value"].append(value_entity_default)
                    elif value_bool_predefini:
                        entities[ent.label_]["value"].append(value_entity_predefini)
                    else:
                        entities[ent.label_]["value"].append(ent.text)
                else:   
                    entities[ent.label_]["value"].append(ent.text)
                if ent.label_ =="microservices" or ent.label_ =="langue" or ent.label_ =="profilsPartieServeur":
                    entities[ent.label_]["max"]="1+"


    # Vérification de l'alignement de l'entité
    doc = nlp.make_doc(text)
    entities_offsets = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    tags = offsets_to_biluo_tags(doc, entities_offsets)
    aligned_entities = []
    for tag, entity in zip(tags, entities_offsets):
        if tag != "-":
            aligned_entities.append(entity)
    # fin de la Vérification de l'alignement de l'entité
  
    print(entities)
    return entities


# text = "Je souhaite développer une nouvelle application sous le nom de MyApp,qui peut etre traduite en Francais ou en Anglais, et je veux que l'espace de travail pour la partie frontend soit dans le dossier TestFront et celui de la partie back dans TestBack.En ce qui concerne les profils de la partie back, je veux les configurer en mode test et prod. j'ai besoin de l'assistance dans l'etape de definition des microservices "

# resultat=extract_entities(text)
# print(json.dumps(resultat, indent=4))
