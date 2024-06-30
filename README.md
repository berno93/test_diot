Etapes à suivre pour éxécuter le projet :

## Prérequis

- Python 3.11.4
- Django 4.2.4

## Installation

- Clonez le repository : git clone https://github.com/berno93/test_diot
- Installer les dépendances nécessaires : pip install -r requirements.txt     

## Générer une clé API sur OPENAI

- Allez sur le site https://platform.openai.com/api-keys et crée une API Key secrete
- Allez dans le fichier settings.py et ajouter cette ligne en modifiant "votre-clé-secrete" par la clé que vous avez générer :
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'votre-clé-secrete')

## Lancer le serveur

- Activez l'environnement du projet : .\env\Scripts\activate    
- Lancer le serveur : python manage.py runserver   






