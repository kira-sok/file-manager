import os
import shutil

extension_map = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".gif": "Images", ".bmp": "Images", ".webp": "Images",
    ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
    ".xls": "Documents", ".xlsx": "Documents", ".ppt": "Documents",
    ".pptx": "Documents", ".txt": "Documents",
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
    ".tar": "Archives", ".gz": "Archives",
    ".mp3": "Music", ".wav": "Music", ".flac": "Music",
    ".mp4": "Video", ".mov": "Video", ".avi": "Video",
    ".py": "Code", ".js": "Code", ".html": "Code"
}

uncategorized_folder = "Other"


def organize(directory: str) -> None:
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Not a directory: {directory}")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if not os.path.isfile(file_path):
            continue

        name, ext = os.path.splitext(filename)
        folder_name = extension_map.get(ext.lower(), uncategorized_folder)
        dest_dir = os.path.join(directory, folder_name)

        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(file_path, dest_dir)
        print(f"{filename} -> {folder_name}/")


def unorganize(directory: str) -> None:
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Not a directory: {directory}")

    folders = set(extension_map.values()) | {uncategorized_folder}

    for folder_name in folders:
        folder_path = os.path.join(directory, folder_name)

        if not os.path.isdir(folder_path):
            continue

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            shutil.move(file_path, directory)
            print(f"{folder_name}/{filename} -> ./")

        os.rmdir(folder_path)  # os.rmdir fails if folder is not empty - that's intentional
        print(f"Removed folder: {folder_name}/\n")


if __name__ == "__main__":
    path = os.path.join(os.path.expanduser("~"), "Downloads")
    organize(path)