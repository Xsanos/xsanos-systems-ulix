import subprocess
libraries = ["pillow", "tk", "pip", "customtkinter"]
for library in libraries:
    try:
        subprocess.run(["pip","install", library], check=True)
    except subprocess.CalledProcessError as pe:
        print(f"Błąd podzczas instalacji {library}: {pe}")    