import argparse
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

from facebook import Facebook
from google_auth import GoogleAuth
from medias import Medias
from templates import Templates
from youtube import Youtube

load_dotenv()

parser = argparse.ArgumentParser(
    description="Uploader une vidéo sur YouTube avec planification"
)
parser.add_argument("--title", required=True, help="Titre de la vidéo")
parser.add_argument("--artist", required=True, help="Nom de l'artiste")
parser.add_argument("--album", required=True, help="Nom de l'album")
parser.add_argument("--genre", required=True, help="Genre musical")
parser.add_argument(
    "--description_text", required=True, help="Description de la musique"
)
parser.add_argument(
    "--facebook_page_url", required=True, help="URL de la page Facebook"
)
parser.add_argument("--image", required=True, help="Chemin de l'image")
parser.add_argument("--audio", required=True, help="Chemin du fichier MP3")
parser.add_argument("--output_video", required=True, help="Chemin de la vidéo générée")
parser.add_argument(
    "--schedule_in_minutes", type=int, help="Temps en minutes avant la publication"
)

args = parser.parse_args()


class App:
    def __init__(self):
        self.google_auth = GoogleAuth()
        self.youtube = Youtube()
        self.templates = Templates()
        self.medias = Medias()
        self.facebook = Facebook()

    def upload_video_to_youtube(
        self,
        video_file,
        title,
        artist,
        album,
        genre,
        description_text,
        facebook_page_url,
        schedule_datetime=None,
    ):
        youtube = self.google_auth.get_authenticated_service()
        video_description = self.templates.generate_youtube_description(
            title,
            artist,
            album,
            genre,
            description_text,
            facebook_page_url,
        )
        privacy_status = "private" if schedule_datetime else "public"
        status_body = {
            "privacyStatus": privacy_status,
        }
        if schedule_datetime:
            status_body["publishAt"] = schedule_datetime.isoformat() + "Z"

        video_url = self.youtube.upload_video(
            youtube, video_file, title, video_description, status_body
        )
        return video_url

    def upload(self, arguments):
        self.medias.generate_video_from_image_audio(
            self, arguments.image, arguments.audio, arguments.output_video
        )
        schedule_datetime = (
            datetime.now() + timedelta(minutes=args.schedule_in_minutes)
            if args.schedule_in_minutes
            else None
        )
        return self.upload_video_to_youtube(
            arguments.output_video,
            arguments.title,
            arguments.artist,
            arguments.album,
            arguments.genre,
            arguments.description_text,
            arguments.facebook_page_url,
            schedule_datetime,
        )

    def main(self, arguments):
        video_url = self.upload(arguments)
        message = self.templates.generate_facebook_description(
            arguments.title,
            arguments.artist,
            arguments.album,
            arguments.genre,
            arguments.description_text,
        )
        self.facebook.post_video_link(
            video_url,
            message,
            os.environ.get("PAGE_ACCESS_TOKEN"),
            os.environ.get("PAGE_ID"),
        )


if __name__ == "__main__":
    app = App()
    app.main(args)
