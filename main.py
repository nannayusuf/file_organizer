import os
import shutil

def organize_downloads():
    folder_path = os.path.expanduser("~/Downloads")

    destination_folders = {
        ".pdf": "PDFs",
        ".txt": "Texts"
    }

    for folder_name in destination_folders.values():
        dest_path = os.path.join(folder_path, folder_name)
        os.makedirs(dest_path, exist_ok=True)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file_name)

            if extension in destination_folders:
                dest_folder = destination_folders[extension]
                dest_path = os.path.join(folder_path, dest_folder, file_name)
                shutil.move(file_path, dest_path)
                print(f"Moved: {file_name} → {dest_folder}")

if __name__ == "__main__":
    organize_downloads()
    print("Download folder organized successfully.")
    
# This script organizes files in the Downloads folder by moving them into subfolders based on their file extensions.