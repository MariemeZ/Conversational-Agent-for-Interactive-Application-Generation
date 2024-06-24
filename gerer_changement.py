import spacy
import json
import re
import numpy as np
import random
from fonctions_utiles import change_value_in_outputFile,update_outputFile


liste_noEtape_noValue = [
    "Pour que je puisse vous aider efficacement, pourriez-vous me fournir l'étape que vous souhaitez modifier et la nouvelle valeur que vous aimeriez ajouter ou remplacer ?",
    "Afin de mieux vous assister, pourriez-vous préciser quelle étape vous souhaitez modifier et quelle nouvelle valeur vous aimeriez introduire ?",
    "Pour que je puisse répondre à votre demande, pourriez-vous me donner plus de détails ? Quelle étape voulez-vous changer et quelle nouvelle valeur souhaitez-vous ajouter ou remplacer ?",
    "Je suis là pour vous aider, mais j'aurais besoin de plus de détails. Pouvez-vous me dire quelle étape vous voulez modifier et quelle nouvelle valeur vous voulez mettre en place ?",
    "Bien sûr, je peux vous aider avec cela. Pourriez-vous préciser quelle étape vous souhaitez modifier et quelle nouvelle valeur vous aimeriez utiliser ?",
    "Afin que je puisse avancer, pouvez-vous me dire quelle étape vous souhaitez modifier et quelle nouvelle valeur vous souhaitez apporter ?"
]

liste_noEtape =[
    "Pour vous aider au mieux, pourriez-vous me préciser quelle nouvelle valeur vous aimeriez attribuer à l'étape : ",
    "Je vous accompagne volontiers. Pour que je puisse continuer, pourriez-vous me donner des détails sur la nouvelle valeur à attribuer à l'étape : ",
    "Afin de personnaliser cette modification, pourriez-vous me dire quelle nouvelle valeur vous avez en tête pour l'étape : "
]

# Chargement du modèle entraîné
model_path = "C:/Users/USER/Desktop/ST2I/modele_changement"
nlp = spacy.load(model_path)

# Ajouter le composant sentencizer au pipeline
if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer")



#new_text = "Je souhaite changer les langues prises en charge"

def gerer_changement(new_text):
    doc = nlp(new_text)
    reponse_chatbot =""
    for sent in doc.sents:
        for ent in sent.ents:
            liste_1=eval(ent.label_)
            entite = liste_1[0]
            if len(liste_1) == 1:
                if entite == "None":
                    reponse_chatbot += random.choice(liste_noEtape_noValue)
                else :
                    reponse_chatbot += random.choice(liste_noEtape) + entite
            elif len(liste_1) == 2:
                reponse_chatbot+= f"Parfait, j'ai bien noté votre demande de modification pour l'étape {entite}. Je vais mettre à jour ces informations.\n"
                new_value= ent
                reponse_chatbot += change_value_in_outputFile(new_value,entite)
            else: 
                new_value = ent
                action = liste_1[2]
                reponse_chatbot += update_outputFile(entite,new_value,action,nlp)    
    return reponse_chatbot


#print(gerer_changement(new_text))


        