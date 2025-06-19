import os

def clear_screen(command):
    os.system(command)  # ❌ SECURITY: ejecución sin sanitización
