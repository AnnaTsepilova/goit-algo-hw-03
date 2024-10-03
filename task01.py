import shutil
import argparse
from pathlib import Path

def copy_and_sort_files(src_dir: Path, dest_dir: Path):
    try:
        # Перебір елементів у вихідній директорії
        for item in src_dir.iterdir():
            # Якщо елемент є директорією, викликаємо функцію рекурсивно
            if item.is_dir():
                copy_and_sort_files(item, dest_dir)
            else:
                # Якщо елемент є файлом, визначаємо його розширення
                file_extension = item.suffix[1:]  # Отримуємо розширення файлу без крапки
                if not file_extension:
                    file_extension = 'no_extension'  # Якщо немає розширення, поміщаємо у відповідну папку

                # Створюємо нову директорію на основі розширення файлу
                dest_folder = dest_dir / file_extension
                dest_folder.mkdir(parents=True, exist_ok=True)

                # Копіюємо файл у відповідну піддиректорію
                dest_file_path = dest_folder / item.name
                shutil.copy2(item, dest_file_path)
                print(f"Файл '{item}' скопійовано в '{dest_file_path}'")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Копіювання і сортування файлів за розширенням")
    parser.add_argument("src_dir", type=Path, help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", type=Path, nargs='?', default=Path("dist"), help="Шлях до директорії призначення (за замовчуванням 'dist')")
    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir
        
    # Перевіряємо, чи існує вихідна директорія
    if not src_dir.exists():
        print(f"Директорія '{src_dir}' не існує.")
        return

    # Створюємо директорію призначення, якщо її немає
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Викликаємо функцію для копіювання і сортування файлів
    copy_and_sort_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()
