import os
import subprocess

# Dossier contenant les scripts Python
script_dir = "python"

# Vérifiez si le dossier existe
if not os.path.exists(script_dir):
    print(f"Le dossier '{script_dir}' n'existe pas.")
    exit(1)

# Liste tous les fichiers dans le dossier
scripts = [f for f in os.listdir(script_dir) if f.endswith('.py')]

# Vérifiez s'il y a des scripts Python dans le dossier
if not scripts:
    print(f"Aucun script Python trouvé dans le dossier '{script_dir}'.")
    exit(1)

# Exécute chaque script
for script in scripts:
    script_path = os.path.join(script_dir, script)
    print(f"Exécution de {script_path}")
    try:
        result = subprocess.run(["python", script_path], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {script_path} : {e.stderr}")

print("Tous les scripts ont été exécutés.")
