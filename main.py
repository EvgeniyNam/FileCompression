import os
import time
import zipfile


def compress_folder(folder_path, zip_name):
    # Создание zip-архива
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))


def save_compressed_folder(source_folder, destination_folder, zip_name):
    # Создание полного пути к исходной и целевой папкам
    source_path = os.path.abspath(source_folder)
    destination_path = os.path.abspath(destination_folder)

    # Проверка существования исходной папки
    if not os.path.exists(source_path):
        print(f"Исходная папка '{source_path}' не существует.")
        return

    # Проверка существования целевой папки, если ее нет, то создаем
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
        print(f"Создана целевая папка '{destination_path}'.")

    # Полный путь к сжатому файлу
    zip_path = os.path.join(destination_path, zip_name)

    # Сжатие папки
    compress_folder(source_path, zip_path)
    print(f"Папка '{source_path}' сжата и сохранена в архив '{zip_path}'.")


if __name__ == "__main__":
    source_folder = 'session-865d4476-f377-4cef-97a2-c36ae11613cf'
    destination_folder = 'zip_folders'
    zip_name = source_folder + '.zip'

    # Бесконечный цикл для выполнения операции раз в день
    while True:
        save_compressed_folder(source_folder, destination_folder, zip_name)
        # Задержка на 60 секунд
        time.sleep(60)
