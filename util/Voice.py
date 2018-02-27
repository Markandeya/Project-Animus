import os
from gtts import gTTS

class Voice:
    def speak(self, speechtext):
        tts = gTTS(text=speechtext, lang='hi', slow=False)
        tts.save("audio.mp3")
        os.system("mpg123 audio.mp3")