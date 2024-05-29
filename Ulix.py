#  _______________________________________
# |        Xsanos Systems Studio®         |
# |_______________________________________|

# This is part of the Ulix
# This module is the main file of the system

import os
from PathConfig import root_path
from sbin import functions

import tkinter as tk
from tkinter import colorchooser, filedialog
import customtkinter
from PIL import ImageTk, Image


def back(parent_window):
    parent_window.destroy()
    main(parent_window)

def shutdown(parent_window):
    functions.save_current_user("")
    parent_window.destroy()
    shutdown_win = customtkinter.CTkFrame(master=root_win)
    shutdown_win.pack()

    res_path = os.path.join(root_path, r"Res\background.jpg")
    bg_pic = customtkinter.CTkImage(Image.open(res_path), size=(1280, 720))
    background_boot = customtkinter.CTkLabel(master=shutdown_win, image=bg_pic, text="U L I X", text_color="#3D7399", bg_color="transparent", font=customtkinter.CTkFont("Helvetica", size=90, weight="bold"))
    background_boot.pack()

    shutdown_win.after(3000, lambda: root_win.destroy())

"---------------------------------------------------------------------------ramka Procesu Wczytywania"
def boot_window():
    global boot_win
    boot_win = customtkinter.CTkFrame(master=root_win)
    boot_win.pack()

    res_path = os.path.join(root_path, r"Res\background.jpg")
    bg_pic = customtkinter.CTkImage(Image.open(res_path), size=(1280, 720))
    background_boot = customtkinter.CTkLabel(master=boot_win, image=bg_pic, text="U L I X", text_color="#3D7399", bg_color="transparent", font=customtkinter.CTkFont("Helvetica", size=90, weight="bold"))
    background_boot.pack()

    global progress_bar
    progress_bar = customtkinter.CTkProgressBar(master=background_boot, width=420, height=20, corner_radius=0, determinate_speed=1)
    progress_bar.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    progress_bar.set(value=0)

    num_steps = 1000
    def start_loading():
        print("START LOADING") # debuging
        progress_bar.set(0)
        progress_val = 1/num_steps
        stepVal = 0
        for i in range(num_steps):
            for j in range(100000):
                pass
            stepVal = stepVal + progress_val
            progress_bar.set(stepVal)
            progress_bar.update_idletasks()
        print("LOADING PASSED") # debuging
        boot_win.after(1000, boot_win.destroy())
        login_window(boot_win)  

    boot_win.after(1000, start_loading)


"---------------------------------------------------------------------------ramka Logowania"
def login_window(parent_window):
    parent_window.destroy()
    login_win = customtkinter.CTkFrame(master=root_win)
    login_win.pack()

    res_path = os.path.join(root_path, r"Res\background.jpg")
    bg_pic = customtkinter.CTkImage(Image.open(res_path),size=(1280,720))
    background_login = customtkinter.CTkLabel(master=login_win, image=bg_pic)
    background_login.pack()

    login_win_container = customtkinter.CTkLabel(master=login_win, width=1080, height=620, text="")
    login_win_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    header = customtkinter.CTkLabel(master=login_win_container, text="Witamy!", font=customtkinter.CTkFont("Helvetica", size=28, weight="bold"))
    header.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    user_name = customtkinter.CTkEntry(master=login_win_container, width=400, height=50, placeholder_text="Nazwa Użytkownika")
    user_name.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

    user_password = customtkinter.CTkEntry(master=login_win_container, width=400, height=50, placeholder_text="Hasło", show="*")
    user_password.place(relx=0.5, rely=0.64, anchor=tk.CENTER)

    check_btn = customtkinter.CTkButton(master=login_win_container, width=190, height=40, text="Zaloguj", command=lambda:get_parameters())
    check_btn.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    def get_parameters():
        print("CHECKING PASSWORDS") # debuging
        username = user_name.get()
        password = user_password.get()
        check_user(username, password)

    def check_user(username, password): 
        if functions.user_exists(username):
            ful_path = os.path.join(root_path, r"users.txt")
            with open(ful_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(":")
                    if len(parts) == 2:
                        stored_username, stored_password = parts
                        if stored_username == username and stored_password == password:
                            print("LOGIN SUCCESSFUL") # debuging
                            functions.save_current_user(username)
                            header.configure(text=f"Zalogowano jako {username}")
                            login_win.after(2500, lambda: main(login_win))
                            return
                print("INCORRECT PASSWORD") # debuging
        else:
            print("USER DOES NOT EXISTS") # debuging


"---------------------------------------------------------------------------Główna Ramka"
def main(parent_window):
    parent_window.destroy()
    main_win = customtkinter.CTkFrame(master=root_win)
    main_win.pack()

    res_path = os.path.join(root_path, r"Res\background.jpg")
    bg_pic = customtkinter.CTkImage(Image.open(res_path), size=(1280, 720))
    background_main = customtkinter.CTkLabel(master=main_win, image=bg_pic)
    background_main.pack()

    main_container = customtkinter.CTkLabel(master=background_main, width=1080, height=620, text="")
    main_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # wiersz poleceń
    res_path = os.path.join(root_path, r"Res\compr.png")
    compr_pic = customtkinter.CTkImage(Image.open(res_path),size=(30,30))
    compr_button = customtkinter.CTkButton(master=main_container, width=150, height=100, text="Wiersz Poleceń",image=compr_pic, corner_radius=8, command=lambda: command_window(main_win))
    compr_button.place(x=150, y=100, anchor=tk.CENTER)

    # paint
    res_path = os.path.join(root_path, r"Res\paint.png")
    paint_pic = customtkinter.CTkImage(Image.open(res_path),size=(30,30))
    paint_button = customtkinter.CTkButton(master=main_container, width=150, height=100, text="Paint",image=paint_pic, corner_radius=8, command=lambda: paint_app(main_win))
    paint_button.place(x=150, y=210, anchor=tk.CENTER)

    # notatnik
    res_path = os.path.join(root_path, r"Res\notes.png")
    notes_pic = customtkinter.CTkImage(Image.open(res_path),size=(30,30))
    notes_button = customtkinter.CTkButton(master=main_container, width=150, height=100, text="Notatnik",image=notes_pic, corner_radius=8, command=lambda: notes_app(main_win))
    notes_button.place(x=150, y=320, anchor=tk.CENTER)

    # start menu sidebar
    def start_sidebar():
        start_menu = customtkinter.CTkLabel(master=main_container, width=350, height=565, text="", bg_color="#181717")
        def toggle_start_menu():
            if start_menu.winfo_ismapped():
                start_menu.place_forget()  # Hide the menu if it's currently visible
            else:
                start_menu.place(relx=0, rely=0, anchor=tk.NW)  # Tworzy warstwę    

        power_menu = customtkinter.CTkLabel(master=start_menu, width=295, height=55, text="", bg_color="#1d1a1a")
        def toggle_power_menu():
            
            if power_menu.winfo_ismapped():
                power_menu.place_forget()  # Hide the menu if it's currently visible
            else:
                power_menu.place(relx=1, rely=1, anchor=tk.SE)  # Tworzy warstwę    

        # ustawienia
        res_path = os.path.join(root_path, r"Res\settings.png")
        settings_pic = customtkinter.CTkImage(Image.open(res_path), size=(30, 30))
        settings_button = customtkinter.CTkButton(master=start_menu, width=55, height=55, text="", image=settings_pic, corner_radius=0, command=lambda: settings_app(main_win))
        settings_button.place(x=0, y=511, anchor=tk.SW)

        # menu zasilania
        res_path = os.path.join(root_path, r"Res\power.png")
        power_pic = customtkinter.CTkImage(Image.open(res_path), size=(30, 30))
        toggle_power_button = customtkinter.CTkButton(master=start_menu, width=55, height=55, image=power_pic, text="", corner_radius=0, command=toggle_power_menu)
        toggle_power_button.place(x=0, rely=1.001, anchor=tk.SW)

        logout_button = customtkinter.CTkButton(master=power_menu, width=296, height=27.5, text="Wyloguj", fg_color="#121111", hover_color="#666666", corner_radius=0, command=lambda: login_window(main_win))
        logout_button.place(x=0, y=0, anchor=tk.NW)

        close_button = customtkinter.CTkButton(master=power_menu, width=296, height=27.5, text="Zamknij", fg_color="#121111", hover_color="#666666", corner_radius=0, command=lambda: shutdown(main_win))
        close_button.place(x=0, rely=1, anchor=tk.SW)

        # przełącznik start_menu
        toggle_menu_button = customtkinter.CTkButton(master=main_container, width=55, height=55, text="Start", corner_radius=0, command=toggle_start_menu)
        toggle_menu_button.place(x=0, rely=1.001, anchor=tk.SW)

    # przełącznik start_menu
    start_button = customtkinter.CTkButton(master=main_container, width=55, height=55, text="Start", corner_radius=0, command=start_sidebar)
    start_button.place(x=0, rely=1.001, anchor=tk.SW)

  

"---------------------------------------------------------------------------ramka Wiersza Poleceń"
def execute_command(entry, text_output):
    action = text_output.get("1.0", tk.END).strip()
    action = entry.get()
    result = ""
    #-------------------------------------------------------------------------------------Foldery
    if action.startswith("mkdir"): 
        folder_name = action.replace("mkdir", "").strip() # Pobiera nazwę folderu z komendy, pomijając "mkdir"
        result += functions.mkdir(folder_name)
        result += '\n'


    elif action.startswith("rmdir"):
        folder_name = action.replace("rmdir", "").strip() # Pobiera nazwę folderu z komendy, pomijając "rmdir"
        result += functions.rmdir(folder_name)
        result += '\n'

    #-------------------------------------------------------------------------------------Pliki
    elif action.startswith("touch"): # touch nazwa_pliku
        # Pobierz nazwę pliku z komendy, pomijając "touch"
        file_name = action.replace("touch", "").strip()
        result += functions.touch(file_name)
        result += '\n'

    elif action.startswith("rm"): # rm nazwa_pliku
        # Pobierz nazwę pliku z komendy, pomijając "rm"
        file_name = action.replace("rm", "").strip()
        result += functions.rm(file_name)
        result += '\n'

    elif action.startswith("cat"): 
        file_name = action.replace("cat", "").strip()
        result = functions.cat(file_name)
        result += '\n'          

    elif action.startswith("rename"):
        command_parts = action.replace("rename", "").strip().split() # Pobiera nazwę pliku z komendy, pomijając "rename"
        try:
            if len(command_parts) == 2:  # Czy są obie nazwy w inpucie
                file_old_name, file_new_name = command_parts
                functions.rename(file_old_name, file_new_name)
            else:
                raise ValueError("Both file names must be provided.")
        except ValueError as ve:
            print(f"Error: {ve}")

    # elif action.startswith("nano -w"): #poprawić
    #     file_name = action.replace("nano -w", "").strip()
    #     result += functions.nano_w(file_name)
    #     result += '\n' 

    # elif action.startswith("nano -d"): #poprawić
    #     file_name = action.replace("nano -d", "").strip()
    #     result += functions.nano_d(file_name)
    #     result += '\n'

    elif action.startswith("run"): 
        file_name = action.replace("run", "").strip() # Pobiera nazwę folderu z komendy, pomijając "mkdir"
        result += functions.run(file_name)
        result += '\n'     

    #-------------------------------------------------------------------------------------Wyświetlanie statystyk
    elif action =="ls":
        files_list = functions.ls()
        result = "\n".join(files_list)
        result += '\n'

    elif action.startswith("ls -all"):
        file_name = action.replace("ls -all", "").strip()
        result = functions.lsall(file_name)
        
    elif action == "cwd":
        result = functions.cwd_command()  
        result += '\n'
        
    elif action.startswith("cd"):
        folder_name = action.replace("cd", "").strip() # Pobiera nazwę folderu z komendy, pomijając "cd"
        result += functions.cd(folder_name)
        console_input_path()
        result += '\n'  

    elif action.startswith("echo"):
        text = action.replace("echo", "").strip()
        result += functions.echo(text)
        result += '\n'   

    #-------------------------------------------------------------------------------------Użytkownicy
    elif action.startswith("useradd"):
        command_parts = action.replace("useradd", "").strip().split()
        if len(command_parts) == 2:  # Check if both username and password are provided
            username, password = command_parts
            result = functions.add_user(username, password)
            result += '\n'  
        else: 
            result += ("Both username and password must be provided.")    

    elif action.startswith("userdel"):
        username = action.replace("userdel", "").strip()
        result += functions.remove_user(username)
        result += '\n'          

    elif action == "users":
        users_list = functions.all_users()
        result += "\n".join(users_list)
        result += '\n' 

    elif action == "whoami":
        user = functions.current_user()
        result += user
        result += '\n'     
    #-------------------------------------------------------------------------------------Obsługa systemu
    elif action == "cls": # Wyczyść konsolę
        text_output.delete(1.0, tk.END)

    elif action == "help":
        result = functions.help()
        result += '\n'

    elif action == "patchnotes":
        result = functions.updateshistory()
        result += '\n'    

    elif action == "osver":
        version = functions.os_version()
        result = version
        result += '\n'           

    else:
        result += "Unknown command. Type 'help' to open documentation"

    text_output.insert(tk.END, result +'\n') # Wstawia do pola tekstowego

def path():
    username = functions.current_user()  # Użyj funkcji current_user() do pobrania aktualnie zalogowanego użytkownika
    return f"{username}:{functions.cwd()}>"

def console_input_path():
    path_win.configure(text=path())   

def command_window(parent_window):
    parent_window.destroy()

    command_prompt_win = customtkinter.CTkFrame(master=root_win)
    command_prompt_win.pack()

    res_path = os.path.join(root_path, r"Res\background.jpg")
    bg_pic = customtkinter.CTkImage(Image.open(res_path),size=(1280,720))
    background_explorer = customtkinter.CTkLabel(master=command_prompt_win, image=bg_pic)
    background_explorer.pack()

    container = customtkinter.CTkFrame(master=background_explorer, width=1080, height=620, corner_radius=15)
    container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    header = customtkinter.CTkLabel(master=container, text="Wiersz Poleceń",font=customtkinter.CTkFont(size=25))
    header.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    
    entry = customtkinter.CTkEntry(master=container, width=450, height=40)
    entry.place(relx=0.5, rely=0.19, anchor=tk.CENTER)
    entry.bind("<Return>",lambda event:execute_command(entry, text_output))

    command_button = customtkinter.CTkButton(master=container, width=100, height=40, text="Uruchom", command=lambda: execute_command(entry, text_output))
    command_button.place(relx=0.77, rely=0.2, anchor=tk.CENTER)
      
    global path_win
    path_win = customtkinter.CTkLabel(master=container, text=path(),font=customtkinter.CTkFont(size=13))
    path_win.place(relx=0.5, rely=0.27, anchor=tk.CENTER)

    text_output = customtkinter.CTkTextbox(master=container, width=1020, height=378, wrap=tk.WORD, font=customtkinter.CTkFont(size=13)) # wartości wielkości się dziwnie podaje LOL
    text_output.place(relx=0.5, rely=0.61, anchor=tk.CENTER)

    close_button = customtkinter.CTkButton(master=container, width=120, height=40, text="Wróć", command=lambda:back(command_prompt_win))
    close_button.place(relx=0.9, rely=0.956, anchor=tk.CENTER)


"---------------------------------------------------------------------------ramka Paint"
def paint_app(parent_window):
    parent_window.destroy() 
    paint_win = customtkinter.CTkFrame(master=root_win)
    paint_win.pack()

    def save_layout(canvas, file_path):
        # Save the canvas content as an image file (JPEG format)
        canvas.postscript(file=file_path, colormode="color")
        img = Image.open(file_path)
        img.save(file_path.replace(".eps", ".jpg"), "JPEG")

    def import_layout(canvas, file_path):
        # Open the JPEG file and create a PIL Image
        image = Image.open(file_path)
        image = image.resize((1280, 660), Image.ADAPTIVE)  # Resize the image to fit the canvas

        # Convert the PIL Image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image)

        # Create a canvas image with the PhotoImage
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo

    start_x, start_y = None, None  # Define start_x and start_y here
    line_width = 5  # Initial line width
    color = "black"  # Initial color

    def paint(event):
        nonlocal start_x, start_y  # Use nonlocal inside the function
        x, y = event.x, event.y
        if start_x is not None and start_y is not None:
            canvas.create_line((start_x, start_y, x, y), width=line_width, fill=color, capstyle=tk.ROUND, smooth=tk.TRUE)

        start_x = x
        start_y = y

    def reset(event):
        nonlocal start_x, start_y
        start_x = None
        start_y = None

    def choose_color():
        nonlocal color
        color = colorchooser.askcolor()[1]

    def set_thickness(val):
        nonlocal line_width
        line_width = int(val)

    def clear_canvas():
        canvas.delete("all")

    def save_image():
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        if file_path:
            save_layout(canvas, file_path)

    def open_image():
        file_path = filedialog.askopenfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        if file_path:
            import_layout(canvas, file_path)


    start_x, start_y = None, None
    color = "black"
    line_width = 2


    # ramka wypychająca przestrzeń, czasem nie wypycha :(
    container = customtkinter.CTkLabel(master=paint_win, width=1280, height=720, text="") 
    container.pack()
    
    canvas = tk.Canvas(master=container,bg="white", width=1280, height=720)
    canvas.bind("<B1-Motion>", paint)
    canvas.bind("<ButtonRelease-1>", reset)
    canvas.place(relx=0.5, rely=0, anchor=tk.N)

    paint_win_container = customtkinter.CTkLabel(master=container, width=1280, height=60, text="") 
    paint_win_container.place(relx=0.5, rely=1, anchor=tk.S)

    color_button = customtkinter.CTkButton(master=paint_win_container, width=100, height=40, text="Kolor", command=choose_color)
    color_button.place(relx=0.1, rely=0.5, anchor=tk.CENTER)

    clear_button = customtkinter.CTkButton(master=paint_win_container, width=100, height=40, text="Wyczyść", command=clear_canvas)
    clear_button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

    thickness_label = customtkinter.CTkLabel(master=paint_win_container, text="Grubość Lini")
    thickness_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

    thickness_slider = customtkinter.CTkSlider(master=paint_win_container, from_=1, to=10, number_of_steps=8, command=set_thickness)
    thickness_slider.set(1)
    thickness_slider.place(relx=0.41, rely=0.5, anchor=tk.CENTER)

    save_button = customtkinter.CTkButton(master=paint_win_container, width=100, height=40, text="Zapisz", command=save_image)
    save_button.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

    open_button = customtkinter.CTkButton(master=paint_win_container, width=100, height=40, text="Otwórz", command=open_image)
    open_button.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    close_button = customtkinter.CTkButton(master=paint_win_container, width=120, height=40, text="Wróć", command=lambda:back(paint_win))
    close_button.place(relx=0.9, rely=0.5, anchor=tk.CENTER)


"---------------------------------------------------------------------------ramka Notatnika"
def notes_app(parent_window):
    parent_window.destroy()
    notes_win = customtkinter.CTkFrame(master=root_win)
    notes_win.pack()

    def save_file():
        caption.set("Plik")
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_box.get("1.0", tk.END))

    def open_file():
        caption.set("Plik")
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text_box.delete("1.0", tk.END)
                text_box.insert(tk.END, content)   
                
    def choose(action):
        if action == "Zapisz":
            save_file()
        elif action == "Otwórz":
            open_file()  

    notes_container = customtkinter.CTkLabel(master=notes_win, width=1280, height=720, text="")
    notes_container.pack()

    notes_btn_container = customtkinter.CTkLabel(master=notes_win, width=1280, height=60, text="")
    notes_btn_container.place(relx=0.5, rely=0.96, anchor=tk.CENTER)

    text_box = customtkinter.CTkTextbox(master=notes_win, wrap="word", width=1280, height=615)
    text_box.place(relx=0.5, rely=0.49, anchor=tk.CENTER)

    caption = tk.StringVar(notes_win)
    caption.set("Plik")
    options = ["Otwórz", "Zapisz"]
    menu = customtkinter.CTkOptionMenu(master=notes_win, width=120, height=30,variable=caption, values=options,command=choose)
    menu.place(relx=0.06, rely=0.03, anchor=tk.CENTER)
    
    close_button = customtkinter.CTkButton(master=notes_btn_container, width=120, height=40, text="Wróć", command=lambda:back(notes_win))
    close_button.place(relx=0.9, rely=0.5, anchor=tk.CENTER)


"---------------------------------------------------------------------------ramka Ustawień"
def settings_app(parent_window):
    parent_window.destroy()
    settingss_win = customtkinter.CTkFrame(master=root_win)
    settingss_win.pack()

    res_path = os.path.join(root_path, r"Res\background.jpg")
    bg_pic = customtkinter.CTkImage(Image.open(res_path),size=(1280,720))
    background_options = customtkinter.CTkLabel(master=settingss_win, image=bg_pic)
    background_options.pack()

    settings_container = customtkinter.CTkLabel(master=settingss_win, width=1080, height=620, text="")
    settings_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    motiv_description = tk.StringVar()
    motiv_description.set("Motyw Systemu") # ustawia statyczny napis, bo dynamiczy nie działa

    def choose(action):
        if action == "Ciemny":
            update_appearance_mode("Dark")
            motiv_description.set("Motyw Systemu") 
        elif action == "Jasny":
            update_appearance_mode("Light")
            motiv_description.set("Motyw Systemu")
        
    def update_appearance_mode(mode):
        with open("Config.py", "r") as config_file:
            config_lines = config_file.readlines()

        with open("Config.py", "w") as config_file:
            for line in config_lines:
                if line.startswith("appearance_MODE = "):
                    config_file.write(f'appearance_MODE = "{mode}"\n')
                else:
                    config_file.write(line)
        customtkinter.set_appearance_mode(mode)

    motiv_button = customtkinter.CTkOptionMenu(master=settings_container, width=100,height=35, variable=motiv_description, values=["Ciemny", "Jasny"], command=choose)
    motiv_button.place(x=120, y=50, anchor=tk.CENTER)

    close_button = customtkinter.CTkButton(master=settings_container, width=120, height=40, text="Wróć", command=lambda: back(settingss_win))
    close_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)


"---------------------------------------------------------------------------Okno Główne"

root_win = customtkinter.CTk()
root_win.geometry("1280x720")
root_win.resizable(False, False)
root_win.title("Ulix")

functions.load_settings()
boot_window()

root_win.mainloop()
