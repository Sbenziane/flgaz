- Découverte des outils - Rédigez un court texte répondant aux questions suivantes

  - Que propose le site PythonAnywhere.com ?

    PythonAnywhere est un environnement de développement intégré en ligne et un service d'hébergement Web basé sur le langage de programmation Python. Il propose de pouvoir héberger des applications web fait en python.

  - Qu'est ce que FLASK ? Quels sites connus utilisent Flask ?

    1/ Flask est un framework open-source de développement web en Python. Son but principal est d'être léger, afin de garder la souplesse de la programmation Python, associé à un système de templates. Il est distribué sous licence BSD2. Il permet de réaliser un site dans un seul fichier python. 

    2/  https://github.com/rochacbruno/flask-powered 

- Description des actions réalisées 

  - Quelles étapes avez-vous suivi ?

    J'ai téléchargé le fichier zip.

    J'ai créer un repository sur github ( https://github.com/Sbenziane/flgaz ) en y ajoutant les fichiers .

    J'ai créer un virtualenv avec python3 et flask en créant un shell pour me faciliter le démarrage du serveur.

    Je me suis connecter sur PythonAnywhere et utiliser git afin de cloner mon projet.

    J'ai installé flask et modifie le wsgi

  - Quelles difficultés avez-vous rencontrées ?

    Comprendre qu'il fallait déclarer des variables avec le nom de l'app pour flask

    A modifier le fichier wsgi

- Réflexions sur le projet 

  - Quels sont, selon vous, les aspects techniques limitants du projet FLGAZ dans l'état initial ?

    Il n'y a pas de système de rôle et de connexion donc problème de sécurité

    Le système est facilement surchargable 

    Il n'y a pas assez d'interaction, de possibilité pour naviguer sans faire retour arrière

  - Quelles sont, selon vous, les menaces auxquelles un tel projet peut être soumis ?

    A la surcharge des serveurs, surtout si il y a beaucoup d'utilisateur.

    Au tentative de piratage

    Aux problématiques légales telles que la protection des données, la responsabilité en cas de message posté jugé diffamatoire ou autre.