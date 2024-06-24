
from training_data import training_data
data_fournir_infos=[(ligne[0],"fournir_infos") for ligne in training_data]



data = [("Pouvez-vous me rappeler le nom de l'application que j'ai spécifié auparavant ?", "demande_infos"),
        ("Quels microservices ai-je déjà inclus dans mon projet ?", "demande_infos"),
        ("Récapitulez les langues que j'ai sélectionnées pour mon application.", "demande_infos"),
        ("Quels sont les profils de la partie serveur que j'ai déjà spécifiés ?", "demande_infos"),
        ("Quels sont les détails que j'ai fournis pour la partie web de mon application ?", "demande_infos"),
        ("Donnez-moi un résumé des configurations que j'ai effectuées pour la partie serveur.", "demande_infos"),
        ("J'aimerais revoir les informations que j'ai déjà données. Pouvez-vous me les rappeler ?", "demande_infos"),
        ("Donnez-moi un récapitulatif des détails que j'ai déjà mentionnés.", "demande_infos"),
        ("Je souhaite obtenir un récapitulatif de toutes les informations que j'ai fournies jusqu'à présent", "demande_infos"),
        ("Pouvez-vous me rappeler les détails que j'ai déjà inclus dans le processus de développement ?", "demande_infos"),
        ("Est-il possible d'avoir un aperçu des étapes que j'ai déjà complétées ?", "demande_infos"),
        ("Est-ce que vous pouvez me dire ce que j'ai déjà enregistré dans ma demande ?", "demande_infos"),
        ("Je souhaiterais obtenir un récapitulatif des détails que j'ai précédemment fournis.", "demande_infos"),
        ("Quels sont les éléments que j'ai déjà spécifiés dans ma demande ?", "demande_infos"),
        ("Pourriez-vous me donner un résumé des données que j'ai déjà entrées ?", "demande_infos"),
        ("Je souhaite savoir quels éléments ont déjà été inclus dans ma demande..", "demande_infos"),
        ("Est-il possible d'avoir un résumé des étapes que j'ai déjà terminées dans le processus de développement ?", "demande_infos"),
        ("J'aimerais avoir une vue d'ensemble des détails que j'ai déjà fournis dans ma demande.", "demande_infos"),
        ("Quelles sont les données que j'ai déjà spécifiées jusqu'à présent dans ma demande ?", "demande_infos"),
        ("Pouvez-vous me rappeler les informations que j'ai déjà fournies concernant le champ du nom de l'application ?", "demande_infos"),
        ("Est-il possible d'avoir un aperçu des informations que j'ai déjà incluses dans le champ du nom de l'application ?", "demande_infos"),
        ("Pouvez-vous me rappeler le nom de mon application ?",  "demande_infos"),
        ("Quel était le nom que j'ai donné à mon application ?", "demande_infos"),
        ("Résumez le nom de l'application que j'ai spécifié.",  "demande_infos"),
        ("Revenons sur le nom que j'ai choisi pour mon application.",  "demande_infos"),
        ("Peux-tu me dire le nom de l'application que j'ai enregistré ?", "demande_infos"),
        ("Quel est le nom que j'ai indiqué pour mon application ?", "demande_infos"),
        ("Je veux un rappel du nom de l'application que j'ai inscrit.", "demande_infos"),
        ("Pourriez-vous récapituler le nom que j'ai mis pour mon application ?",  "demande_infos"),
        ("Quel nom d'application ai-je enregistré ?",  "demande_infos"),
        ("Répétez le nom de l'application que j'ai spécifié.", "demande_infos"),
        ("Je veux savoir ce que j'ai deja introduit comme valeur pour le nom de mon application",  "demande_infos"),
        ("Pouvez-vous me rappeler le nom de mon espace de travail frontend ?",  "demande_infos"),
        ("Quel était le nom que j'ai donné à ma zone de travail côté client ?",  "demande_infos"),
        ("Résumez l'espace de travail frontend que j'ai spécifié.", "demande_infos"),
        ("Revenons sur le nom de mon espace de travail côté client.", "demande_infos"),
        ("Peux-tu me dire comment s'appelle mon espace de travail frontend ?",  "demande_infos"),
        ("Quel est le nom que j'ai indiqué pour mon espace de travail côté client ?",  "demande_infos"),
        ("Je veux un rappel du nom de mon espace de travail frontend.", "demande_infos"),
        ("Pourriez-vous récapituler l'espace de travail frontend que j'ai spécifié ?", "demande_infos"),
        ("Quel espace de travail côté client ai-je enregistré ?", "demande_infos"),
        ("Répétez le nom de mon espace de travail côté client.",  "demande_infos"),
        ("Quel est le nom de ma zone de travail frontend ?", "demande_infos"),
        ("Dis-moi le nom de mon environnement frontend.", "demande_infos"),
        ("Pouvez-vous me rappeler le nom de mon espace de travail backend ?", "demande_infos"),
        ("Quel était le nom que j'ai donné à ma zone de travail côté serveur ?",  "demande_infos"),
        ("Résumez l'espace de travail backend que j'ai spécifié.", "demande_infos"),
        ("Revenons sur le nom de mon espace de travail côté serveur.",  "demande_infos"),
        ("Peux-tu me dire comment s'appelle mon espace de travail backend ?",  "demande_infos"),
        ("Quel est le nom que j'ai indiqué pour mon espace de travail côté serveur ?",  "demande_infos"),
        ("Je veux un rappel du nom de mon espace de travail backend.",  "demande_infos"),
        ("Pourriez-vous récapituler l'espace de travail backend que j'ai spécifié ?",  "demande_infos"),
        ("Quel espace de travail côté serveur ai-je enregistré ?",  "demande_infos"),
        ("Répétez le nom de mon espace de travail côté serveur.",  "demande_infos"),
        ("Quel est le nom de ma zone de travail backend ?",  "demande_infos"),
        ("Dis-moi le nom de mon environnement backend.",  "demande_infos"),
        ("Pouvez-vous me rappeler le profil de ma partie serveur ?", "demande_infos"),
        ("Quel profil ai-je spécifié pour la partie serveur de mon application ?",  "demande_infos"),
        ("Résumez le profil de la partie serveur que j'ai indiqué.",  "demande_infos"),
        ("Revenons sur le profil de ma partie serveur.",  "demande_infos"),
        ("Peux-tu me dire quel profil j'ai choisi pour ma partie serveur ?",  "demande_infos"),
        ("Quel est le profil que j'ai défini pour ma partie serveur ?",  "demande_infos"),
        ("Je veux un rappel du profil de ma partie serveur.",  "demande_infos"),
        ("Pourriez-vous récapituler le profil de la partie serveur que j'ai spécifié ?",  "demande_infos"),
        ("Quel profil ai-je enregistré pour la partie serveur ?", "demande_infos"),
        ("Répétez le profil de ma partie serveur.",  "demande_infos"),
        ("Quel est le profil de ma partie serveur ?",  "demande_infos"),
        ("Dis-moi le profil de ma partie serveur.", "demande_infos"),
        ("Quels microservices ai-je sélectionnés pour mon projet ?",  "demande_infos"),
        ("J'aimerais revoir les microservices que j'ai spécifiés",  "demande_infos"),
        ("Pourriez-vous m'indiquer les microservices que j'ai enregistrés ?",  "demande_infos"),
        ("Donnez-moi une liste des microservices que j'ai définis.",  "demande_infos"),
        ("Je veux un rappel des microservices que j'ai choisis pour mon application.",  "demande_infos"),
        ("Pouvez-vous me dire quels microservices sont enregistrés pour mon projet ?",  "demande_infos"),
        ("Affichez les microservices que j'ai configurés.", "demande_infos"),
        ("Besoin de connaître les microservices que j'ai spécifiés.", "demande_infos"),
        ("Répétez la liste des microservices que j'ai enregistrés.",  "demande_infos"),
        ("Répétez les microservices que j'ai définis.", "demande_infos"),
        ("Quels sont les microservices que j'ai configurés pour mon application ?",  "demande_infos"),
        ("Quels sont les microservices que j'ai mentionnés précédemment ?",  "demande_infos"),
        ("Pourriez-vous me rappeler les langues que j'ai sélectionnées ?", "demande_infos"),
        ("Affichez la liste des langues que j'ai enregistrées.",  "demande_infos"),
        ("Quelles langues ai-je spécifiées pour mon application ?",  "demande_infos"),
        ("Pouvez-vous me dire quelles langues sont configurées pour mon projet ?",  "demande_infos"),
        ("Besoin de connaître les langues que j'ai choisies.",  "demande_infos"),
        ("Répétez la liste des langues que j'ai définies.",  "demande_infos"),
        ("Quelles sont les langues que j'ai précédemment enregistrées ?",  "demande_infos"),
        ("Pouvez-vous me rappeler les détails que j'ai fournis sur mon application ?",  "demande_infos"),
        ("Pouvez-vous me rappeler ce que j'ai dit précédemment ?",  "demande_infos"),
        ("Quelles informations ai-je fournies jusqu'à présent ?",  "demande_infos"),
        ("Affichez-moi un récapitulatif de ce que j'ai introduit.",  "demande_infos"),
        ("Répétez ce que j'ai dit auparavant.",  "demande_infos"),
        ("Pouvez-vous rappeler les détails que j'ai fournis ?",  "demande_infos"),
        ("Quelles sont les informations que j'ai déjà mentionnées ?",  "demande_infos"),
        ("Affichez-moi les données que j'ai déjà partagées.", "demande_infos"),
        ("Quels sont les éléments que j'ai déjà communiqués ?",  "demande_infos"),
        ("Besoin d'un rappel sur les détails que j'ai donnés.",  "demande_infos"),
        ("Pouvez-vous me rappeler le nom de mon application ?", "demande_infos"),
        ("Quel était le nom que j'ai donné à mon application ?", "demande_infos"),
        ("Résumez le nom de l'application que j'ai spécifié.", "demande_infos"),
        ("Revenons sur le nom que j'ai choisi pour mon application.", "demande_infos"),
        ("Peux-tu me dire le nom de l'application que j'ai enregistré ?", "demande_infos"),
        ("Quel est le nom que j'ai indiqué pour mon application ?", "demande_infos"),
        ("Je veux un rappel du nom de l'application que j'ai inscrit.", "demande_infos"),
        ("Pourriez-vous récapituler le nom que j'ai mis pour mon application ?", "demande_infos"),
        ("Quel nom d'application ai-je enregistré ?", "demande_infos"),
        ("Répétez le nom de l'application que j'ai spécifié.", "demande_infos"),
        ("Je veux savoir ce que j'ai deja introduit comme valeur pour le nom de mon application","demande_infos"),
        ("Pouvez-vous me rappeler le nom de mon espace de travail frontend ?", "demande_infos"),
        ("Quel était le nom que j'ai donné à ma zone de travail côté client ?", "demande_infos"),
        ("Résumez l'espace de travail frontend que j'ai spécifié.", "demande_infos"),
        ("Revenons sur le nom de mon espace de travail côté client.", "demande_infos"),
        ("Peux-tu me dire comment s'appelle mon espace de travail frontend ?", "demande_infos"),
        ("Quel est le nom que j'ai indiqué pour mon espace de travail côté client ?", "demande_infos"),
        ("Je veux un rappel du nom de mon espace de travail frontend.", "demande_infos"),
        ("Pourriez-vous récapituler l'espace de travail frontend que j'ai spécifié ?", "demande_infos"),
        ("Quel espace de travail côté client ai-je enregistré ?", "demande_infos"),
        ("Répétez le nom de mon espace de travail côté client.", "demande_infos"),
        ("Quel est le nom de ma zone de travail frontend ?", "demande_infos"),
        ("Dis-moi le nom de mon environnement frontend.", "demande_infos"),
        ("Pouvez-vous me rappeler le nom de mon espace de travail backend ?", "demande_infos"),
        ("Quel était le nom que j'ai donné à ma zone de travail côté serveur ?", "demande_infos"),
        ("Résumez l'espace de travail backend que j'ai spécifié.", "demande_infos"),
        ("Revenons sur le nom de mon espace de travail côté serveur.", "demande_infos"),
        ("Peux-tu me dire comment s'appelle mon espace de travail backend ?", "demande_infos"),
        ("Quel est le nom que j'ai indiqué pour mon espace de travail côté serveur ?", "demande_infos"),
        ("Je veux un rappel du nom de mon espace de travail backend.", "demande_infos"),
        ("Pourriez-vous récapituler l'espace de travail backend que j'ai spécifié ?", "demande_infos"),
        ("Quel espace de travail côté serveur ai-je enregistré ?", "demande_infos"),
        ("Répétez le nom de mon espace de travail côté serveur.", "demande_infos"),
        ("Quel est le nom de ma zone de travail backend ?", "demande_infos"),
        ("Dis-moi le nom de mon environnement backend.", "demande_infos"),
        ("Pouvez-vous me rappeler le profil de ma partie serveur ?", "demande_infos"),
        ("Quel profil ai-je spécifié pour la partie serveur de mon application ?", "demande_infos"),
        ("Résumez le profil de la partie serveur que j'ai indiqué.", "demande_infos"),
        ("Revenons sur le profil de ma partie serveur.", "demande_infos"),
        ("Peux-tu me dire quel profil j'ai choisi pour ma partie serveur ?", "demande_infos"),
        ("Quel est le profil que j'ai défini pour ma partie serveur ?","demande_infos"),
        ("Je veux un rappel du profil de ma partie serveur.", "demande_infos"),
        ("Pourriez-vous récapituler le profil de la partie serveur que j'ai spécifié ?", "demande_infos"),
        ("Quel profil ai-je enregistré pour la partie serveur ?", "demande_infos"),
        ("Répétez le profil de ma partie serveur.", "demande_infos"),
        ("Quel est le profil de ma partie serveur ?", "demande_infos"),
        ("Dis-moi le profil de ma partie serveur.", "demande_infos"),
        ("Quels microservices ai-je sélectionnés pour mon projet ?", "demande_infos"),
        ("J'aimerais revoir les microservices que j'ai spécifiés", "demande_infos"),
        ("Pourriez-vous m'indiquer les microservices que j'ai enregistrés ?", "demande_infos"),
        ("Donnez-moi une liste des microservices que j'ai définis.", "demande_infos"),
        ("Je veux un rappel des microservices que j'ai choisis pour mon application.", "demande_infos"),
        ("Pouvez-vous me dire quels microservices sont enregistrés pour mon projet ?", "demande_infos"),
        ("Affichez les microservices que j'ai configurés.", "demande_infos"),
        ("Besoin de connaître les microservices que j'ai spécifiés.", "demande_infos"),
        ("Répétez la liste des microservices que j'ai enregistrés.", "demande_infos"),
        ("Répétez les microservices que j'ai définis.", "demande_infos"),
        ("Quels sont les microservices que j'ai configurés pour mon application ?", "demande_infos"),
        ("Quels sont les microservices que j'ai mentionnés précédemment ?", "demande_infos"),
        ("Pourriez-vous me rappeler les langues que j'ai sélectionnées ?", "demande_infos"),
        ("Affichez la liste des langues que j'ai enregistrées.", "demande_infos"),
        ("Quelles langues ai-je spécifiées pour mon application ?", "demande_infos"),
        ("Pouvez-vous me dire quelles langues sont configurées pour mon projet ?", "demande_infos"),
        ("Besoin de connaître les langues que j'ai choisies.", "demande_infos"),
        ("Répétez la liste des langues que j'ai définies.", "demande_infos"),
        ("Quelles sont les langues que j'ai précédemment enregistrées ?", "demande_infos"),


        ("Pouvez-vous m'aider à comprendre les prochaines étapes du développement de mon application ?", "demande_aide"),
        ("Quelles sont les étapes clés que je dois suivre pour terminer mon application ?", "demande_aide"),
        ("J'ai besoin d'assistance pour savoir ce que je dois faire ensuite dans le processus de développement. Pouvez-vous m'aider ?", "demande_aide"),
        ("Aidez-moi à comprendre les étapes restantes pour finaliser mon application.", "demande_aide"),
        ("Je suis un peu perdu, pouvez-vous me guider dans les prochaines étapes ?", "demande_aide"),
        ("Est-ce que vous pouvez m'expliquer plus en détail cette partie du processus ?", "demande_aide"),
        ("Je ne suis pas sûr de savoir comment aborder cette étape, pouvez-vous me donner des indications ?", "demande_aide"),
        ("J'aimerais obtenir des conseils supplémentaires sur la meilleure approche à suivre pour cette partie du développement.", "demande_aide"),
        ("Je souhaite améliorer ma compréhension de cette fonctionnalité, pouvez-vous m'en dire plus à ce sujet ?", "demande_aide"),
        ("J'aimerais obtenir des conseils pour progresser dans le processus de développement.", "demande_aide"),
        ("Je souhaite recevoir des indications supplémentaires sur cette partie du processus.", "demande_aide"),
        ("Je me sens un peu perdu, j'apprécierais votre assistance pour me guider.", "demande_aide"),
        ("Je ne suis pas sûr(e) de la façon de choisir les caractéristiques des microservices, pouvez-vous me donner des conseils ?", "demande_aide"),
        ("Pouvez-vous m'aider à comprendre comment spécifier les informations pour chaque étape du processus de développement ?", "demande_aide"),
        ("J'aimerais obtenir des suggestions sur la manière de spécifier les valeurs par défaut pour les entités.", "demande_aide"),
        ("Comment puis-je savoir si j'ai rempli correctement toutes les informations nécessaires pour chaque étape ?", "demande_aide"),
        ("Je ne sais pas comment spécifier les informations pour les microservices GED, Reporting et Administration, pouvez-vous me montrer comment le faire ?", "demande_aide"),
        ("Comment puis-je ajouter mes propres microservices avec des caractéristiques personnalisées ?", "demande_aide"),
        ("J'ai besoin d'assistance pour comprendre comment spécifier les caractéristiques des microservices prédéfinis.", "demande_aide"),
        ("Pouvez-vous me guider sur la manière de spécifier le nom de l'application ?", "demande_aide"),
        ("Je voudrais obtenir des conseils sur la manière de spécifier les langues que peut supporter mon application. Pouvez-vous m'aider ?", "demande_aide"),
        ("Aidez-moi à comprendre comment spécifier les profils de la partie serveur pour mon application.", "demande_aide"),
        ("Je ne suis pas sûr(e) de la meilleure façon de spécifier les microservices Eureka et Gateway. Pouvez-vous me donner des indications ?", "demande_aide"),
        ("Pouvez-vous m'aider à comprendre comment spécifier les informations par défaut pour chaque entité ?", "demande_aide"),
        ("J'ai besoin d'aide pour savoir si j'ai rempli correctement toutes les informations nécessaires pour chaque étape du processus de développement.", "demande_aide"),
        ("Je souhaite ajouter mes propres microservices avec des caractéristiques personnalisées. Comment puis-je faire cela ?", "demande_aide"),
        ("J'aimerais obtenir des suggestions sur la manière de spécifier les valeurs par défaut pour les entités. Pouvez-vous me montrer comment faire ?", "demande_aide"),
        ("Aidez-moi à comprendre comment spécifier les caractéristiques des microservices prédéfinis comme GED, Reporting et Administration.", "demande_aide"),
        ("Je suis un peu perdu(e) concernant la spécification des informations pour la partie web de mon application. Pouvez-vous me guider ?", "demande_aide"),
        ("Pouvez-vous m'expliquer en détail comment spécifier les profils de la partie serveur pour mon application ?", "demande_aide"),
        ("j'ai besoin d'aide pour accomplir cette étape", "demande_aide"),
        ("je veux que tu m'aides dans cette etape", "demande_aide"),
        ("je suis un peu perdu", "demande_aide"),
        ("Je ne sais pas comment spécifier les informations pour la partie serveur de mon application, pouvez-vous m'aider à comprendre cette étape ?", "demande_aide"),
        ("Aidez-moi à comprendre comment spécifier le nom de l'application de manière précise et unique.", "demande_aide"),
        ("J'ai besoin d'assistance pour comprendre comment spécifier les informations pour les microservices GED, Reporting et Administration. Pouvez-vous me donner des indications ?", "demande_aide"),
        ("Quelle est l'étape de spécification des microservices prédéfinis ?",  "demande_aide"),
        ("Qu'est-ce que l'étape de configuration des microservices implique ?", "demande_aide"),
        ("Pouvez-vous m'expliquer l'étape de spécification des microservices ?",  "demande_aide"),
        ("Je suis un peu perdu concernant l'explication de la configuration des microservices.",   "demande_aide"),
        ("Je ne sais pas comment spécifier les informations pour les microservices GED, Reporting et Administration, pouvez-vous me montrer comment le faire ?",  "demande_aide"),
        ("Je ne sais pas comment spécifier les informations pour  GED, Reporting, Administration et Gestion des admins, pouvez-vous me montrer comment le faire ?",  "demande_aide"),
        ("Pour la partie frontend, j'aimerais savoir comment spécifier les URL des microservices.",  "demande_aide"),
        ("En ce qui concerne les microservices, j'aimerais obtenir des conseils pour choisir les valeurs.",  "demande_aide"),
        ("J'ai besoin d'aide pour comprendre la spécification des microservices GED, Reporting et Administration.", "demande_aide"),
        ("Je souhaite obtenir des informations détaillées sur les microservices GED, Reporting et Administration.",  "demande_aide"),
        ("Pouvez-vous m'expliquer en détail l'étape de spécification des microservices GED, Reporting et Administration ?",   "demande_aide"),
        ("J'aimerais obtenir des informations détaillées sur la spécification des microservices GED, Reporting et Administration.", "demande_aide"),
        ("J'ai besoin d'aide pour comprendre l'explication de la spécification des microservices GED, Reporting et Administration.", "demande_aide"),
        ("Comment spécifier le nom de mon application ?",  "demande_aide"),
        ("En quoi consiste l'étape de spécification du nom de l'application ?",  "demande_aide"),
        ("Pouvez-vous m'aider à comprendre les prochaines étapes du développement de mon application ?",  "demande_aide"),
        ("J'ai besoin d'aide pour spécifier les langues que mon application doit prendre en charge.",  "demande_aide"),
        ("J'ai besoin d'aide pour configurer les profils de la partie backend de mon application.", "demande_aide"),
        ("Pouvez-vous m'aider à comprendre les étapes restantes pour finaliser mon application ?", "demande_aide"),
        ("Je suis un peu perdu quant à la manière de configurer les profils de la partie serveur, pouvez-vous me donner des instructions détaillées ?", "demande_aide"),
        ("Pourriez-vous m'expliquer en détail l'étape de spécification des langues ?",  "demande_aide"),
        ("Je ne comprends pas bien l'étape de configuration des profils de la partie serveur, pouvez-vous m'aider ?", "demande_aide"),
        ("Qu'en est-il de l'étape de définition des langages supportés ? Je ne suis pas sûr de la comprendre.",  "demande_aide"),



        ("Je souhaite apporter quelques modifications à l'étape du nom de l'application.", "demande_changement"),
        ("Peut-on ajuster les informations concernant le nom de la partie serveur ?", "demande_changement"),
        ("J'aimerais changer certains détails concernant la partie web.", "demande_changement"),
        ("Est-il possible de faire des ajustements aux langues prises en charge par l'application ?", "demande_changement"),
        ("Pouvez-vous effectuer des modifications aux profils de la partie serveur ?", "demande_changement"),
        ("Je voudrais apporter des changements aux microservices spécifiés.", "demande_changement"),
        ("Peut-on ajuster les caractéristiques des microservices pré-définis tels que Eureka et Gateway ?", "demande_changement"),
        ("J'aimerais changer certains détails concernant le microservice GED.", "demande_changement"),
        ("Est-ce que nous pouvons ajuster les informations du microservice Reporting ?", "demande_changement"),
        ("Pouvez-vous effectuer des modifications aux caractéristiques du microservice Administration ?", "demande_changement"),
        ("Je souhaite apporter quelques ajustements à l'étape du nom de l'application.", "demande_changement"),
        ("Peut-on modifier les informations concernant le nom de la partie serveur ?", "demande_changement"),
        ("J'aimerais ajuster certains détails concernant la partie web.", "demande_changement"),
        ("J'aimerais apporter quelques modifications à une étape que j'ai déjà complétée.", "demande_changement"),
        ("Comment puis-je ajuster une étape que j'ai déjà enregistrée ?", "demande_changement"),
        ("Pouvez-vous m'aider à changer certaines informations que j'ai déjà incluses dans ma demande ?", "demande_changement"),
        ("J'aimerais effectuer des ajustements à une partie spécifique de ma demande d'informations.", "demande_changement"),
        ("Est-il possible de modifier les données que j'ai fournies pour une étape déjà terminée ?", "demande_changement"),
        ("Je me suis trompé dans le nom de l'application, comment puis-je le changer ?", "demande_changement"),
        ("J'aimerais ajuster le nom de l'application que j'ai saisi, comment faire ?", "demande_changement"),
        ("Puis-je revenir en arrière et changer le nom de l'application que j'ai donné ?", "demande_changement"),
        ("Je veux effectuer des ajustements aux caractéristiques du microservice XYZ que j'ai spécifié précédemment", "demande_changement"),
        ("Peut-on changer les informations concernant le microservice Eureka ?", "demande_changement"),
        ("J'aimerais apporter des modifications aux langues que j'ai précédemment spécifiées pour l'application.", "demande_changement"),
        ("Est-ce que je peux ajuster les profils de la partie serveur que j'ai déjà enregistrés ?", "demande_changement"),
        ("Je souhaite changer les détails concernant le microservice GED que j'ai inclus dans ma demande initiale.", "demande_changement"),
        ("Pouvez-vous m'aider à modifier certaines informations que j'ai déjà fournies pour les microservices pré-définis comme Gateway ?", "demande_changement"),
        ("J'aimerais effectuer des changements aux microservices que j'ai choisis, y compris celui appelé Reporting.", "demande_changement"),
        ("Peut-on ajuster les caractéristiques du microservice Administration que j'ai inclus dans ma demande d'informations ?", "demande_changement"),
        ("Je voudrais apporter quelques modifications aux langues prises en charge par l'application, est-ce possible ?", "demande_changement"),
        ("Est-il possible de faire des ajustements aux profils de la partie serveur que j'ai spécifiés pour mon application ?", "demande_changement"),
        ("Je voudrais apporter des modifications à mon application. Pouvez-vous m'aider ?", "demande_changement"),
        ("Est-il possible de faire des ajustements dans mon application ?", "demande_changement"),
        ("J'aimerais effectuer des changements dans mon application. Comment puis-je procéder ?", "demande_changement"),
        ("Je souhaite mettre à jour mon application. Comment faire pour changer des éléments ?","demande_changement"),
        ("Y a-t-il un moyen de modifier des éléments dans mon application ?","demande_changement"),
        ("Comment puis-je faire des modifications dans mon application ?", "demande_changement"),
        ("Je veux apporter des changements à mon application. Par où dois-je commencer ?", "demande_changement"),
        ("Je souhaite changer le nom de l'application.","demande_changement"),
        ("Pouvez-vous m'aider à modifier le nom de l'application ?", "demande_changement"),
        ("Est-il possible de changer le nom de l'application ?", "demande_changement"),
        ("Je veux mettre à jour le nom de l'application.", "demande_changement"),
        ("Peut-on changer le nom de l'application ?", "demande_changement"),
        ("Je voudrais modifier le nom de l'application.", "demande_changement"),
        ("Comment puis-je changer le nom de l'application ?", "demande_changement"),
        ("Je souhaite changer le nom de mon application.", "demande_changement"),
        ("Pouvez-vous m'expliquer comment changer le nom de l'application ?", "demande_changement"),
        ("J'aimerais savoir comment changer le nom de l'application.", "demande_changement"),
        ("Je souhaite changer le nom de l'application en MyAppGenial.","demande_changement"),
        ("Pouvez-vous m'aider à modifier le nom de l'application pour MonAppMeilleure ?","demande_changement"),
        ("Est-il possible de changer le nom de l'application en SuperApp ?", "demande_changement"),
        ("Je veux mettre à jour le nom de l'application vers NouveauNomApp.", "demande_changement"),
        ("Peut-on changer le nom de l'application en NomApplicationCool ?", "demande_changement"),
        ("Je voudrais modifier le nom de l'application pour AppAmeliorée.", "demande_changement"),
        ("Comment puis-je changer le nom de l'application en MonAppParfaite ?","demande_changement"),
        ("Je souhaite changer le nom de mon application en SuperAppGenius.", "demande_changement"),
        ("Pouvez-vous m'expliquer comment changer le nom de l'application en TopApp ?","demande_changement"),
        ("J'aimerais savoir comment changer le nom de l'application en MyAppUltimate.", "demande_changement"),
        ("Je souhaite changer l'espace de travail pour la partie frontend.","demande_changement"),
        ("Pouvez-vous m'aider à modifier l'espace de travail de la partie web ?", "demande_changement"),
        ("Est-il possible de changer l'espace de travail pour le frontend ?","demande_changement"),
        ("Je veux mettre à jour l'espace de travail pour la partie web.","demande_changement"),
        ("Peut-on changer l'espace de travail de la partie frontend ?","demande_changement"),
        ("Je voudrais modifier l'espace de travail pour l'interface web.", "demande_changement"),
        ("Comment puis-je changer l'espace de travail de la partie client ?", "demande_changement"),
        ("Je souhaite changer l'espace de travail pour la partie web de mon application.", "demande_changement"),
        ("Pouvez-vous m'expliquer comment changer l'espace de travail de la partie frontend ?","demande_changement"),
        ("J'aimerais savoir comment changer l'espace de travail pour l'interface utilisateur.", "demande_changement"),
        ("Je souhaite changer l'espace de travail pour la partie frontend en 'NouvelEspaceFrontend'.", "demande_changement"),
        ("Pouvez-vous m'aider à modifier l'espace de travail de la partie web vers 'NouveauFrontendWorkspace' ?","demande_changement"),
        ("Est-il possible de changer l'espace de travail pour le frontend en 'EspaceWebModifié' ?","demande_changement"),
        ("Je veux mettre à jour l'espace de travail pour la partie web avec 'NouveauWorkspace'.", "demande_changement"),
        ("Peut-on changer l'espace de travail de la partie frontend en 'FrontendRenouvelé' ?","demande_changement"),
        ("Je voudrais modifier l'espace de travail pour l'interface web vers 'EspaceModifié'.", "demande_changement"),
        ("Comment puis-je changer l'espace de travail de la partie client à 'NouveauClientWorkspace' ?", "demande_changement"),
        ("Je souhaite changer l'espace de travail pour la partie web de mon application en 'EspaceNouveau'.", "demande_changement"),
        ("Pouvez-vous m'expliquer comment changer l'espace de travail de la partie frontend en 'WorkspaceActualisé' ?", "demande_changement"),
        ("J'aimerais savoir comment changer l'espace de travail pour l'interface utilisateur vers 'NouvelEspaceClient'.","demande_changement"),
        ("Je souhaite changer l'espace de travail pour la partie serveur.", "demande_changement"),
        ("Pouvez-vous m'aider à modifier l'espace de travail de la partie serveur ?","demande_changement"),
        ("Est-il possible de changer l'espace de travail pour le backend ?", "demande_changement"),
        ("Je veux mettre à jour l'espace de travail pour la partie serveur.", "demande_changement"),
        ("Peut-on changer l'espace de travail de la partie serveur ?", "demande_changement"),
        ("Je voudrais modifier l'espace de travail pour le serveur.", "demande_changement"),
        ("Comment puis-je changer l'espace de travail de la partie backend ?", "demande_changement"),
        ("Je souhaite changer l'espace de travail pour la partie serveur de mon application.","demande_changement"),
        ("Pouvez-vous m'expliquer comment changer l'espace de travail de la partie backend ?", "demande_changement"),
        ("J'aimerais savoir comment changer l'espace de travail pour le serveur.", "demande_changement"),
        ("Je souhaite changer l'espace de travail backend en 'MonEspaceBackend'.", "demande_changement"),
        ("Pouvez-vous m'aider à modifier l'espace de travail du backend pour 'NouveauBackend' ?", "demande_changement"),
        ("Est-il possible de changer l'espace de travail pour le backend en 'Backend2023' ?","demande_changement"),
        ("Je veux mettre à jour l'espace de travail backend avec 'NouvelEspace' comme nom.","demande_changement"),
        ("Peut-on changer l'espace de travail du backend en 'EspaceModifié' ?", "demande_changement"),
        ("Je voudrais modifier l'espace de travail pour le backend en 'MonBackendEspace'.", "demande_changement"),
        ("Comment puis-je changer l'espace de travail de la partie backend en 'NouveauWorkspace' ?","demande_changement"),
        ("Je souhaite changer l'espace de travail backend pour 'EspaceDeTravail2022'.", "demande_changement"),
        ("Pouvez-vous m'expliquer comment changer l'espace de travail de la partie backend en 'BackendWorkspace' ?","demande_changement"),
        ("J'aimerais savoir comment changer l'espace de travail pour le backend en 'NouveauBackendEspace'.", "demande_changement"),
        ("Je souhaite changer les langues prises en charge.","demande_changement"),
        ("Pouvez-vous m'aider à modifier les langages supportés ?", "demande_changement"),
        ("Est-il possible de changer les langues de l'application ?", "demande_changement"),
        ("Peut-on changer les langages utilisés dans l'application ?", "demande_changement"),
        ("Je voudrais modifier les langues de mon application.", "demande_changement"),
        ("Comment puis-je changer les langages supportés par l'application ?","demande_changement"),
        ("Je souhaite changer les langues de mon projet.","demande_changement"),
        ("Pouvez-vous m'expliquer comment modifier les langages de l'application ?", "demande_changement"),
        ("J'aimerais savoir comment mettre à jour les langages pris en charge.", "demande_changement"),
        ("Je souhaite ajouter une nouvelle langue à mon application : l'espagnol.","demande_changement"),
        ("Pouvez-vous m'aider à définir une nouvelle langue pour mon projet ? J'aimerais ajouter le chinois.","demande_changement"),
        ("Est-il possible de spécifier une langue différente pour mon application ? Je voudrais ajouter l'italien.","demande_changement"),
        ("Je veux mettre à jour les langues de mon application. Pourriez-vous ajouter le russe ?", "demande_changement"),
        ("Peut-on changer la langue principale de l'application ? J'aimerais ajouter l'arabe.","demande_changement"),
        ("Je voudrais modifier les langues de mon projet. Ajoutez le portugais, s'il vous plaît.", "demande_changement"),
        ("Comment puis-je ajouter une nouvelle langue à mon application ? Je souhaite inclure le japonais.", "demande_changement"),
        ("Je souhaite supprimer la langue espagnole de mon application.", "demande_changement"),
        ("Pouvez-vous m'aider à remplacer le français par l'allemand dans mon projet ?","demande_changement"),
        ("Est-il possible de retirer l'italien de la liste des langues supportées ?", "demande_changement"),
        ("Je veux enlever le russe et le chinois des langues disponibles et ajouter le coréen.", "demande_changement"),
        ("Je souhaite changer les profils de la partie serveur de dev et test à prod et pre-prod.", "demande_changement"),
        ("Pouvez-vous m'aider à remplacer les profils de développement et de test par production et pre-production ?", "demande_changement"),
        ("Est-il possible de changer les profils de prod et pre-prod pour dev et test ?","demande_changement"),
        ("Je veux remplacer les profils de test et pre-prod par dev et prod.","demande_changement"),
        ("Peut-on changer les profils de développement et de pre-production à production et test ?","demande_changement"),
        ("Je voudrais modifier les profils de prod et test en dev et pre-prod.", "demande_changement"),
        ("Je voudrais ajouter le profil de pré-production pour la partie serveur.", "demande_changement"),
        

        #test

        

        ]  

data=data+data_fournir_infos