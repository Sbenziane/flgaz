# FLGAZ
fait par BENZIANE Sofiane & SAGUERRE Vibita

Service en ligne : http://sofiane77.eu.pythonanywhere.com/
Projet permettant d'envoyer des messages et de les afficher sur une interface hébergé sur eu.pythonanywhere.com

## Prérequis
Vous aurez besoin d'installer ce qui est indiqué ci-dessus pour pouvoir gérer le projet.
  - Python : https://www.python.org/downloads/
  - Pip : permettant d'installer les packages python sur lesquels vous voulez travailler
  - Flask : micro-frameword utilisé pour créer le projet

### Installation

Placer vous dans votre projet via votre terminal
Conseil : gérer votre projet sur un environnement virtuel pour ne pas à avoir à mettre à jour pour chaque utilisation les versions du langages / des packages utilisés :
```
virtualenv venv
venv/bin/activate
(venv) $ pip install -r requirements.txt
```
*venv* étant le nom de votre environnement virtuel

Ensuite, vous aurez beoin d'installer le micro-framework

```
pip install flask
```

Pour la base de donnée nous avons 'essayer d'utiliser SQLAlchemy
```
pip install sqlalchemy
```

## Hébergement

Le service est hébergé sur [pythonanywhere](https://eu.pythonanywhere.com/)

## Ce que fait le projet

/ : Racine <br />
&nbsp;&nbsp;|_ /gaz : formulaire d'entrée avec pseudo & message<br />
&nbsp;&nbsp;|_ /timeline : affichage des messages insérés<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|_ /timeline/[nom de l'utilisateur] : affichage des messages d'un utlisateur précis

###### Parties en cours
- Base de données : mis en place en utilsant [SQLAlchemy](https://docs.sqlalchemy.org/en/13/dialects/mysql.html)
- Limiter les doublons de message

## License

[MIT](https://choosealicense.com/licenses/mit/)