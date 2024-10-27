import os
import numpy as np
import torch
import librosa
import subprocess
import tempfile
import threading
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Загрузка модели и процессора
model_name = "C:/Users/New/PycharmProjects/pythonProject/Audio/Мodel"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

def GetAudio(voice):
    # Создание временного файла для хранения OGG
    with tempfile.NamedTemporaryFile(suffix='.ogg', delete=False) as ogg_file:
        ogg_file.write(voice)
        ogg_file_path = ogg_file.name

    # Создание временного файла для хранения WAV
    wav_file_path = tempfile.mktemp(suffix='.wav')

    # Преобразование OGG в WAV
    os.system(f'ffmpeg -i {ogg_file_path} {wav_file_path}')
    print("Преобразование завершено.")

    # Проверка существования файла
    if not os.path.exists(wav_file_path):
        print("Файл audio.wav не найден!")
        return

    # Распознавание речи
    speech_array, sampling_rate = librosa.load(wav_file_path, sr=16_000)
    inputs = processor(speech_array, sampling_rate=sampling_rate, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    predicted_sentence = processor.batch_decode(predicted_ids)[0]

    # Удаление временных файлов
    os.remove(ogg_file_path)
    os.remove(wav_file_path)

    return predicted_sentence



