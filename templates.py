from datetime import datetime


class Templates:
    def youtube_template(self):
        return """
Titre : {title}
Artiste : {artist}
Genre : {genre}
Date de sortie : {release_date}

Description :
{description_text}

Retrouvez-nous aussi sur Facebook : {facebook_page_url}

Merci pour votre écoute ! N'oubliez pas de liker et de vous abonner pour plus de musique !
"""

    def generate_youtube_description(
        self, title, artist, album, genre, description_text, facebook_page_url
    ):
        release_date = datetime.now().strftime("%d/%m/%Y")
        youtube_template = self.youtube_template()
        return youtube_template.format(
            title=title,
            artist=artist,
            album=album,
            genre=genre,
            release_date=release_date,
            description_text=description_text,
            facebook_page_url=facebook_page_url,
        )
