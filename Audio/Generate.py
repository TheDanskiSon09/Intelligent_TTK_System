import os
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Имя модели
model_name = "bond005/wav2vec2-large-ru-golos"

# Путь для сохранения модели и процессора
save_directory = "Мodel"

# Создание директории, если она не существует
os.makedirs(save_directory, exist_ok=True)

# Загрузка модели и процессора
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

# Сохранение модели и процессора локально
processor.save_pretrained(save_directory)
model.save_pretrained(save_directory)

print("Модель и процессор успешно загружены и сохранены в папке 'model'!")