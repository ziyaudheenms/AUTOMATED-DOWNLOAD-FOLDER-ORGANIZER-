import os
import shutil





def InitialOrgainzer(DOWNLOADS_FOLDER):
    ALL_THE_AVAILABLE_FILES = os.listdir(DOWNLOADS_FOLDER)
    #All the possible categories and their associated file extensions
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
        "ARCHIVES": [".zip", ".rar", ".7z", ".tar", ".gz"],
        # Code and Scripts
        "CODE": [".py", ".js", ".html", ".css", ".c", ".cpp", ".java", ".sh"],
        # Catch-all for everything else
        "OTHERS": [""] 
    }
    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(DOWNLOADS_FOLDER , folder)

        if not os.path.exists(folder_path):
            try:
                os.mkdir(folder_path)
            except Exception as e:
                print(f"error occured while trying to create the folder {folder_path} : {e}")
                
    for file in ALL_THE_AVAILABLE_FILES:
        if not os.path.isdir(os.path.join(DOWNLOADS_FOLDER,file)):
            name_of_the_file , extension_of_the_file = os.path.splitext(file)
            for folder in FILE_CATEGORIES.keys():
                if extension_of_the_file.lower() in FILE_CATEGORIES[folder]:
                    available_files_in_this_new_folder = os.listdir(os.path.join(DOWNLOADS_FOLDER,folder))
                    if file in available_files_in_this_new_folder:
                        counter = 1
                        modified_file_name_with_number = f"{name_of_the_file}({counter}){extension_of_the_file}"
                        while modified_file_name_with_number in available_files_in_this_new_folder:
                            counter +=1
                            modified_file_name_with_number = f"{name_of_the_file}({counter}){extension_of_the_file}"
                        try:
                            shutil.move(os.path.join(DOWNLOADS_FOLDER,file) , os.path.join(DOWNLOADS_FOLDER,folder,modified_file_name_with_number))
                        except Exception as e:
                            print(f"error occured while trying to move the file {file} to the folder {folder} : {e}")
                    else:
                        try:
                            shutil.move(os.path.join(DOWNLOADS_FOLDER,file) , os.path.join(DOWNLOADS_FOLDER,folder,file))
                        except Exception as e:
                            print(f"error occured while trying to move the file {file} to the folder {folder} : {e}")
