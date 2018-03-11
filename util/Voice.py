import os
from gtts import gTTS

class Voice:
    @staticmethod
    def speak(speechtext):
        try:
            tts = gTTS(text=speechtext, lang='en', slow=False)
            tts.save("audio.mp3")
            os.system("mpg123 audio.mp3 2>&1 >/dev/null")
        except Exception as e:
            pass