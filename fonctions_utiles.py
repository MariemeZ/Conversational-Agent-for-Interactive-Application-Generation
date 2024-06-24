# -*- coding: utf-8 -*-
import json
import random
from correspondance_nom import entite_correspondance
import spacy
from spacy.tokens import Span

def check_etapes_restantes(data_file,output_file,etapes):
    with open(data_file, 'r') as file1 , open(output_file, 'r') as file2:
       data_file = json.load(file1)
       output_file = json.load(file2)
       
       for rule in data_file["rules"]:
           etape = rule["etape"]
           pattern = rule["pattern"] 
           if len(output_file[pattern])==0:
               etapes.append(pattern)
    return etapes


def generer_reponse_generale(liste_etapes,type_aide):
    paragraphe ="Pour finaliser le processus de génération de votre application, voici les étapes qui restent à accomplir : \n"
    num_etape = 1
    for etape in liste_etapes:
        if type_aide == "specification":
            with open("C:\\Users\\USER\\Desktop\ST2I\\data_aide_reponse.json", 'r', encoding='utf-8') as file:
                data_file = json.load(file)
                for rule in data_file["rules"]:
                    if rule["pattern"] == etape:
                        instructions = rule["instructions"]
                        break
                instrcution = random.choice(instructions)

                paragraphe += str(num_etape) + ") " + instrcution + "\n"
                aide_generale = random.choice(data_file["assistance_supplementaire"])
                
        else : # type_aide == "explication"
            True
        num_etape += 1
    paragraphe += aide_generale
    return paragraphe

def get_num_precedence_etape_actuelle(etape): #get le numero les les etapes qui precedent l'etape actuelle
    with open("C:\\Users\\USER\\Desktop\ST2I\\data_aide_reponse.json", 'r', encoding='utf-8') as file:
        liste_etape_precendence=[]
        num_etape_actuelle=0
        data_file = json.load(file)
        for rule in data_file["rules"]:
            if rule["pattern"] == etape:
                num_etape_actuelle = rule["etape"]
                liste_etape_precendence = rule["precedence"]
                break
    return num_etape_actuelle, liste_etape_precendence
    


def verifier_dependance_etapes_precedentes(etape):
    liste_etapes=[]
    with open("C:\\Users\\USER\\Desktop\ST2I\\data_aide_reponse.json", 'r', encoding='utf-8') as file:
        data_file = json.load(file)
        num_etape_actuelle, etapes_precendentes = get_num_precedence_etape_actuelle(etape)
      
        # if etapes_precendentes != None: #dans le cas ou il n'ya pas de sous etapes
        #     return liste_etapes
        # else:
        #     return etapes_precendentes
        return etapes_precendentes


def generer_reponse_specifique(etape,type_etape,type_aide, etapes):
    print('etapes eli lezemni')
    print(etapes)
    if etapes ==None:
        with open("C:\\Users\\USER\\Desktop\ST2I\\data_aide_reponse.json", 'r', encoding='utf-8') as file:
            data_file = json.load(file)
            for rule in data_file["rules"]:
                if rule["pattern"] == etape:
                    if type_etape =="etape":
                        nom_etape = rule["nom_etape"]
                        if type_aide =="specifcation":

                            instructions = rule["instructions"]
                            instrcution = random.choice(instructions)
                            
                            conseils = rule["conseils"]
                            conseil = random.choice(conseils)

                            exemples = rule["valeur_par_defaut"]
                            exemple = random.choice(exemples)

                            reponse = "Bien sûr ! Vous avez demandé de l'aide pour l'étape de " + nom_etape +". Voici des informations détaillées pour vous aider :\n"
                            reponse += instrcution + "\n"
                            reponse += conseil + "\n"
                            reponse += "vous pouvez dire par exemple je veux que " + nom_etape + " soit " + exemple 
                            aide_generale = random.choice(data_file["assistance_supplementaire"])
                            reponse += aide_generale

                            return reponse
                        
                        elif type_aide =="explication":
                            explication_detaillee = rule["explication_detaillee"]
                            
                            assistances = rule["assistance"]
                            assistance = random.choice(assistances)

                            reponse = "Bien sûr ! Vous avez demandé de l'aide pour l'étape de " + nom_etape +". Voici des informations détaillées pour vous aider :\n"
                            reponse += explication_detaillee + "\n"
                            reponse += assistance + "\n"

                            aide_generale = random.choice(data_file["assistance_supplementaire"])
                            reponse += aide_generale

                            return reponse


                    elif type_etape == "sous-etape":
                        True
                        
                    break
    else : # famma des dependences
        reponse = "Bien sûr, je suis là pour vous aider ! Cependant, veuillez noter que l'étape que vous avez mentionnée dépend de la fin des étapes précédentes pour être réalisée avec succès. Voici les étapes que vous devrez accomplir avant de pouvoir avancer :"
        num =1
        with open("C:\\Users\\USER\\Desktop\ST2I\\data_aide_reponse.json", 'r', encoding='utf-8') as file:
            data_file = json.load(file)
            for rule in data_file["rules"]:
                num_etape = rule["etape"]
                if num_etape in etapes:
                    reponse += str(num) + ") " + random.choice(rule["instructions"]) + "\n"
                    num +=1
                
        reponse += "Une fois que vous aurez terminé ces étapes, vous serez prêt à aborder l'étape que vous avez mentionnée. Si vous avez des questions sur les étapes précédentes ou si vous avez besoin d'assistance pour les compléter, n'hésitez pas à me demander. \n"
        return reponse


def change_value_in_outputFile(new_value,entite):
    with open("C:\\Users\\USER\\Desktop\ST2I\\output.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    if entite in data:
        # Vérifier si new_value est un objet Span
        if isinstance(new_value, Span):
            new_value = convert_span_to_dict(new_value)
        # Mettre à jour la clé entite avec la nouvelle valeur
        data[entite] = new_value



    with open("C:\\Users\\USER\\Desktop\ST2I\\output.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    message =f"Parfait, j'ai bien noté votre demande de modification pour l'étape {entite} avec la nouvelle valeur {new_value}. Je vais mettre à jour ces informations."
    
    return message

def convert_span_to_dict(span):
    return  [(span.text)]
        # Autres informations pertinentes
    
 

def update_outputFile(entity,new_value,action,nlp):
    with open("C:\\Users\\USER\\Desktop\ST2I\\output.json", "r", encoding='utf-8') as f:
        data = json.load(f)

    # Vérifier si l'entité existe dans le fichier
    
    if entity in data:
        if action == "add":
            data[entity].append(str(new_value))
            message = f"La valeur '{new_value}' a été ajoutée avec succés.\n"
        elif action == "delete":

            span_texts = [nlp(text).text for text in data[entity]]  # Convert all values to Span and get their texts
 
            if new_value.text in span_texts:  # Compare directly with the span text
                data[entity].remove(new_value.text)
                message = f"La valeur '{new_value.text}' a été supprimée avec succès.\n"
            else:
                message = f"La valeur '{new_value.text}' n'existe pas.\n"
        else:
            message = "Action non reconnue. Utilisez 'add' ou 'delete'."

        # Écrire les modifications dans le fichier
        #print(data)
        with open("C:\\Users\\USER\\Desktop\ST2I\\output.json", "w", encoding='utf-8') as f:
            try:
                json.dump(data, f, indent=4)
            except Exception as e:
                print(f"An error occurred: {e}")
            
        
        return message



def tatalite_infos():
    reponse =""
    with open("C:\\Users\\USER\\Desktop\ST2I\\output.json", "r") as f:
        data = json.load(f)
    #correspondance entre les noms d'entites dans un autre fichier
    for entite in data: 
        nom_entite= entite_correspondance.get(entite, "Entité non trouvée")
        if len(data[entite]) != 0:
            reponse += nom_entite + " : "
            for info in data[entite]:
                reponse += info + ","
            reponse += ";"
    
    return reponse


# def infos_spe(entite):
#     reponse =""
#     with open("C:\\Users\\USER\\Desktop\ST2I\\output.json", "r") as f:
#         data = json.load(f)
#     #en cas aana barcha naamlou for
#     nom_entite= entite_correspondance.get(entite, "Entité non trouvée")

#     if len(data[entite]) != 0:
#             reponse += nom_entite + " : "
#             for info in data[entite]:
#                 reponse += info + ","
#             reponse += "; \n"
#     else :
#         reponse = " Je suis désolé, mais je n'ai pas d'informations préalables sur cette étape. Pourriez-vous s'il vous plaît me fournir des détails sur cette étape spécifique ?"

   
    
#     return reponse

def infos_spe(entites):
    
    reponse =""
    with open("C:\\Users\\USER\\Desktop\ST2I\\output.json", "r") as f:
        data = json.load(f)
    liste_nom_entite = [entite_correspondance.get(entite, "Entité non trouvée") for entite in entites]
    print("listaa")
    print(liste_nom_entite)
    for entite, nom_entite in zip(entites, liste_nom_entite):
        reponse += nom_entite + " : "
        for info in data[entite]:
                reponse += info + ","
                reponse += "; \n"

    
    return reponse




def formater_texte(texte):
    lignes = texte.strip().split(';')

    # Parcourez les lignes et formatez-les correctement
    for ligne in lignes:
        # Séparez la ligne en deux parties en utilisant le premier ':'
        if ':' in ligne:
            entite, valeur = ligne.split(":",1)
            # Supprimez les espaces inutiles autour de l'entité et de la valeur
            entite = entite.strip()
            valeur = valeur.strip()
            # Imprimez le résultat formaté
            print(f"{entite}: {valeur}")

       

def check_dict_values(dictionary):
    full_lists = {}
    for key, value in dictionary.items():
        if len(value["value"]) > 0:
            full_lists[key] = value["value"]
    return full_lists

def generer_reponse_fournir_infos(dict):
    reponse =""
    for key, value in dict.items():
        nom_entite= entite_correspondance.get(key, "Entité non trouvée")
        reponse += "- " +nom_entite + " : "
        for val in value:
            reponse += val + ", "
        reponse += "\n"
    return reponse
        
def get_objectif_aide(previous_statement):
    model_path = "C:/Users/USER/Desktop/ST2I/modele_aide"
    nlp = spacy.load(model_path)

    # Ajouter le composant sentencizer au pipeline

    if "sentencizer" not in nlp.pipe_names:
        nlp.add_pipe("sentencizer")
    
    doc_temp=nlp(previous_statement)
    for sent in doc_temp.sents:
        for ent in sent.ents:
            liste_1=eval(ent.label_)
            entite = liste_1[0]
            return(entite)
    
        
