from moviepy.editor import AudioFileClip, ImageClip


class Medias:
    def generate_video_from_image_audio(
        self, image_path, audio_path, output_video_path, duration=None
    ):
        audio = AudioFileClip(audio_path)
        if duration is None:
            duration = audio.duration
        video = ImageClip(image_path).set_duration(duration)
        video = video.set_audio(audio)
        video.write_videofile(output_video_path, fps=24)
