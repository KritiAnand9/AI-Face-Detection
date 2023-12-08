from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path, codec='mp3')

if __name__ == "__main__":
    video_path = "Sample Video.mp4"
    output_audio_path = "audio.mp3"

    extract_audio(video_path, output_audio_path)
