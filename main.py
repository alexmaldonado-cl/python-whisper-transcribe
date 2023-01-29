import whisper
import pytube

url_youtube = "https://www.youtube.com/watch?v=x_4k4oJPV5U"
videoYoutube = pytube.YouTube(url_youtube)

audio = videoYoutube.streams.get_audio_only()
audio.download(filename='openia-youtube.mp4')

model = whisper.load_model("small")
result = model.transcribe('openia-youtube.mp4', fp16=False)

print(result['text'])