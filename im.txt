import subprocess
import os

def execute_script(script_path):
    try:
        result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True)
        print(f"Successfully executed {script_path}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}: {e}")
        print("Standard Output:\n", e.stdout)
        print("Error Output:\n", e.stderr)

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    python_directory = os.path.join(script_directory, "python")

    # Récupérer tous les fichiers Python dans le dossier "python"
    scripts = [os.path.join(python_directory, f).replace("\\", "/") for f in os.listdir(python_directory) if f.endswith('.py')]

    for script in scripts:
        execute_script(script)
