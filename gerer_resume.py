import spacy
import json
import re
import numpy as np
import random
from fonctions_utiles import tatalite_infos,infos_spe,formater_texte



# Chargement du modèle entraîné
model_path = "C:/Users/USER/Desktop/ST2I/modele_resume"
nlp = spacy.load(model_path)

# Ajouter le composant sentencizer au pipeline
if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer")


new_text="Pourriez-vous me rappeler les langues que j'ai sélectionnées ?"

#new_text = "Je veux savoir ce que j'ai deja introduit comme valeur pour le nom de mon application"
#new_text = "Répétez ce que j'ai dit auparavant."

def gerer_resume(new_text):
    print(new_text)
    doc = nlp(new_text)
    reponse_chatbot =""

    for sent in doc.sents:
        print("entites::")
        print(sent.ents)
        print(len(sent.ents))

        if len(sent.ents) ==0:
            reponse_chatbot += tatalite_infos()
        else:
            for ent in sent.ents:
                # liste_1=eval(ent.label_)
                # entite = str(liste_1)
                # print(liste_1)
                entite = ent.label_
                print("entiteeeee")
                print(entite)
                reponse_chatbot += infos_spe(list(entite))
                        
    return reponse_chatbot

# reponse_chatbot = gerer_resume(new_text)
# print(reponse_chatbot)
#print(formater_texte(reponse_chatbot))



        