
# Préparation des exemples d'entraînement NER
training_data = [
    # data pour l'entite "nomApplication"
    ("Programme une nouvelle application nommée XYZ", {"entities": [(42, 45, "nomApplication")]}),#*
    ("Conçois une application appelée XYZ", {"entities": [(32, 35, "nomApplication")]}),#*
    ("Mets au point une application nommée XYZ", {"entities": [(37, 40, "nomApplication")]}),#*
    ("Invente une nouvelle application appelée XYZ", {"entities": [(41, 44, "nomApplication")]}),#*
    ("Je veux créer une application nommée MyApp", {"entities": [(37, 42, "nomApplication")]}),
    ("Je souhaite développer une application portant le nom 'MyApp'.", {"entities": [(55,60, "nomApplication")]}),
    ("Crée une nouvelle application appelée XYZ", {"entities": [(38, 41, "nomApplication")]}),
    ("Réalise une application innovante appelée XYZ", {"entities": [(42, 45, "nomApplication")]}),
    ("Conceptrice une application révolutionnaire nommée XYZ", {"entities": [(51, 54, "nomApplication")]}),
    ("Fabrique une nouvelle application et donne-lui le nom de XYZ", {"entities": [(57, 60, "nomApplication")]}),
    ("Mets en place une application fraîche et moderne nommée XYZ", {"entities": [(56, 59, "nomApplication")]}),
    ("Imagines et crée une application originale baptisée XYZ", {"entities": [(52, 55, "nomApplication")]}),
    ("Élabore une application inédite connue sous le nom de XYZ", {"entities": [(54, 57, "nomApplication")]}),
    ("Pouvez-vous m'aider à mettre en place une application appelée 'MyApp' ?", {"entities": [(63,68, "nomApplication")]}),
    ("J'aimerais commencer un projet d'application nommée 'MyApp'.", {"entities": [(53,58, "nomApplication")]}),
    ("Commencez un nouveau projet avec le nom 'MyApp' pour moi, s'il vous plaît.", {"entities": [(41,46, "nomApplication")]}),
    ("Je veux entamer le développement d'une application nommée 'MyApp'.", {"entities": [(59,64, "nomApplication")]}),
    ("Pour commencer, je souhaite créer une application que je nommerai 'MyApp'.", {"entities": [(67,72, "nomApplication")]}),
    ("Créons ensemble une application et appelons-la 'MyApp'.", {"entities": [(48,53, "nomApplication")]}),
    ("Je désire lancer une application et je la baptiserai 'MonAppli'.", {"entities": [(54,62, "nomApplication")]}),
    ("Commencez la conception d'une nouvelle application que je nommerai 'ProApp'.", {"entities": [(68,74, "nomApplication")]}),
    ("Crée une application pour moi et donne-lui le nom 'SuperApp'.", {"entities": [(51,59, "nomApplication")]}),
    ("Je vais débuter un projet d'application et je souhaite l'appeler 'AppX'.", {"entities": [(66,70, "nomApplication")]}),
    ("Pour démarrer, je veux construire une application et l'intituler 'InnovaApp'.", {"entities": [(66,75, "nomApplication")]}),
    ("J'ai en tête une application, je la nommerai 'QuickStart'.", {"entities": [(46,56, "nomApplication")]}),
    ("Réalisez une nouvelle application, son nom sera 'MySoft'.", {"entities": [(49,55, "nomApplication")]}),


    # data pour l'entite "frontendWorkspace"
    ("Assure-toi que le workspace FrontProjet est configuré pour le frontend", {"entities": [(28, 39, "frontendWorkspace")]}),#*
    ("Choisis FrontProjet comme nom du workspace pour le frontend", {"entities": [(8, 19, "frontendWorkspace")]}),#*
    ("Configure FrontProjet comme l'environnement de travail pour le frontend", {"entities": [(10, 21, "frontendWorkspace")]}),#*
    ("Le nom du workspace pour la partie frontend est FrontProjet", {"entities": [(48, 59, "frontendWorkspace")]}),#*
    ("Le workspace de la partie frontend est FrontProjet", {"entities": [(39, 50, "frontendWorkspace")]}),
    ("Utilise FrontProjet comme nom de workspace pour la partie frontend", {"entities": [(8, 19, "frontendWorkspace")]}),
    ("Définis FrontProjet comme workspace principal du frontend", {"entities": [(8, 19, "frontendWorkspace")]}),
    ("Assigne FrontProjet comme workspace de travail pour la partie frontend", {"entities": [(8, 19, "frontendWorkspace")]}),
    ("Attribue FrontProjet en tant que dossier de la partie frontend", {"entities": [(9, 20, "frontendWorkspace")]}),
    ("Désigne FrontProjet comme l'espace de travail spécifique au frontend", {"entities": [(8, 19, "frontendWorkspace")]}),
    ("Indique que FrontProjet est le nom du workspace utilisé pour le frontend", {"entities": [(12, 23, "frontendWorkspace")]}),
    ("Précise que le workspace FrontProjet est destiné à la partie frontend", {"entities": [(25, 36, "frontendWorkspace")]}),
    ("Configure FrontProjet comme le workspace par défaut pour le frontend", {"entities": [(10, 21, "frontendWorkspace")]}),
    ("Choisis FrontProjet comme workspace de référence pour la partie frontend", {"entities": [(8, 19, "frontendWorkspace")]}),

    # data pour l'entite "backendWorkspace"
    ("Assure-toi que le workspace BackProjet est configuré pour le backend", {"entities": [(28, 38, "backendWorkspace")]}),#*
    ("Choisis BackProjet comme nom du workspace pour le backend", {"entities": [(8, 18, "backendWorkspace")]}),#*
    ("Configure BackProjet comme l'environnement de travail pour le backend", {"entities": [(10, 20, "backendWorkspace")]}),#*
    ("Le nom du workspace pour la partie backend est BackProjet", {"entities": [(47, 57, "backendWorkspace")]}),#*
    ("Le workspace de la partie backend est BackProjet", {"entities": [(38, 48, "backendWorkspace")]}),
    ("Utilise BackProjet comme nom de workspace pour la partie backend", {"entities": [(8, 18, "backendWorkspace")]}),
    ("Définis BackProjet comme workspace principal du backend", {"entities": [(8, 18, "backendWorkspace")]}),
    ("Assigne BackProjet comme workspace de travail pour la partie backend", {"entities": [(8, 18, "backendWorkspace")]}),
    ("Attribue BackProjet en tant que dossier de la partie backend", {"entities": [(9, 19, "backendWorkspace")]}),
    ("Désigne BackProjet comme l'espace de travail spécifique au backend", {"entities": [(8, 18, "backendWorkspace")]}),
    ("Indique que BackProjet est le nom du workspace utilisé pour le backend", {"entities": [(12, 22, "backendWorkspace")]}),
    ("Précise que le workspace BackProjet est destiné à la partie backend", {"entities": [(25, 35, "backendWorkspace")]}),
    ("Configure BackProjet comme le workspace par défaut pour le backend", {"entities": [(10, 20, "backendWorkspace")]}),
    ("Choisis BackProjet comme workspace de référence pour la partie backend", {"entities": [(8, 18, "backendWorkspace")]}),

    ("je veux que l'espace de travail pour la partie frontend soit dans le dossier TestFront et celui de la partie back dans TestBack", {"entities": [(119, 127, "backendWorkspace"),(77, 86, "frontendWorkspace")]}),
    ("Organise le workspace de la partie frontend dans le dossier TestFront, et celui de la partie back dans TestBack", {"entities": [(103, 111, "backendWorkspace"),(60, 69, "frontendWorkspace")]}),


    # data pour l'entite "langue"
    ("Développez une application qui peut être localisée en différentes langues telles que le français, l'anglais et l'arabe", {"entities": [(88,96,"langue"),(100,107,"langue"),(113,118,"langue")]}),#*
    ("Imaginez une plateforme multilingue qui permet aux utilisateurs de traduire du texte en français, anglais et arabe", {"entities": [(88,96,"langue"),(98,105,"langue"),(109,114,"langue")]}),#*
    ("Créez un outil linguistique qui offre une traduction fluide vers le français, l'anglais et l'arabe, le tout dans une seule application", {"entities": [(68,76,"langue"),(80,87,"langue"),(93,98,"langue")]}),#*
    ("Élaborez un système de traduction automatique qui peut être utilisé pour convertir des textes entre le français, l'anglais et l'arabe", {"entities": [(103,111,"langue"),(115,122,"langue"),(128,133,"langue")]}),#*
    ("Concevez une application polyglotte capable de supporter les langues françaises, anglaises et arabes pour une expérience utilisateur globale", {"entities": [(69,79,"langue"),(81,90,"langue"),(94,100,"langue")]}),
    ("Je veux créer une application qui peut être traduite en français, anglais et arabe", {"entities": [(56,64,"langue"),(66,73,"langue"),(77,82,"langue")]}),
    ("J'ai l'intention de développer une application polyglotte qui prend en charge la traduction en français, anglais et arabe", {"entities": [(95,103,"langue"),(105,112,"langue"),(116,121,"langue")]}),
    ("Mon objectif est de concevoir une application qui offre la possibilité d'être traduite en français, anglais et arabe", {"entities": [(90,98,"langue"),(100,107,"langue"),(111,116,"langue")]}),
    ("Je cherche à créer une application multilingue qui peut être rendue en français, anglais et arabe", {"entities": [(71,79,"langue"),(81,88,"langue"),(92,97,"langue")]}),
    ("L'idée est de développer une application avec une fonctionnalité de traduction en français, anglais et arabe", {"entities": [(82,90,"langue"),(92,99,"langue"),(103,108,"langue")]}),
    ("Mon projet consiste à concevoir une application qui permettra aux utilisateurs de traduire son contenu en français, anglais et arabe", {"entities": [(106,114,"langue"),(116,123,"langue"),(127,132,"langue")]}),
    ("Je souhaite créer une application offrant une traduction en français, anglais et arabe pour atteindre un public plus large", {"entities": [(60,68,"langue"),(70,77,"langue"),(81,86,"langue")]}),
    ("Mon objectif est de mettre au point une application qui supporte la traduction en français, anglais et arabe", {"entities": [(82,90,"langue"),(92,99,"langue"),(103,108,"langue")]}),
    ("Je désire développer une application qui puisse être traduite en français, anglais et arabe pour faciliter la communication entre différents utilisateurs", {"entities": [(65,73,"langue"),(75,82,"langue"),(86,91,"langue")]}),
    ("Je m'efforce de créer une application multilingue qui permettra aux utilisateurs de choisir entre le français, l'anglais et l'arabe pour son contenu", {"entities": [(101,109,"langue"),(113,120,"langue"),(126,131,"langue")]}),
    ("L'application que je veux créer doit être accessible dans trois langues : le français, l'anglais et l'arabe, grâce à une fonction de traduction intégrée", {"entities": [(77,85,"langue"),(89,96,"langue"),(102,107,"langue")]}),


    # data pour l'entite "profilsPartieServeur"
    ("Je voudrais activer les paramètres de pré-production et production pour le serveur d'application", {"entities": [(38,52,"profilsPartieServeur"),(56,66,"profilsPartieServeur")]}),
    ("Assure-toi que les profils de la partie serveur sont configurés en mode développement, pré-production et production", {"entities": [(72,85,"profilsPartieServeur"),(87,101,"profilsPartieServeur"),(105,115,"profilsPartieServeur")]}),
    ("Sélectionne les profils de la partie serveur en mode test et production pour l'exécution des tâches", {"entities": [(53,57,"profilsPartieServeur"),(61,71,"profilsPartieServeur")]}),
    ("Configure les profils de la partie serveur en mode dev et test", {"entities": [(51,54,"profilsPartieServeur"),(58,62,"profilsPartieServeur")]}),
    ("Vérifie les paramètres des profils de la partie serveur : pre-prod et prod", {"entities": [(58,66,"profilsPartieServeur"),(70,74,"profilsPartieServeur")]}),
    ("Déploie l'application sur le profil de la partie serveur en mode production", {"entities": [(65,75,"profilsPartieServeur")]}),
    ("Configure les profils de la partie serveur en mode développement et test", {"entities": [(51,64,"profilsPartieServeur"),(68,72,"profilsPartieServeur")]}),
    ("Utilise les profils de pré-production et production pour la partie serveur", {"entities": [(23,37,"profilsPartieServeur"),(41,51,"profilsPartieServeur")]}),
    ("Active les profils de développement, test et production pour la partie serveur", {"entities": [(22,35,"profilsPartieServeur"),(37,41,"profilsPartieServeur"),(45,55,"profilsPartieServeur")]}),
    ("Sélectionne les profils de la partie serveur en mode pre-prod et prod pour l'exécution des tâches", {"entities": [(53,61,"profilsPartieServeur"),(65,69,"profilsPartieServeur")]}),
    ("Est-ce que je peux utiliser plusieurs profils pour la partie serveur ? J'aimerais utiliser les profils de développement, pré-production et prod en même temps", {"entities": [(106,119,"profilsPartieServeur"),(121,135,"profilsPartieServeur"),(139,143,"profilsPartieServeur")]}),
    ("Pouvez-vous activer les profils de développement, test et production pour la partie serveur ?", {"entities": [(35,48,"profilsPartieServeur"),(50,54,"profilsPartieServeur"),(58,68,"profilsPartieServeur")]}),
    ("Je souhaite configurer les profils pour le serveur backend en mode développement et test", {"entities": [(67,80,"profilsPartieServeur"),(84,88,"profilsPartieServeur")]}),
    ("Je veux définir les profils pour la partie back-end de l'application en mode test et pré-production", {"entities": [(77,81,"profilsPartieServeur"),(85,99,"profilsPartieServeur")]}),
    ("Je veux définir les différentes alternatives de test et pré-production pour la partie serveur", {"entities": [(48,52,"profilsPartieServeur"),(56,70,"profilsPartieServeur")]}),
    
    # data pour l'entite "microservices"  
    ("Je souhaite ajouter le microservice Eureka à mon architecture", {"entities": [(36,42,"microservices")]}),
    ("Je souhaite intégrer les microservices GED, Reporting et GestionProfil dans mon profil de pré-production", {"entities": [(39,42,"microservices"),(44,53,"microservices"),(57,70,"microservices")]}),
    ("Je suis intéressé par l'ajout du microservice Gateway à mon profil de test", {"entities": [(46,53,"microservices")]}),
    ("Incluez le microservice Gateway dans la configuration", {"entities": [(24,31,"microservices")]}),
    ("Est-il possible d'inclure le microservice gateway dans mon architecture ? ", {"entities": [(42,49,"microservices")]}),
    ("J'ai besoin du microservice Administration pour gérer mon application", {"entities": [(28,42,"microservices")]}),
    ("Je veux intégrer les microservices GED et Reporting à mon application", {"entities": [(35,38,"microservices"),(42,51,"microservices")]}),
    ("Ajoutez le microservice Administration à la partie serveur", {"entities": [(24,38,"microservices")]}),
    ("Intégrez les microservices personnalisés que j'ai développés : GestionUtilisateurs et GestionProduits", {"entities": [(63,82,"microservices"),(86,101,"microservices")]}),
 
    ("Définit le dossier TestFront comme répertoire du workspace de la partie frontend, et TestBack comme répertoire du workspace de la partie back", {"entities": [(85,93,"backendWorkspace"),(19,28,"frontendWorkspace")]}),
    ("Indique que le workspace de la partie frontend doit être situé dans le dossier TestFront, et que celui de la partie back doit être situé dans TestBack", {"entities": [(79,88,"frontendWorkspace"),(142,150,"backendWorkspace")]}),
    ("Établis que le dossier TestFront sera utilisé comme emplacement du workspace associé à la partie frontend, et que le dossier TestBack sera utilisé comme emplacement du workspace associé à la partie back", {"entities": [(23,32,"frontendWorkspace"),(125,133,"backendWorkspace")]}),


    # # data pour l'entite "aide"  
    # ("Je suis un peu perdu, pouvez-vous m'aider avec ce formulaire ?", {"entities": [(36,41,"aide"),(8,20,"aide")]}),
    # ("J'ai besoin d'assistance pour remplir ce formulaire, pouvez-vous me guider ?", {"entities": [(14,24,"aide")]}),
    # ("Pouvez-vous m'expliquer comment remplir cette partie du formulaire ?", {"entities": [(0,23,"aide")]}),
    # ("Je ne suis pas sûr(e) de ce qu'il faut faire ici, pouvez-vous me donner des instructions ?", {"entities": [(50,88,"aide")]}),
    # ("Aidez-moi à comprendre les informations requises pour cette étape du formulaire", {"entities": [(0,5,"aide")]}),
    # ("Je ne sais pas comment fournir les détails demandés, pouvez-vous m'orienter ?", {"entities": [(53,77,"aide")]}),
    # ("Je suis bloqué. Pouvez-vous m'expliquer ce que je dois faire ?", {"entities": [(8,14,"aide")]}),
    # ("Besoin d'aide pour ajouter des microservices. Comment procéder ?", {"entities": [(46,64,"aide")]}),


    ("Je souhaite vous informer que je vais créer une application nommée 'SIMep' avec un frontend appelé 'front-workspace' et un backend nommé 'workspace du backend'.", {"entities": [(68,73,"nomApplication"),(100,115,"frontendWorkspace"),(138,158,"backendWorkspace")]}),
    ("J'ai quelques détails à vous donner concernant mon projet. Je vais développer une application appelée 'MonProjet' avec un frontend nommé 'FrontEndXYZ' et un backend appelé 'BackEnd123'.", {"entities": [(103,112,"nomApplication"),(138,149,"frontendWorkspace"),(173,183,"backendWorkspace")]}),
    ("Voici les informations dont vous avez besoin : Je vais créer une application 'MyApp' avec un frontend nommé 'FrontEnd1' et un backend nommé 'BackEndA'", {"entities": [(78,83,"nomApplication"),(109,118,"frontendWorkspace"),(141,149,"backendWorkspace")]}),
    ("Pour mon projet, j'ai l'intention de développer une application 'SuperApp' avec un frontend 'WebFront' et un backend 'ServerBack'.", {"entities": [(65,73,"nomApplication"),(93,101,"frontendWorkspace"),(118,128,"backendWorkspace")]}),
    ("Je veux fournir des informations pour mon projet en cours. L'application s'appelle 'AppXYZ' avec un frontend 'WebApp' et un backend 'AppServer'.", {"entities": [(84,90,"nomApplication"),(110,116,"frontendWorkspace"),(133,142,"backendWorkspace")]}),
    ("Je vais démarrer un nouveau projet et voici les détails : l'application sera 'NewApp', le frontend 'WebUI', et le backend 'ServerXYZ'.", {"entities": [(78,84,"nomApplication"),(100,105,"frontendWorkspace"),(123,132,"backendWorkspace")]}),
    ("Je veux vous fournir des informations sur mon projet. L'application s'appelle 'MyApp', le frontend 'FrontEnd1', le backend 'BackEndA', et elle sera développée en utilisant les langues 'Français' et 'Anglais'.", {"entities": [(79,84,"nomApplication"),(100,109,"frontendWorkspace"),(124,132,"backendWorkspace"),(185,193,"langue"),(199,206,"langue")]}),
    ("J'aimerais vous donner des détails sur mon projet. L'application s'appelle 'ProjetABC' avec un frontend 'FrontWeb' et un backend 'BackEndServer'. Les langues supportées sont 'Espagnol' et 'Allemand'.", {"entities": [(76,85,"nomApplication"),(105,113,"frontendWorkspace"),(130,143,"backendWorkspace"),(175,183,"langue"),(189,197,"langue")]}),
    ("Pour mon projet, voici les informations essentielles : nom de l'application 'CoolApp', frontend 'WebUI', backend 'Server123', et les langues 'Portugais' et 'Chinois' sont prises en charge.", {"entities": [(77,84,"nomApplication"),(97,102,"frontendWorkspace"),(114,123,"backendWorkspace"),(142,151,"langue"),(157,164,"langue")]}),
    ("Je prévois de développer une nouvelle application, NewCoolApp, avec un frontend WebFrontend et un backend ServerBackend. Les langues utilisées seront Italien et Néerlandais.", {"entities": [(51,61,"nomApplication"),(80,91,"frontendWorkspace"),(106,119,"backendWorkspace"),(150,157,"langue"),(161,172,"langue")]}),
    ("Je vais créer une application nommée AppX avec un frontend UIWeb et un backend ServerApp. Pour les langues, nous aurons Japonais et Coréen.", {"entities": [(37,41,"nomApplication"),(59,64,"frontendWorkspace"),(79,88,"backendWorkspace"),(120,128,"langue"),(132,138,"langue")]}),
    ("L'application que je veux développer se nomme SuperApp, elle aura un frontend nommé WebUI et un backend ServerApp.", {"entities": [(46,54,"nomApplication"),(84,89,"frontendWorkspace"),(104,113,"backendWorkspace")]}),
    ("Mon projet concerne une application intitulée AppTech. Le frontend sera TechFrontend et le backend TechBackend.", {"entities": [(46,53,"nomApplication"),(72,84,"frontendWorkspace"),(99,110,"backendWorkspace")]}),
    ("Pour démarrer, je vais travailler sur une application que je nommerai MyMobileApp. Le frontend sera MobileUI et le backend MobileServer.", {"entities": [(70,81,"nomApplication"),(100,108,"frontendWorkspace"),(123,135,"backendWorkspace")]}),
    ("Je vais vous donner des informations sur mon projet. L'application s'appelle NextGenApp, le frontend est NextGenUI et le backend NextGenServer.", {"entities": [(77,87,"nomApplication"),(105,114,"frontendWorkspace"),(129,142,"backendWorkspace")]}),
    ("J'aimerais discuter de mon projet d'application. Elle se nomme AppX1, le frontend UIX1, et le backend ServerX1.", {"entities": [(63,68,"nomApplication"),(82,86,"frontendWorkspace"),(102,110,"backendWorkspace")]}),
   # ("Je suis en train de concevoir une application appelée MyServiceApp. Elle aura deux microservices : ServiceA et ServiceB. Pour la partie serveur, nous utiliserons le profil de développement.", {"entities": [(54,66,"nomApplication"),(99,107,"microservices"),(111,119,"microservices"),(175,188,"profilsPartieServeur")]}),
    ("Mon projet concerne la création de l'application XYZApp. Nous aurons trois microservices : Micro1, Micro2 et Micro3. Pour la partie serveur, nous choisissons le profil de production.", {"entities": [(49,55,"nomApplication"),(91,97,"microservices"),(99,105,"microservices"),(109,115,"microservices"),(171,181,"profilsPartieServeur")]}),
    ("Pour mon application FutureApp, nous avons prévu d'utiliser trois microservices : MicroFront, MicroAPI et MicroDB. En ce qui concerne la partie serveur, nous optons pour le profil de pré-production.", {"entities": [(21,30,"nomApplication"),(82,92,"microservices"),(94,102,"microservices"),(106,113,"microservices"),(183,197,"profilsPartieServeur")]}),
    ("Je prévois de développer une application nommée SmartApp. Nous utiliserons deux microservices : MicroUI et MicroServer. Pour la partie serveur, nous sélectionnons le profil de test.", {"entities": [(48,56,"nomApplication"),(96,103,"microservices"),(107,118,"microservices"),(176,180,"profilsPartieServeur")]}),
    #("L'application que je suis en train de concevoir s'appelle MyAppX. Elle comprendra quatre microservices : Service1, Service2, Service3 et Service4. Pour la partie serveur, nous avons besoin du profil de développement.", {"entities": [(58,64,"nomApplication"),(105,113,"microservices"),(115,123,"microservices"),(125,133,"microservices"),(137,145,"microservices"),(202,215,"profilsPartieServeur")]})


    ("Je prévois de mettre en place une application SIMep. Le nom du frontend sera Front-Workspace, et le backend sera configuré dans l'espace de travail du backend.", {"entities": [(46,51,"nomApplication"),(77,92,"frontendWorkspace"),(151,158,"backendWorkspace")]}),
    ("J'aimerais discuter de la création d'une application SIMep. Le frontend sera nommé Frontend Workspace, et pour le backend, nous utiliserons Workspace du Backend.", {"entities": [(53,58,"nomApplication"),(83,101,"frontendWorkspace"),(140,160,"backendWorkspace")]}),
    ("Mon projet consiste à élaborer une application SIMep. Je compte appeler le frontend Front Workspace et configurer le backend dans Workspace du Backend.", {"entities": [(47,52,"nomApplication"),(84,99,"frontendWorkspace"),(130,150,"backendWorkspace")]}),
    ("J'ai l'intention de développer une application SIMep. Le nom du frontend sera Front-Workspace, et le backend sera basé sur Workspace du Backend.", {"entities": [(47,52,"nomApplication"),(78,93,"frontendWorkspace"),(123,143,"backendWorkspace")]}),
    ("Je souhaite créer une application SIMep avec le frontend Front-Workspace et le backend configuré dans l'espace de travail du backend.", {"entities": [(34,39,"nomApplication"),(57,72,"frontendWorkspace"),(125,132,"backendWorkspace")]}),
    ("Je prépare un nouveau projet pour l'application SIMepX. Le nom de l'application sera SIMepX, avec un frontend appelé Front-Workspace et un backend configuré dans l'espace de travail de production. Nous utiliserons des microservices de type 'prod' pour cette application.", {"entities": [(85,91,"nomApplication"),(48,54,"nomApplication"),(117,132,"frontendWorkspace"),(185,195,"backendWorkspace"),(241,245,"profilsPartieServeur")]}),
    ("J'ai l'intention de créer une application nommée MyApp2. Pour le frontend, nous opterons pour Front-Workspace, tandis que le backend sera géré dans l'espace de travail de développement. Nous envisageons d'utiliser des microservices de type 'dev' pour cette application.", {"entities": [(49,55,"nomApplication"),(94,109,"frontendWorkspace"),(171,184,"backendWorkspace"),(241,244,"profilsPartieServeur")]}),
    ("Mon objectif est de développer une nouvelle application, AppXYZ. Le frontend, appelé Frontend-Workspace, et le backend dans l'espace de travail du backend. Nous aurons également des microservices de type 'pre-prod' et 'test' pour cette application.", {"entities": [(57,63,"nomApplication"),(85,103,"frontendWorkspace"),(147,154,"backendWorkspace"),(205,213,"profilsPartieServeur"),(219,223,"profilsPartieServeur")]}),
    ("Je veux créer une application nommée MyApp avec le microservice Eureka pour la gestion des services et le microservice Gateway pour la gestion des API. Les profils de la partie serveur incluront Dev et Prod.", {"entities": [(37,42,"nomApplication"),(64,70,"microservices"),(119,126,"microservices"),(195,198,"profilsPartieServeur"),(202,206,"profilsPartieServeur")]}),
    ("J'envisage de lancer un projet d'application baptisé XYZ-App, qui comprendra les microservices Eureka et Gateway. Les profils de la partie serveur seront Dev et Test.", {"entities": [(53,60,"nomApplication"),(95,101,"microservices"),(105,112,"microservices"),(154,157,"profilsPartieServeur"),(161,165,"profilsPartieServeur")]}),
    ("Mon idée est de développer une application révolutionnaire appelée ABC-App. Pour le front-end, nous choisirons Frontend-Workspace, et pour le backend, Back-Workspace. Nous aurons également besoin de configurer les microservices Eureka et Gateway, avec les profils de la partie serveur Dev et Pre-Prod.", {"entities": [(67,74,"nomApplication"),(111,129,"frontendWorkspace"),(151,165,"backendWorkspace"),(228,234,"microservices"),(238,245,"microservices"),(285,288,"profilsPartieServeur"),(292,300,"profilsPartieServeur")]}),
    ("Je veux discuter de la création d'une application innovante, que nous appellerons MyApp-Plus. Le microservice Eureka sera responsable de la gestion des services, tandis que le microservice Gateway gérera les API. Les profils de la partie serveur seront Dev et Test.", {"entities": [(82,92,"nomApplication"),(110,116,"microservices"),(189,196,"microservices"),(253,256,"profilsPartieServeur"),(260,264,"profilsPartieServeur")]}),
    ("Mon objectif est de mettre en place une application de pointe, que nous nommerons SuperApp. Les microservices Eureka et Gateway seront au cœur de cette application. Les profils de la partie serveur incluront Test et Pre-Prod.", {"entities": [(82,90,"nomApplication"),(110,116,"microservices"),(120,127,"microservices"),(208,212,"profilsPartieServeur"),(216,224,"profilsPartieServeur")]})


]



# Des exemples pour le test du modele
test_data  = [
   
]