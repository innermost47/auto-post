import requests


class Facebook:

    def post_video_link(self, video_url, message, page_access_token, page_id):
        url = f"https://graph.facebook.com/{page_id}/feed"
        payload = {
            "message": message,
            "link": video_url,
            "access_token": page_access_token,
        }
        response = requests.post(url, data=payload, timeout=60)
        if response.status_code == 200:
            print("La vidéo a été partagée avec succès sur la page Facebook !")
        else:
            print(
                "Erreur lors du partage de la vidéo sur la page Facebook :",
                response.json(),
            )
