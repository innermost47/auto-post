from datetime import datetime


class Templates:
    def youtube_template(self):
        return """
Titre : {title}
Artiste/Groupe : {artist}
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

    def facebook_template(self):
        return """
Titre : {title}
Artiste/Groupe : {artist}
Genre : {genre}
Date de sortie : {release_date}

Description :
{description_text}

Merci pour votre écoute ! N'oubliez pas de liker la publication et la page pour plus de musique !
"""

    def generate_facebook_description(
        self, title, artist, album, genre, description_text
    ):
        release_date = datetime.now().strftime("%d/%m/%Y")
        facebook_template = self.facebook_template()
        return facebook_template.format(
            title=title,
            artist=artist,
            album=album,
            genre=genre,
            release_date=release_date,
            description_text=description_text,
        )
