import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from dotenv import load_dotenv

load_dotenv()


class GoogleAuth:

    def __init__(self):
        self.SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
        self.CLIENT_SECRET_FILE = os.environ.get("CLIENT_SECRET_FILE")
        self.API_SERVICE_NAME = "youtube"
        self.API_VERSION = "v3"

    def get_authenticated_service(self):
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CLIENT_SECRET_FILE, self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open("token.json", "w", encoding="utf-8") as token_file:
                token_file.write(creds.to_json())
        return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=creds)
