# AutoPost - Application de Publication Automatisée sur YouTube et Facebook

**AutoPost** est un outil en ligne de commande permettant de générer automatiquement une vidéo à partir d'une image et d'un fichier audio, de la publier sur YouTube avec une planification optionnelle, puis de partager automatiquement le lien de la vidéo sur une page Facebook.

## Fonctionnalités

- **Génération de vidéo** : Convertit une image et un fichier MP3 en une vidéo MP4.
- **Publication sur YouTube** : Publie la vidéo sur YouTube, avec une option de planification pour une date et une heure spécifiques.
- **Partage sur Facebook** : Partage automatiquement le lien YouTube de la vidéo sur une page Facebook.

## Prérequis

- Python 3.6 ou supérieur
- Les bibliothèques Python suivantes :
  - `argparse`
  - `datetime`
  - `os`
  - `python-dotenv`
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `google-api-python-client`
  - `requests`

## Installation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/votre_nom_d_utilisateur/AutoPost.git
   cd AutoPost
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Créez un fichier `.env` pour stocker vos variables d’environnement :
   ```
   PAGE_ACCESS_TOKEN=your_facebook_page_access_token
   PAGE_ID=your_facebook_page_id
   ```

## Configuration

- **YouTube** : Configurez les identifiants OAuth 2.0 dans Google Cloud Console et téléchargez le fichier `client_secret.json` dans le dossier de l’application.
- **Facebook** : Générez un token d’accès à la page Facebook avec les permissions `pages_manage_posts` et `pages_read_engagement`.

## Utilisation

Lancez l'application depuis la ligne de commande avec les arguments requis :

```bash
python main.py --title "Titre de la vidéo" --artist "Nom de l'artiste" --album "Nom de l'album" --genre "Genre musical" --description_text "Description de la musique" --facebook_page_url "URL de la page Facebook" --image "Chemin de l'image" --audio "Chemin du fichier MP3" --output_video "Chemin de la vidéo générée" --schedule_in_minutes 60
```

### Arguments

- `--title` : Titre de la vidéo.
- `--artist` : Nom de l’artiste.
- `--album` : Nom de l’album.
- `--genre` : Genre musical.
- `--description_text` : Description de la musique.
- `--facebook_page_url` : URL de la page Facebook où partager la vidéo.
- `--image` : Chemin vers l’image qui sera utilisée dans la vidéo.
- `--audio` : Chemin vers le fichier MP3 de la musique.
- `--output_video` : Chemin où la vidéo générée sera enregistrée.
- `--schedule_in_minutes` (optionnel) : Temps en minutes avant la publication de la vidéo sur YouTube. Par défaut, la vidéo est publiée immédiatement.

## Exemple

```bash
python main.py --title "Mon Titre" --artist "Mon Artiste" --album "Mon Album" --genre "Rock" --description_text "Une nouvelle musique inspirée de grands espaces" --facebook_page_url "https://www.facebook.com/YourPage" --image "cover.jpg" --audio "track.mp3" --output_video "output.mp4" --schedule_in_minutes 120
```

Dans cet exemple, la vidéo sera publiée sur YouTube dans 2 heures (120 minutes) et le lien sera automatiquement partagé sur la page Facebook spécifiée.

## Structure du Code

- **App** : La classe principale qui gère l'authentification, la génération de vidéos, et les publications sur YouTube et Facebook.
- **upload_video_to_youtube** : Méthode qui gère la génération de la description et la planification de la publication YouTube.
- **main** : Méthode qui orchestre le flux complet, de la création de la vidéo à la publication sur YouTube et le partage sur Facebook.

## Avertissements

Cette application utilise des tokens d'accès pour publier sur Facebook. Assurez-vous de sécuriser vos tokens et de respecter les conditions d’utilisation de Facebook et YouTube.

## Licence

Ce projet est sous licence MIT.
