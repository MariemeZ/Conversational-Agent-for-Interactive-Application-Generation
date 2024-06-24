from gerer_fournir_infos import extract_entities
from segmentation_input import segment_text
from fonctions_utiles import check_dict_values,generer_reponse_fournir_infos,get_objectif_aide
from gerer_aide import gerer_aide
from gerer_changement import gerer_changement
from gerer_resume import gerer_resume
import json


def fournir_aide(sentence):
    return "aide"


def gerer_chevauchement_infos(entity):
    reponse =f"Je suis désolé, mais vous avez déjà ajouté le nombre maximum autorisé de {entity}. Vous ne pouvez plus ajouter d'autres {entity}."
    return reponse


def save_entities_to_json(entities, filename):
    reponse=""
    
    with open(filename, 'r') as file:
        data = json.load(file)

    print(entities)
    for entity, value in entities.items():
        if value["max"] == "1":
            if len(value['value']) > 1 :
                reponse=gerer_chevauchement_infos(entity)
            else:
                data[entity]=value["value"]
        else:
            if len(value['value'])!=0 :
                data[entity]=value["value"]


    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    return reponse
    

def process_intent(intent_data):
    resultat=""
    resultat_fournir_infos="Merci pour les informations que vous m'avez fournies:\n"
    reponse_chevauchement=""
    resultat_demande_aide=""
    resultat_demande_changement=""
    resultat_demande_resume=""
    reponse_temp_aide=""
    previous_intent=""
    previous_statement=""
    for sentence, intent in intent_data:
        print(sentence)
        print(intent)
        if intent == 'fournir_infos':
            informations = extract_entities(sentence)
            reponse_chevauchement=save_entities_to_json(informations, "output.json")
            resultat_fournir_infos +=generer_reponse_fournir_infos(check_dict_values(informations))
            #resultat="Informations extraites :"+ (json.dumps(check_dict_values(informations), indent=4))

        elif intent == 'demande_aide':

            if previous_intent=="demande_aide":
                objectif=str(get_objectif_aide(previous_statement))
                if objectif=="None":
                    reponse = gerer_aide(sentence)
                    print('reponse')
                    print(reponse)
                    reponse_temp_aide=""
                    resultat_demande_aide += reponse
            else:
                objectif=get_objectif_aide(sentence)
                if objectif=="None":
                    reponse = gerer_aide(sentence)
                    reponse_temp_aide = reponse
                else:
                    reponse = gerer_aide(sentence)
                    resultat_demande_aide += reponse

            
            resultat_demande_aide += reponse_temp_aide

                
            #print("Réponse à la demande d'aide :", reponse)
        
        elif intent == 'demande_changement':
            resultat_demande_changement = gerer_changement(sentence)
            #print("Réponse à la demande de changement :", reponse)
        elif intent =="demande_infos":
            print('lena')
            resultat_demande_resume += gerer_resume(sentence)

        else:
            # Cas pour les intentions non reconnues
            print("Intention non reconnue :", intent)
        previous_intent=intent
        previous_statement=sentence
    if len(resultat_fournir_infos)!= 54:
        resultat+=resultat_fournir_infos
    resultat+=resultat_demande_aide
    resultat+=resultat_demande_changement
    resultat+=resultat_demande_resume
    if len(reponse_chevauchement)!=0:
        resultat+=reponse_chevauchement

    return resultat

# input_text = "Je souhaite développer une nouvelle application sous le nom de MyApp,qui peut etre traduite en Francais ou en Anglais, et je veux que l'espace de travail pour la partie frontend soit dans le dossier TestFront et celui de la partie back dans TestBack.En ce qui concerne les profils de la partie back, je veux les configurer en mode test et prod. j'ai besoin de l'assistance dans l'etape de definition des microservices "

# result = segment_text(input_text)
# process_intent(result)


def process_app(input_text):
    result = segment_text(input_text)
    reponse=process_intent(result)
    return(reponse)

