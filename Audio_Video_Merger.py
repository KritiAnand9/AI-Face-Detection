from moviepy.editor import VideoFileClip, AudioFileClip
def combine_audio_video(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    video_path = "Output Video.mp4"
    audio_path = "audio.mp3"
    output_path = "output.mp4"

    combine_audio_video(video_path, audio_path, output_path)