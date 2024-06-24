# -*- coding: utf-8 -*-
import spacy
import json
import re
import numpy as np
from fonctions_utiles import check_etapes_restantes, verifier_dependance_etapes_precedentes,generer_reponse_generale, generer_reponse_specifique

# Chargement du modèle entraîné
model_path = "C:/Users/USER/Desktop/ST2I/modele_aide"
nlp = spacy.load(model_path)

# Ajouter le composant sentencizer au pipeline

if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer")



new_text = "Pouvez-vous m'aider à comprendre les étapes restantes pour finaliser mon application ?"

def gerer_aide(new_texte):


    doc = nlp(new_texte)

    etapes_previous=[]
    reponse=""
    previous_help=None
    for sent in doc.sents:
        for ent in sent.ents:
            liste_1=eval(ent.label_)
            entite = liste_1[0]
            type_etape = liste_1[1]
            type_aide = liste_1[2]
            
            if entite == "None" and type_etape == "None":
                list1=check_etapes_restantes("C:\\Users\\USER\\Desktop\\ST2I\\data_aide_reponse.json","C:\\Users\\USER\\Desktop\\ST2I\\output.json",etapes_previous) 
                reponse += generer_reponse_generale(list1,type_aide)
                
            else: 
                list2=verifier_dependance_etapes_precedentes(entite)
                reponse += generer_reponse_specifique(entite,type_etape,type_aide,list2)
    print(reponse)
    return reponse



