import os
from gtts import gTTS

class Voice:
    @staticmethod
    def speak(speechtext):
        try:
            tts = gTTS(text=speechtext, lang='en', slow=False)
            tts.save("audio.mp3")
            os.system("mpg123 audio.mp3")
        except Exception as e:
            pass