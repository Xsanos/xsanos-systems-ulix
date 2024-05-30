#  _______________________________________
# |        Xsanos Systems Studio®         |
# |_______________________________________|

# This is part of the Ulix
# This module contains all system functions

import os
import time
import stat
import datetime
import subprocess
import PathConfig
import Config


"""
kolejność  funkcji expect error jest ważna, bo "code is unrichable"
returny zwraca text do konsoli
bez except VE python zatrzymuje kod!!!!!
(CHYBA)
"""
"-------------------------------------------------------------------------------------Boot"
def boot_console(): # tylko dla console
    i = 0
    while i < 20:
        print('=', end=' ', flush=True)  # flush=True ensures that the dot is immediately printed
        time.sleep(0.1)  
        i += 1
    os.system('cls')
    print(5*"-----"+"--------"+5*"-----")
    print(5*"     "+"  ULIX  "+5*"     ")
    print(5*"-----"+"--------"+5*"-----")
    time.sleep(1) 
    os.system('cls')    
    print(5*"-----"+"--------"+5*"-----")
    print(5*"     "+"Welcome!"+5*"     ")
    print(5*"-----"+"--------"+5*"-----")
    time.sleep(1) 
    os.system('cls')

"-------------------------------------------------------------------------------------Foldery"
def mkdir(folder_name=None):
    try: 
        if folder_name is None or not folder_name.strip(): # Sprawdź, czy folder_name zostało podane  
            raise ValueError("Folder name not provided")

        if os.path.isabs(folder_name): # Sprawdź, czy folder_name jest pełną ścieżką (absolute path)
            new_directory = folder_name
        else:
            new_directory = os.path.join(os.getcwd(), folder_name) # Łączy ściężkę i nazwę pliku

        os.makedirs(new_directory) # makedirs tworzy nową ścieżkę (folder)
        print(f"Directory '{new_directory}' created successfully.")
        return (f"Directory '{new_directory}' created successfully.")
    
    except FileExistsError:
        print(f"Directory '{new_directory}' already exists.")
        return (f"Directory '{new_directory}' already exists.")
    
    except ValueError as ve: 
        print(f"Error: {ve}")
        return (f"Error: {ve}")
    
    except Exception as e:
        print(f"Error creating directory: {e}")
        return (f"Error creating directory: {e}")


def rmdir(folder_name=None):
    try:
        if folder_name is None or not folder_name.strip(): # Sprawdź, czy folder_name zostało podane
            raise ValueError("Folder name not provided")

        os.rmdir(folder_name) # rmdir usuwa ścieżkę (folder)
        print(f"Directory '{folder_name}' deleted successfully.")
        return (f"Directory '{folder_name}' deleted successfully.")
    
    except FileNotFoundError:
        print(f"Directory '{folder_name}' not found.")
        return (f"Directory '{folder_name}' not found.")
    except PermissionError:
        print(f"Permission denied to delete directory: {folder_name}")
        return (f"Permission denied to delete directory: {folder_name}")
    
    except ValueError as ve: 
        print(f"Error: {ve}") 
        return (f"Error: {ve}") 
    
    except OSError as e:
        print(f"Error deleting directory: {e}")   
        return (f"Error deleting directory: {e}")   
        
"-------------------------------------------------------------------------------------Pliki"
def touch(file_name=None):
    try:
        if file_name is None or not file_name.strip(): # Sprawdź, czy file_name zostało podane
            raise ValueError("File name not provided")

        full_path = os.path.join(os.getcwd(), file_name) # Łączy ściężkę i nazwę pliku

        # Sprawdź, czy plik już istnieje
        if os.path.isfile(full_path):
            print(f"File '{file_name}' already exists.")
            return (f"File '{file_name}' already exists.")
        else:
            # Stwórz plik, jeśli nie istnieje
            with open(full_path, 'w'):  # The 'with' statement ensures proper file closure
                pass  # No need to do anything, the file is created automatically
            print(f"File '{file_name}' created successfully.")
            return (f"File '{file_name}' created successfully.")
        
    except ValueError as ve: 
        print(f"Error: {ve}") 
        return (f"Error: {ve}")
    
    except Exception as e:
        print(f"Error: {e}")  
        return (f"Error: {e}")
    

def rm(file_name=None):
    try:
        if file_name is None or not file_name.strip(): # Sprawdź, czy file_name zostało podane
            raise ValueError("File name not provided")
        
        full_path = os.path.join(os.getcwd(), file_name) # Łączy ściężkę i nazwę pliku

        os.remove(full_path)
        print(f"File {file_name} deleted successfully.")
        return (f"File {file_name} deleted successfully.")
        
    except OSError as e:
        print(f"Error deleting file {file_name}: {e}")
        return (f"Error deleting file {file_name}: {e}")
    except ValueError as ve: 
        
        print(f"Error: {ve}")  
        return (f"Error: {ve}")  

def cat(file_name=None):
    try:
        if file_name is None or not file_name.strip(): # Sprawdź, czy file_name zostało podane
            raise ValueError("File name not provided")

        full_path = os.path.join(os.getcwd(), file_name) # Łączy ściężkę i nazwę pliku

        with open(full_path, 'r') as file:
            content = file.read()
            print("Content:\n"f"{content}")
            return content
        
    except FileNotFoundError:
        print(f"File '{full_path}' not found...")
        return (f"File '{full_path}' not found...")
    
    except ValueError as ve: 
        print(f"Error: {ve}")     
        return (f"Error: {ve}") 
    
    except Exception as e:
        print(f"Error: {e}")
        return (f"Error: {e}")

def rename(file_old_name=None, file_new_name=None):
    try:
        if file_old_name is None or not file_old_name.strip() or file_new_name is None or not file_new_name.strip():
            raise ValueError("Both names must be provided")
        
        file_old_path = os.path.join(os.getcwd(), file_old_name)  # Łączy ściężkę i nazwę pliku
        file_new_path = os.path.join(os.getcwd(), file_new_name)  # Łączy ściężkę i nazwę pliku

        os.rename(file_old_path, file_new_path)
        print(f"Renamed '{file_old_name}' to '{file_new_name}'.")
        return (f"Renamed '{file_old_name}' to '{file_new_name}'.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return (f"Error: {ve}")
     
    except Exception as e:
        print(f"Error renaming: '{e}'.")
        return (f"Error renaming: '{e}'.")
        

def nano_w(file_name=None):
    try:
        if file_name is None or not file_name.strip(): # Sprawdź, czy file_name zostało podane
            raise ValueError("File name not provided")
        with open(file_name, 'a') as file: # Otwieranie pliku w trybie dopisywania - dodawanie kolejych lini
            while True:
                line = input("Enter a line (or 'exit' to finish): ")
                
                if line.lower() == 'exit':
                    break

                file.write(line + '\n')
                print(f"Line '{line}' added to '{file_name}'.")

    except ValueError as ve:
        print(f"Error: {ve}") 
        return (f"Error: {ve}") 
          
    except Exception as e:
        print(f"Error writing to file: {e}")
        return (f"Error writing to file: {e}")

def nano_d():
    try:
        file_name = input("Enter file name: ")
        full_path = os.path.join(os.getcwd(), file_name) # Łączy ściężkę i nazwę pliku

        with open(full_path, 'r') as file:
            lines = file.readlines() # Czytanie lini

        line_number = int(input("Choose text line: "))

        if 1 <= line_number <= len(lines):
            del lines[line_number - 1]
            with open(full_path, 'w') as file: # Nadpisywanie lini
                file.writelines(lines)
            print(f"Line {line_number} deleted from '{full_path}")
        else:
            print(f"Invalid line number: {line_number}. No changes made...")
    except Exception as e:
        print(f"Error: {e}")        

"""
def add_execute_permission(file_name): 
    try:
        file_path = os.path.join(os.getcwd(), file_name)

        if not os.path.exists(file_path): # Sprawdź, czy plik istnieje
            raise FileNotFoundError(f"File not found: {file_path}")

        os.chmod(file_path, 0o755)  # Nadaj uprawnienia do wykonywania (rwxr-xr-x)

        print(f"Added execute permission to file: {file_path}")
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except Exception as e:
        print(f"Error adding execute permission: {e}")

def remove_execute_permission(file_name):
    try:
        full_path = os.path.join(os.getcwd(), file_name) # Łączy ściężkę i nazwę pliku

        current_permissions = os.stat(full_path).st_mode_
        new_permissions = current_permissions & ~(stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        os.chmod(full_path, new_permissions)
        print(f"Removed execute premission to file: {full_path}")
    except Exception as e:
        print(f"Error removing execute premission: {e}")
"""
        
def run(file_path):
    try:
        if file_path is None or not file_path.strip():
            raise ValueError("Directory not provided")
        
        # result = subprocess.check_output(['python', file_path], text=True, stderr=subprocess.STDOUT)
        result = subprocess.run(['python', file_path], check=True, capture_output=True, text=True)
        output = result.stdout
        print(result)
        # return result
        return output
        
    except subprocess.CalledProcessError as pe:
        print(f"Error: {pe}")
        return f"Error: {pe}"
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return f"Error: {ve}"
    
    except Exception as e:
        print(f"Unexpected error: {e}") 
        return f"Error renaming: '{e}'."     

"-------------------------------------------------------------------------------------Wyświetlanie statystyk"
def ls():
    try:
        files = os.listdir()  # Use os.listdir() without a specific path to list files in the current working directory
        for file in files:
            print(file)
        return files    
    
    except Exception as e:
        print(f"Error: {e}")  
        return (f"Error: {e}")  

def lsall(file_name=None):
    try:
        result = ""
        if file_name:
            full_path = os.path.join(os.getcwd(), file_name)
            file_info = os.stat(full_path)

            last_modified_time = datetime.datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            file_mode = stat.filemode(file_info.st_mode)

            print(f"{file_mode}\t{file_info.st_nlink}\t{file_info.st_uid}\t{file_info.st_gid}\t{file_info.st_size}\t{last_modified_time}\t{file_name}\n")
            result += f"{file_mode}\t{file_info.st_nlink}\t{file_info.st_uid}\t{file_info.st_gid}\t{file_info.st_size}\t{last_modified_time}\t{file_name}\n"
        else:
            files = os.listdir()
            for file in files:
                full_path = os.path.join(os.getcwd(), file)
                file_info = os.stat(full_path)

                last_modified_time = datetime.datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                file_mode = stat.filemode(file_info.st_mode)

                print(f"{file_mode}\t{file_info.st_nlink}\t{file_info.st_uid}\t{file_info.st_gid}\t{file_info.st_size}\t{last_modified_time}\t{file}\n")
                result += f"{file_mode}\t{file_info.st_nlink}\t{file_info.st_uid}\t{file_info.st_gid}\t{file_info.st_size}\t{last_modified_time}\t{file}\n"
        return result
    
    except FileNotFoundError:
        print(f"File or directory not found: {file_name}")
        return (f"File or directory not found: {file_name}")
    
    except Exception as e:
        print(f"Error listing files: {e}")
        return (f"Error listing files: {e}")

def cwd():
    current_dir = os.getcwd()
    return current_dir

def cwd_command():
    path = os.getcwd()
    print(path)
    return path

def cd(folder_name=None):
    try:
        if folder_name is None or not folder_name.strip():
            raise ValueError("Directory not provided")

        target_path = os.path.join(os.getcwd(), folder_name) # Łączy ściężkę i nazwę pliku
        os.chdir(target_path)
        print(f"Changed current directory to: {os.getcwd()}")
        return (f"Changed current directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory not found: {folder_name}")
        return (f"Directory not found: {folder_name}")
    
    except PermissionError:
        print(f"Permission denied to access directory: {folder_name}")
        return (f"Permission denied to access directory: {folder_name}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return (f"Error: {ve}")
    
    except Exception as e:
        print(f"Error changing directory: {e}")
        return (f"Error changing directory: {e}")
    
def echo(text=None):
    try:
        if text is None or not text.strip():
            raise ValueError("Text not provided")
        
        print(text)
        return text
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return f"Error: {ve}"
    
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"
        

"-------------------------------------------------------------------------------------Użytkownicy"
users_path = os.path.join(PathConfig.root_path, r"users.txt")
def add_user(username, password):
    if not user_exists(username):
        with open(users_path, "a") as file:
            file.write(f"{username}:{password}\n")
        print(f"Użytkownik {username} dodany pomyślnie.")
        return f"Użytkownik {username} dodany pomyślnie."
    else:
        print(f"Użytkownik {username} już istnieje.")
        return f"Użytkownik {username} już istnieje."

def user_exists(username):
        with open(users_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                existing_user = line.split(":")[0]
                if existing_user == username:
                    return True
        return False

def remove_user(username):
    try:
        with open(users_path, "r") as file:
            lines = file.readlines()
        with open(users_path, "w") as file:
            user_found = False
            for line in lines:
                existing_user = line.split(":")[0]
                if existing_user != username:
                    file.write(line)
                else:
                    user_found = True
            if not user_found:
                print(f"Użytkownik {username} nie istnieje.")
                return f"Użytkownik {username} nie istnieje."
            
        print(f"Użytkownik {username} usunięty pomyślnie.")
        return f"Użytkownik {username} usunięty pomyślnie."
    except Exception as e:
        print(f"Wystąpił błąd podczas usuwania użytkownika: {e}")
        return f"Wystąpił błąd podczas usuwania użytkownika: {e}"

def all_users():
    with open(users_path, "r") as file:
        lines = file.readlines()
        users_list = [line.strip().split(":")[0] for line in lines if ":" in line]
        return users_list
    
def save_current_user(username):
    with open(users_path, "r") as config_file:
        config_lines = config_file.readlines()

    with open(users_path, "w") as config_file:
        for line in config_lines:
            if line.startswith("CURRENT_USER = "):
                config_file.write(f'CURRENT_USER = "{username}"\n')
            else:
                config_file.write(line)

def current_user():
    with open(users_path, "r") as config_file:
        config_lines = config_file.readlines()

    for line in config_lines:
        if line.startswith("CURRENT_USER = "):
            return line.split("=")[1].strip().strip('"')

    return None


"-------------------------------------------------------------------------------------Obsługa systemu"
def help():
    full_path = os.path.join(PathConfig.root_path, r"Documentations\commands-info.txt")
    with open(full_path) as file:
            content = file.read()
    return content      

def updateshistory():
    full_path = os.path.join(PathConfig.root_path, r"Documentations\ulix-updates-history.txt")
    with open(full_path) as file:
            content = file.read()
    return content  

def os_version():
    with open("Config.py", "r") as config_file:
        config_lines = config_file.readlines()

    for line in config_lines:
        if line.startswith("osversion = "):
            return line.split("=")[1].strip().strip('"')

    return None  


def load_settings():
    import customtkinter
    customtkinter.set_appearance_mode(Config.appearance_MODE) # Ustawia zapisany wcześniej motyw