from genericpath import isdir
import os
import shutil
import time
from watchdog.events import DirCreatedEvent, FileCreatedEvent, FileSystemEventHandler
from watchdog.observers import Observer
from initializer import InitialOrgainzer





def organize_the_file(filename):
    print(f"Organizing the file: {filename}")
    DOWNLOADS_FOLDER = 'C:\\Users\\HP\\Downloads'
    FILE_CATEGORIES = {
        # Documents and Spreadsheets
        "DOCUMENTS": [".pdf", ".docx", ".txt", ".xlsx", ".ppt", ".pptx", ".odt", ".rtf"],
        "DATA_FILES": [".csv", ".json", ".xml", ".db", ".sql"],
        # Executables and Software
        "PROGRAMS": [".exe", ".msi", ".dmg", ".apk", ".bat"],
        # Media
        "IMAGES": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico"],
        "VIDEOS": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".webm"],
        "AUDIO": [".mp3", ".wav", ".flac", ".aac"],
        # Compressed Files
        "ARCHIVES": [".zip", ".rar", ".7z", ".tar", ".gz" , ".tmp"],
        # Code and Scripts
        "CODE": [".py", ".js", ".html", ".css", ".c", ".cpp", ".java", ".sh"],
        # Catch-all for everything else
        "OTHERS": [""] 
    }

    if os.path.isdir(os.path.join(DOWNLOADS_FOLDER,filename)) and os.path.split(filename)[-1] not in FILE_CATEGORIES["ARCHIVES"]:
        print("blocked")
        return
    print("passed")
    name_of_the_file , extension_of_the_file = os.path.splitext(filename)
    print(name_of_the_file ,extension_of_the_file)
    for folder in FILE_CATEGORIES.keys():
        if extension_of_the_file.lower() in FILE_CATEGORIES[folder]:
            available_files_in_this_new_folder = os.listdir(os.path.join(DOWNLOADS_FOLDER,folder))
            if filename in available_files_in_this_new_folder:
                counter = 1
                modified_file_name_with_number = f"{name_of_the_file}({counter}){extension_of_the_file}"
                while modified_file_name_with_number in available_files_in_this_new_folder:
                    counter +=1
                    modified_file_name_with_number = f"{name_of_the_file}({counter}){extension_of_the_file}"
                try:
                    print('passed 1')
                    shutil.move(os.path.join(DOWNLOADS_FOLDER,filename) , os.path.join(DOWNLOADS_FOLDER,folder,modified_file_name_with_number))
                except Exception as e:
                    print(f"error occured while trying to move the file {filename} to the folder {folder} : {e}")
            else:
                print("passed 2")
                try:
                    shutil.move(os.path.join(DOWNLOADS_FOLDER,filename) , os.path.join(DOWNLOADS_FOLDER,folder,filename))
                    print(f"Moved file {filename} to folder {folder}")
                except Exception as e:
                    print(f"error occured while trying to move the file {filename} to the folder {folder} : {e}")

class DownloadsFolderHandler(FileSystemEventHandler):
    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
       
        filename = os.path.basename(event.src_path)
        print(f"New file detected: {filename}")
        if filename.endswith(('.tmp', '.crdownload', '.part', '.download')):
            print(f"Skipping temporary file: {filename}")
            return
        time.sleep(1)
        organize_the_file(filename)


if __name__ == "__main__":
    print("Starting the watchdog server")
    DOWNLOADS_FOLDER = input("Enter the path of your downloads folder (or press Enter to use the default path 'C:\\Users\\HP\\Downloads'): ") or 'C:\\Users\\HP\\Downloads'
    print("Calling the initial organizer")
    InitialOrgainzer(DOWNLOADS_FOLDER)
    print("completed the initial organization")
    event_handler = DownloadsFolderHandler()
    observer = Observer()
    observer.schedule(event_handler,DOWNLOADS_FOLDER,recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Stopped the watchdog server")
