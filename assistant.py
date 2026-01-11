import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import commands

# Загрузка моделі
model = Model("models/vosk-model")
rec = KaldiRecognizer(model, 16000)

# Завантаження налаштувань
with open("config.json") as f:
    config = json.load(f)
WAKE_WORD = config.get("wake_word", "wasup")



