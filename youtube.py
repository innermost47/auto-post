from googleapiclient.http import MediaFileUpload


class Youtube:
    def __init__(self):
        pass

    def upload_video(
        self,
        youtube,
        video_file,
        title,
        description,
        status_body=None,
    ):
        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                    "categoryId": "22",
                },
                "status": status_body,
            },
            media_body=MediaFileUpload(video_file, chunksize=-1, resumable=True),
        )
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"Upload progress: {int(status.progress() * 100)}%")

        print("Upload complete!")
        video_id = response.get("id")
        return f"https://www.youtube.com/watch?v={video_id}"
